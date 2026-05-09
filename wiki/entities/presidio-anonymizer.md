---
type: entity
title: Presidio Anonymizer
created: 2026-05-07
updated: 2026-05-07
tags: [pii, anonymization, redaction, masking]
related: [presidio, presidio-analyzer, data-masking-techniques, data-pseudonymization]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# Presidio Anonymizer

The Presidio Anonymizer is the de-identification module of the [[Presidio]] framework. It processes the entities detected by the [[Presidio Analyzer]] and applies configurable anonymization operators, including:

- **Redaction** — Removing PII entirely
- **Masking** — Replacing PII with placeholder characters
- **Replacement** — Substituting PII with predefined values or entity types
- **Encryption** — Applying cryptographic transformations

The Anonymizer supports custom operators, allowing organizations to define their own anonymization strategies.