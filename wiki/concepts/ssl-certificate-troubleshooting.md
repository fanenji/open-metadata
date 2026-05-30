---
type: concept
title: SSL Certificate Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [troubleshooting, ssl, auto-classification, ingestion, windows]
related: [auto-pii-tagging, entity-recognition-engine, auto-classification, ingestion-pipeline-troubleshooting]
sources: ["auto-pii-tagging-guide-official-documentation---op-20260514.md"]
---
# SSL Certificate Troubleshooting

This page documents a known SSL certificate verification issue affecting the [[auto-pii-tagging]] workflow on corporate Windows laptops, along with the recommended workaround.

## Symptom

When the Auto PII Tagging workflow attempts to download the spaCy Entity Recognition model, the following error occurs:

```
Unexpected error while processing sample data for auto pii tagging -
HTTPSConnectionPool(host='raw.githubusercontent.com', port=443):
Max retries exceeded with url: /explosion/spacy-models/master/compatibility.json
(Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
```

## Root Cause

This issue has been identified on some **corporate Windows laptops** where the system's certificate trust store does not include the certificate chain required to verify `raw.githubusercontent.com`. The profiler (running as part of the ingestion pipeline) attempts to download the [[entity-recognition-engine|Entity Recognition]] model's compatibility manifest and encounters a certificate verification failure.

## Workaround

Manually install the spaCy model on the ingestion container or Airflow host using `pip` with the `--trusted-host` flag to bypass certificate verification for the download:

```bash
pip --trusted-host github.com --trusted-host objects.githubusercontent.com install \
  https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.5.0/en_core_web_md-3.5.0.tar.gz
```

### Docker Deployment
If using Docker, customize the `openmetadata-ingestion` image to run this command at build time so the model is pre-installed in the container image.

## Caveats

- **Not a production-grade solution**: The `--trusted-host` flag bypasses certificate validation, which is a security risk in production environments
- **Requires custom image builds**: The workaround necessitates maintaining a custom Docker image rather than using the official image directly
- **Model version pinning**: The workaround installs a specific model version (3.5.0); future OpenMetadata versions may require a different model version

## Related Troubleshooting

For general ingestion pipeline issues, see [[ingestion-pipeline-troubleshooting]].