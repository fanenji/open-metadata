---
type: entity
title: Presidio
created: 2026-05-07
updated: 2026-05-07
tags: [pii, data-governance, anonymization, open-source, microsoft]
related: [microsoft, presidio-analyzer, presidio-anonymizer, presidio-image-redactor, presidio-structured, data-masking-techniques, data-pseudonymization, automated-data-discovery-and-classification]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# Presidio

Presidio is an open-source framework developed and maintained by [[Microsoft]] for detecting, redacting, masking, and anonymizing personally identifiable information (PII) across text, images, and structured data. The name derives from the Latin *praesidium*, meaning "protection" or "garrison."

## Architecture

Presidio is composed of four core modules:

- **[[Presidio Analyzer]]** — Identifies PII in text using Named Entity Recognition (NER), regular expressions, rule-based logic, and checksum validation. Supports custom recognizers and integration with external detection models.
- **[[Presidio Anonymizer]]** — Redacts, masks, or transforms detected PII entities based on configurable operators.
- **[[Presidio Image-Redactor]]** — Detects and redacts PII in images, including standard image formats and DICOM medical images.
- **[[Presidio Structured]]** — Handles PII detection and anonymization in structured/tabular data.

## Key Capabilities

- Predefined recognizers for common PII types (credit card numbers, names, locations, SSNs, bitcoin wallets, US phone numbers, financial data)
- Custom PII recognizers for domain-specific needs
- Context-aware detection across multiple languages
- Multiple deployment options: Python, PySpark, Docker, and Kubernetes
- Extensible and customizable pipelines

## Limitations

Presidio uses automated detection mechanisms and **cannot guarantee** finding all sensitive information. It is intended as a component within a broader data protection strategy, not a standalone solution.

## Relevance to the Data Platform

Presidio provides a practical, open-source tool for implementing [[data-masking-techniques]] and [[data-pseudonymization]] strategies. It supports [[automated-data-discovery-and-classification]] workflows and is suitable for organizations at higher maturity levels in the [[data-maturity-model-for-sensitive-data]].