# 🎙️ Podcast Studio Plugin

**Author:** gaurav0651  
**Plugin Name:** podcast_studio  
**Repository URL:** https://github.com/gaurav0651/podcast_studio

## Overview

Transform text scripts into professional podcast audio with AI-powered voices. This plugin brings **new value to Dify** by enabling content creators to generate high-quality, multi-host podcast conversations directly within their Dify workflows, eliminating the need for expensive recording equipment or voice actors.

### Key Value Propositions
- **Workflow Integration**: Seamlessly generate podcast audio within Dify workflows
- **Multi-TTS Support**: Choose between OpenAI and ElevenLabs for optimal quality/cost balance  
- **Professional Quality**: Studio-grade voices with various accents and characteristics
- **Time Savings**: Convert scripts to audio in minutes instead of hours of recording/editing
- **Cost Effective**: No need for professional voice actors or recording studios

## Features

- Generate podcast audio using OpenAI or ElevenLabs Text-to-Speech
- Support for multiple host voices with distinct characteristics
- Australian accent voices (Stuart, Lee, Amelia, Maya, Sophia)
- American premium voices (Rachel, Drew, Clyde, Paul, Domi)
- British voices (Dave)  
- Mixed TTS service support (use different services for each host)
- Production-grade audio generation optimized for podcast content

## Supported TTS Services

### OpenAI TTS
- **Voices:** Alloy, Echo, Fable, Onyx, Nova, Shimmer
- **Languages:** 29+ supported languages
- **Quality:** High-quality neural voices
- **Cost:** Pay-per-character usage

### ElevenLabs
- **Voices:** 11 premium voices with various accents and styles
- **Specialties:** Australian, American, and British accents
- **Quality:** Studio-grade voice synthesis
- **Cost:** Subscription-based with character limits

## Setup Instructions

### Step 1: Install the Plugin

1. Download the latest `.difypkg` file from the [releases page](https://github.com/gaurav0651/podcast_studio/releases)
2. In your Dify instance, navigate to **Tools** → **Plugins**
3. Click **"Install Plugin"** and upload the `.difypkg` file
4. Wait for installation confirmation message
5. Verify the plugin appears in your available tools list

### Step 2: Configure API Credentials

#### For OpenAI TTS:
1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key with TTS permissions
3. In Dify, go to plugin settings and select **"OpenAI TTS"**
4. Enter your OpenAI API key in the API Key field
5. (Optional) Set custom base URL if using a proxy or custom endpoint
6. Click **"Test Connection"** to verify setup

#### For ElevenLabs:
1. Visit [ElevenLabs API Keys](https://elevenlabs.io/app/settings/api-keys)
2. Create a new API key 
3. In Dify, go to plugin settings and select **"ElevenLabs"**
4. Enter your ElevenLabs API key in the API Key field
5. Click **"Test Connection"** to verify setup

### Step 3: Verify Installation

1. Create a new workflow in Dify
2. Add the **"Podcast Studio"** tool from the tools panel
3. Configure your desired voices for Host 1 and Host 2
4. Test with a sample script:
   ```
   Host 1: Welcome to our test podcast!
   Host 2: Thanks for having me. This is exciting!
   ```
5. Run the workflow and verify audio generation

## Usage Instructions

### Basic Usage

1. **Add the Tool:** In your Dify workflow, drag the "Podcast Studio" tool into your workflow
2. **Configure Voices:** 
   - Select voice for Host 1 (e.g., "Stuart - Australian Male, Energetic")
   - Select voice for Host 2 (e.g., "Sophia - Australian Female, Bright")
3. **Format Your Script:** Use clear speaker labels with consistent formatting:
   ```
   Host 1: Welcome everyone to our podcast! Today we're discussing AI technology.
   Host 2: That's right! It's fascinating how AI is changing everything.
   Host 1: Let's dive into the technical details...
   Host 2: I'd love to hear your thoughts on machine learning applications.
   ```
4. **Generate Audio:** Connect your script input and run the workflow
5. **Download Result:** The tool outputs an audio file ready for podcast distribution

### Advanced Configuration

- **Mixed Services:** Use OpenAI voices for one host and ElevenLabs for another to optimize cost/quality
- **Voice Characteristics:** Each voice has specific traits (age, accent, tone) - choose combinations that create natural conversations
- **Script Formatting:** Ensure consistent "Host 1:" and "Host 2:" labels for proper voice assignment
- **Workflow Integration:** Connect with other Dify tools for automated content generation pipelines

## Required APIs and Credentials

### OpenAI TTS (Option 1)
- **API Key:** Required from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Permissions:** Text-to-Speech API access
- **Pricing:** Pay-per-use based on character count (~$15/1M characters)
- **Base URL:** Optional custom endpoint support
- **Rate Limits:** 50 requests per minute (default)

### ElevenLabs (Option 2)  
- **API Key:** Required from [ElevenLabs Dashboard](https://elevenlabs.io/app/settings/api-keys)
- **Subscription:** Starter plan or higher recommended
- **Pricing:** Character-based limits vary by plan
- **Character Limits:** 10K (free) to 500K+ (paid plans) per month
- **Rate Limits:** Varies by subscription tier

## Connection Requirements and Configuration

### Network Requirements
- **Outbound HTTPS connections required to:**
  - `api.openai.com` (for OpenAI TTS service)
  - `api.elevenlabs.io` (for ElevenLabs service)
- **Ports:** 443 (HTTPS)
- **Firewall:** Ensure outbound connections are allowed
- **Proxy Support:** OpenAI base URL can be customized for proxy usage

### System Requirements
- **Memory:** 256MB minimum for plugin operation
- **CPU Architecture:** AMD64 or ARM64 supported
- **Python Runtime:** 3.12+ (managed by Dify)
- **Dify Version:** Compatible with Community Edition and Cloud Version

### Configuration Details
- **Plugin Memory Allocation:** 268MB reserved
- **Concurrent Requests:** Supports parallel processing
- **Audio Output Format:** WAV format, 22kHz sample rate
- **Maximum Script Length:** Limited by TTS service character limits

## Testing and Compatibility

✅ **Tested Environments:**
- Dify Community Edition v0.6.0+
- Dify Cloud Version (latest)
- Docker deployments
- Local development environments

✅ **Functionality Verified:**
- OpenAI TTS integration and voice generation
- ElevenLabs TTS integration and voice generation  
- Mixed service usage (different services per host)
- Error handling for invalid API keys
- Network connectivity issues handling
- Large script processing
- Audio quality and format consistency

## Troubleshooting

### Common Issues

**"Invalid API key" Error:**
- Verify your API key is correctly entered without extra spaces
- Check that the API key has proper permissions for TTS services
- Ensure you've selected the correct TTS service (OpenAI vs ElevenLabs)
- Test the API key directly with the service provider's documentation

**"Plugin verification failed" Error:**
- For local development: Disable plugin verification in Dify settings
- For production: Ensure plugin is properly signed and approved
- Check plugin installation logs for specific error details

**Audio generation fails:**
- Verify your script follows the correct format with "Host 1:" and "Host 2:" labels
- Check API key has sufficient credits/quota remaining
- Ensure network connectivity to TTS service endpoints
- Verify script length doesn't exceed service character limits

**Poor audio quality:**
- Try different voice combinations for better contrast
- Ensure script has natural conversation flow
- Check if using mixed services improves quality for your use case

### Getting Support

For technical issues, feature requests, or contributions:
- **GitHub Issues:** [Create an issue](https://github.com/gaurav0651/podcast_studio/issues)
- **Documentation:** Review this README and GUIDE.md
- **Community:** Check existing issues for similar problems

## Repository and Source Code

**Source Code Repository:** https://github.com/gaurav0651/podcast_studio

The complete source code, documentation, and examples are available in the GitHub repository. Contributors welcome!

## License

This plugin is released under the MIT License. See the [LICENSE](https://github.com/gaurav0651/podcast_studio/blob/main/LICENSE) file in the repository for full license details.

---

*This plugin complies with Dify Plugin Privacy Protection Guidelines and has been thoroughly tested for completeness and functionality on both Dify Community Edition and Cloud Version.*