---
type: concept
title: Named Entity Recognition
created: 2026-05-07
updated: 2026-05-07
tags: [nlp, pii, detection, machine-learning]
related: [presidio, pii-detection, presidio-analyzer]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# Named Entity Recognition

Named Entity Recognition (NER) is a natural language processing (NLP) technique used to identify and classify named entities in text into predefined categories such as person names, organizations, locations, medical codes, and financial identifiers. In the context of the [[Presidio]] framework, NER is a key technique used by the [[Presidio Analyzer]] for context-aware PII detection.

NER enables Presidio to detect sensitive information that does not follow a fixed pattern (e.g., names, addresses) by understanding the semantic context of the text. This complements regex-based and rule-based approaches for structured PII types.