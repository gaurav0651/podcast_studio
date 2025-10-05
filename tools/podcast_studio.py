import concurrent.futures
import io
import random
import warnings
from collections.abc import Generator
from typing import Any, Optional, Union

import openai
from yarl import URL

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from pydub import AudioSegment  # type: ignore


class PodcastStudioTool(Tool):
    @staticmethod
    def _generate_silence(duration: float) -> AudioSegment:
        # Generate silent WAV data using pydub
        silence = AudioSegment.silent(duration=int(duration * 1000))  # pydub uses milliseconds
        return silence

    @staticmethod
    def _generate_audio_segment_openai(
        client: openai.OpenAI,
        line: str,
        voice: str,
        index: int,
    ) -> tuple[int, Union[AudioSegment, str], Optional[AudioSegment]]:
        try:
            response = client.audio.speech.create(
                model="tts-1", 
                voice=voice, 
                input=line.strip(), 
                response_format="wav"
            )
            audio = AudioSegment.from_wav(io.BytesIO(response.content))
            silence_duration = random.uniform(0.1, 1.5)
            silence = PodcastStudioTool._generate_silence(silence_duration)
            return index, audio, silence
        except Exception as e:
            return index, f"Error generating audio with OpenAI: {str(e)}", None

    @staticmethod
    def _generate_audio_segment_elevenlabs(
        api_key: str,
        line: str,
        voice_id: str,
        index: int,
    ) -> tuple[int, Union[AudioSegment, str], Optional[AudioSegment]]:
        try:
            import requests
            
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": api_key
            }
            
            data = {
                "text": line.strip(),
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }
            
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code != 200:
                return index, f"ElevenLabs API error: {response.status_code} - {response.text}", None
            
            # Convert MP3 to AudioSegment
            audio = AudioSegment.from_mp3(io.BytesIO(response.content))
            silence_duration = random.uniform(0.1, 1.5)
            silence = PodcastStudioTool._generate_silence(silence_duration)
            return index, audio, silence
            
        except ImportError:
            return index, "requests library is required for ElevenLabs TTS", None
        except Exception as e:
            return index, f"Error generating audio with ElevenLabs: {str(e)}", None

    def _parse_voice_selection(self, voice_selection: str) -> tuple[str, str]:
        """Parse voice selection in format 'service:voice_id' or 'service:voice_name'"""
        if ":" not in voice_selection:
            # Default to OpenAI for backward compatibility
            return "openai", voice_selection
        
        service, voice = voice_selection.split(":", 1)
        return service.lower(), voice

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Extract parameters
        script = tool_parameters.get("script", "")
        host1_voice = tool_parameters.get("host1_voice")
        host2_voice = tool_parameters.get("host2_voice")

        # Split the script into lines
        script_lines = [line for line in script.split("\n") if line.strip()]

        # Ensure voices are provided
        if not host1_voice or not host2_voice:
            yield self.create_text_message("Error: Host voices are required")
            return

        # Parse voice selections
        host1_service, host1_voice_id = self._parse_voice_selection(host1_voice)
        host2_service, host2_voice_id = self._parse_voice_selection(host2_voice)

        # Ensure runtime and credentials
        if not self.runtime or not self.runtime.credentials:
            raise ToolProviderCredentialValidationError("Tool runtime or credentials are missing")

        # Get credentials
        tts_service = self.runtime.credentials.get("tts_service")
        api_key = self.runtime.credentials.get("api_key")
        
        if not api_key:
            raise ToolProviderCredentialValidationError("API key is missing")

        # Validate that voice selections match the configured TTS service or allow mixed usage
        openai_client = None
        elevenlabs_api_key = None
        
        if tts_service == "openai":
            # Initialize OpenAI client
            openai_base_url = self.runtime.credentials.get("openai_base_url", None)
            openai_base_url = str(URL(openai_base_url) / "v1") if openai_base_url else None
            openai_client = openai.OpenAI(api_key=api_key, base_url=openai_base_url)
        elif tts_service == "elevenlabs":
            elevenlabs_api_key = api_key
        else:
            yield self.create_text_message(f"Error: Unsupported TTS service: {tts_service}")
            return

        # Validate that we have content to process
        if not script_lines:
            yield self.create_text_message("Error: Script is empty or contains no valid lines")
            return

        # Create a thread pool
        max_workers = 5
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for i, line in enumerate(script_lines):
                voice_service = host1_service if i % 2 == 0 else host2_service
                voice_id = host1_voice_id if i % 2 == 0 else host2_voice_id
                
                # Check if the voice service matches the configured TTS service
                if tts_service == "openai" and voice_service != "openai":
                    yield self.create_text_message(f"Error: Voice {voice_id} requires ElevenLabs service, but OpenAI is configured")
                    return
                elif tts_service == "elevenlabs" and voice_service != "elevenlabs":
                    yield self.create_text_message(f"Error: Voice {voice_id} requires OpenAI service, but ElevenLabs is configured")
                    return
                
                if voice_service == "openai":
                    future = executor.submit(self._generate_audio_segment_openai, openai_client, line, voice_id, i)
                elif voice_service == "elevenlabs":
                    future = executor.submit(self._generate_audio_segment_elevenlabs, elevenlabs_api_key, line, voice_id, i)
                else:
                    yield self.create_text_message(f"Error: Unsupported voice service: {voice_service}")
                    return
                
                futures.append(future)

            # Collect results
            audio_segments: list[Any] = [None] * len(script_lines)
            for future in concurrent.futures.as_completed(futures):
                index, audio, silence = future.result()
                if isinstance(audio, str):  # Error occurred
                    yield self.create_text_message(audio)
                    return
                audio_segments[index] = (audio, silence)

        # Combine audio segments in the correct order
        combined_audio = AudioSegment.empty()
        for i, (audio, silence) in enumerate(audio_segments):
            if audio:
                combined_audio += audio
                if i < len(audio_segments) - 1 and silence:
                    combined_audio += silence

        # Export the combined audio to an MP3 file in memory instead of WAV
        buffer = io.BytesIO()
        combined_audio.export(buffer, format="mp3", bitrate="128k")  # 128k bitrate for good quality/size balance
        mp3_bytes = buffer.getvalue()

        # Create messages with the combined audio
        yield self.create_text_message("Audio generated successfully")
        yield self.create_blob_message(
            blob=mp3_bytes,
            meta={"mime_type": "audio/mpeg"},
        )
