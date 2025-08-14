# Privacy Policy - Podcast Studio Plugin

**Effective Date:** January 15, 2025  
**Plugin:** Podcast Studio v1.0.0  
**Author:** gaurav0651  
**Repository:** https://github.com/gaurav0651/podcast_studio

## Data Collection

### What Data We Collect

This plugin processes the following data to provide text-to-speech services:

1. **Text Content:** 
   - Podcast scripts provided by users through Dify workflows
   - Speaker labels and dialogue text for voice assignment
   - Content is used solely for audio generation purposes
   - No persistent storage of script content

2. **Configuration Data:**
   - Selected voice preferences for Host 1 and Host 2
   - TTS service selection (OpenAI vs ElevenLabs)
   - API endpoint configurations and custom base URLs
   - Voice parameter settings

3. **Operational Data:**
   - API request logs for debugging purposes (temporary)
   - Error messages and status codes (temporary)
   - Processing time metrics (temporary)

### What Data We Don't Collect

- Personal identification information of users
- User account details or authentication data
- Generated audio files (not stored permanently)
- Usage analytics, tracking cookies, or behavioral data
- IP addresses or location information
- Billing or payment information

## Data Processing

### Third-Party Services

This plugin transmits text data to external TTS services for voice synthesis:

**OpenAI Text-to-Speech API:**
- Text content is sent to OpenAI's TTS API endpoints for voice generation
- Data processing occurs on OpenAI's secure servers
- Subject to [OpenAI's Privacy Policy](https://openai.com/privacy/)
- OpenAI's data retention policies apply to transmitted content

**ElevenLabs Voice Synthesis API:**
- Text content is sent to ElevenLabs API for voice generation  
- Data processing occurs on ElevenLabs' secure infrastructure
- Subject to [ElevenLabs Privacy Policy](https://elevenlabs.io/privacy)
- ElevenLabs' data handling practices apply to transmitted content

### Data Transmission Security
- All API communications use TLS 1.2+ encryption (HTTPS)
- API keys are transmitted securely and stored in Dify's encrypted credential system
- No sensitive data is logged in plain text format
- Network connections are validated for certificate authenticity

### Data Retention

- **Plugin Level:** No user data is permanently stored by this plugin
- **Memory Processing:** Text content is processed in memory and discarded after audio generation
- **Third-Party Services:** Data retention governed by each service's privacy policy:
  - OpenAI: Refer to their current data retention policy
  - ElevenLabs: Refer to their current data retention policy
- **Temporary Logs:** Error logs are automatically purged after 24 hours

## Data Security

### Security Measures
- **Encryption in Transit:** All API communications encrypted with HTTPS/TLS
- **Credential Management:** API keys stored using Dify's secure credential system
- **Access Control:** Only authorized workflow executions can access plugin functionality
- **No Local Storage:** No persistent data storage on plugin infrastructure
- **Memory Protection:** Sensitive data cleared from memory after processing

### Access Control
- Plugin access controlled through Dify's user permission system
- API credentials managed through Dify's encrypted credential storage
- No direct database access or file system persistence
- Audit trail through Dify's workflow execution logs

## User Rights and Control

### Data Control Rights
- **Content Control:** Users have complete control over text content sent for processing
- **Service Selection:** Users choose which TTS service processes their data
- **API Management:** Users control their own API keys and can revoke access at any time
- **Processing Transparency:** All data processing is documented and visible in workflow logs

### Data Subject Rights
- **Right to Information:** This privacy policy provides complete transparency about data handling
- **Right to Control:** Users control what content is processed and when
- **Right to Deletion:** No persistent data means no data retention to delete
- **Right to Portability:** Generated audio files can be downloaded and used freely

## Compliance and Standards

### Regulatory Compliance
This plugin is designed to comply with:
- **Dify Plugin Privacy Protection Guidelines** (full compliance)
- **GDPR principles** for data protection and user rights
- **CCPA requirements** for data transparency and user control
- **General data protection best practices**

### Third-Party Compliance
- OpenAI and ElevenLabs maintain their own compliance certifications
- Users should review third-party service privacy policies
- Plugin acts as a data processor, not a data controller

## Privacy by Design

### Built-in Privacy Features
- **Minimal Data Collection:** Only necessary data for functionality is processed
- **No Persistent Storage:** Data is processed and immediately discarded
- **User Control:** Users have complete control over what data is processed
- **Transparency:** All data flows are documented and visible
- **Security First:** Encryption and secure practices are mandatory

## Contact and Updates

### Privacy Questions
For privacy-related questions or concerns:
- **Repository Issues:** [GitHub Issues](https://github.com/gaurav0651/podcast_studio/issues)
- **Email:** Contact through GitHub repository
- **Documentation:** Refer to this privacy policy and plugin documentation

### Policy Updates
This privacy policy may be updated to reflect:
- Changes in plugin functionality or data handling
- Updates to third-party service privacy policies
- New regulatory requirements or best practices
- User feedback and privacy improvements

**Notification Method:** Users will be notified of significant privacy policy changes through:
- Plugin version updates with changelog
- Repository announcements and releases
- Updated documentation in plugin packages

---

**Compliance Statement:** This privacy policy has been prepared in accordance with the Dify Plugin Privacy Protection Guidelines and represents our commitment to protecting user privacy while providing valuable podcast generation functionality.

**Last Updated:** January 15, 2025
**Policy Version:** 1.0.0