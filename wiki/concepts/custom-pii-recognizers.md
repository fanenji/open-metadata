---
type: concept
title: Custom PII Recognizers
created: 2026-05-07
updated: 2026-05-07
tags: [pii, extensibility, customization, detection]
related: [presidio, presidio-analyzer, pii-detection]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# Custom PII Recognizers

Custom PII Recognizers are an extensibility mechanism in the [[Presidio]] framework that allows organizations to define their own detection patterns for domain-specific PII types. The [[Presidio Analyzer]] supports custom recognizers that can be implemented using:

- Custom regular expressions
- Rule-based logic
- Integration with external detection models or APIs

This capability enables Presidio to be adapted to specific business needs, regulatory requirements, or industry-specific data types that are not covered by the predefined recognizers.