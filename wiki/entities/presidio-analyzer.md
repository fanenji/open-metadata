---
type: entity
title: Presidio Analyzer
created: 2026-05-07
updated: 2026-05-07
tags: [pii, nlp, regex, detection]
related: [presidio, presidio-anonymizer, named-entity-recognition]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# Presidio Analyzer

The Presidio Analyzer is the core detection module of the [[Presidio]] framework. It identifies PII in text using a combination of techniques:

- **Named Entity Recognition (NER)** — Context-aware detection using NLP models
- **Regular Expressions** — Pattern-based matching for structured PII (e.g., credit card numbers, SSNs)
- **Rule-based Logic** — Heuristic rules for specific entity types
- **Checksum Validation** — Verification algorithms (e.g., Luhn for credit cards)

The Analyzer supports predefined recognizers for common PII types and allows users to define custom recognizers for domain-specific needs. It can also integrate with external PII detection models.