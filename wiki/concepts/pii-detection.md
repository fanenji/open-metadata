---
type: concept
title: PII Detection
created: 2026-05-07
updated: 2026-05-07
tags: [pii, data-governance, privacy, detection]
related: [presidio, data-masking-techniques, data-pseudonymization, automated-data-discovery-and-classification, named-entity-recognition]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# PII Detection

PII (Personally Identifiable Information) Detection is the automated identification of sensitive data such as credit card numbers, names, locations, social security numbers, and financial information within text, images, and structured data. The [[Presidio]] framework implements PII detection using a combination of techniques:

- **Named Entity Recognition (NER)** — Context-aware NLP models that identify entities based on their semantic meaning
- **Regular Expressions** — Pattern matching for structured PII with known formats
- **Rule-based Logic** — Heuristic rules for domain-specific entity types
- **Checksum Validation** — Verification algorithms (e.g., Luhn algorithm for credit cards)

PII detection is a critical component of [[data-masking-techniques]] and [[data-pseudonymization]] workflows, enabling [[automated-data-discovery-and-classification]] at scale. It is a foundational capability for implementing [[data-maturity-model-for-sensitive-data]] strategies.