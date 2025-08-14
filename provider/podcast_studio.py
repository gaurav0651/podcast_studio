from typing import Any

import openai
from yarl import URL

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class PodcastStudioProvider(ToolProvider):
    
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        tts_service = credentials.get("tts_service")
        api_key = credentials.get("api_key")
        base_url = credentials.get("openai_base_url")

        if not tts_service:
            raise ToolProviderCredentialValidationError("TTS service is not specified")

        if not api_key:
            raise ToolProviderCredentialValidationError("API key is missing")

        if tts_service == "openai":
            if base_url:
                base_url = str(URL(base_url) / "v1")
            self._validate_openai_credentials(api_key, base_url)
        elif tts_service == "elevenlabs":
            self._validate_elevenlabs_credentials(api_key)
        else:
            raise ToolProviderCredentialValidationError(f"Unsupported TTS service: {tts_service}")

    def _validate_openai_credentials(self, api_key: str, base_url: str | None) -> None:
        client = openai.OpenAI(api_key=api_key, base_url=base_url)
        try:
            # We're using a simple API call to validate the credentials
            client.models.list()
        except openai.AuthenticationError:
            raise ToolProviderCredentialValidationError("Invalid OpenAI API key")
        except Exception as e:
            raise ToolProviderCredentialValidationError(f"Error validating OpenAI API key: {str(e)}")

    def _validate_elevenlabs_credentials(self, api_key: str) -> None:
        try:
            import requests
            
            headers = {
                "Accept": "application/json",
                "xi-api-key": api_key
            }
            
            response = requests.get("https://api.elevenlabs.io/v1/user", headers=headers, timeout=10)
            
            if response.status_code == 401:
                raise ToolProviderCredentialValidationError("Invalid ElevenLabs API key")
            elif response.status_code != 200:
                raise ToolProviderCredentialValidationError(f"ElevenLabs API returned status code: {response.status_code}")
                
        except requests.RequestException as e:
            raise ToolProviderCredentialValidationError(f"Error validating ElevenLabs API key: {str(e)}")
        except ImportError:
            raise ToolProviderCredentialValidationError("requests library is required for ElevenLabs validation")

    #########################################################################################
    # If OAuth is supported, uncomment the following functions.
    # Warning: please make sure that the sdk version is 0.4.2 or higher.
    #########################################################################################
    # def _oauth_get_authorization_url(self, redirect_uri: str, system_credentials: Mapping[str, Any]) -> str:
    #     """
    #     Generate the authorization URL for podcast_studio OAuth.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR AUTHORIZATION URL GENERATION HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return ""
        
    # def _oauth_get_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], request: Request
    # ) -> Mapping[str, Any]:
    #     """
    #     Exchange code for access_token.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR CREDENTIALS EXCHANGE HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return dict()

    # def _oauth_refresh_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], credentials: Mapping[str, Any]
    # ) -> OAuthCredentials:
    #     """
    #     Refresh the credentials
    #     """
    #     return OAuthCredentials(credentials=credentials, expires_at=-1)
