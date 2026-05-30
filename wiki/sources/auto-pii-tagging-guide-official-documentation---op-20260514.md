---
type: source
title: "Auto PII Tagging Guide | Official Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, pii, data-governance, classification-tags]
related: [auto-pii-tagging, entity-recognition-engine, column-name-scanner, auto-classification, pii-sample-data-masking, sample-data-storage-toggle, ssl-certificate-troubleshooting]
sources: ["auto-pii-tagging-guide-official-documentation---op-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/auto-pii-tagging"
venue: "OpenMetadata Documentation v1.12.x"
---
# Auto PII Tagging Guide | Official Documentation

Official documentation for the Auto PII Tagging workflow in OpenMetadata v1.12.x. Covers the dual detection approach (Column Name Scanner + Entity Recognition), the confidence parameter for tuning sensitivity, the idempotency rule for already-tagged columns, the enterprise vs. open-source feature gap for General Classification tags, and troubleshooting the SSL certificate verification issue on corporate Windows laptops.

## Key Points

- **Dual Detection**: Column Name Scanner (regex-based) and Entity Recognition (NLP-based via spaCy `en_core_web_md` model)
- **Confidence Parameter**: Tunable threshold for minimum score required to tag a column as `PII.Sensitive`
- **Idempotency**: Columns already tagged as PII are skipped during execution
- **Feature Gap**: General Classification tags (Address, Name, etc.) are not available in open-source; expected from v1.7.1
- **SSL Issue**: Corporate Windows laptops may encounter `CERTIFICATE_VERIFY_FAILED` when downloading the NLP model; workaround is manual `pip install` with `--trusted-host`