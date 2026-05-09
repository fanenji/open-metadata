---
type: entity
title: Presidio Image-Redactor
created: 2026-05-07
updated: 2026-05-07
tags: [pii, image-redaction, dicom, medical-imaging]
related: [presidio, presidio-analyzer, presidio-anonymizer]
sources: ["Microsoft Presidio An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines..md"]
---
# Presidio Image-Redactor

The Presidio Image-Redactor is a module of the [[Presidio]] framework that detects and redacts PII in images. It supports:

- Standard image formats (PNG, JPEG, etc.)
- DICOM medical images

The Image-Redactor uses OCR and other computer vision techniques to identify text within images and applies redaction to protect sensitive information.