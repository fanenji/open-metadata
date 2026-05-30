---
type: concept
title: Auto PII Tagging
created: 2026-05-14
updated: 2026-05-14
tags: ["data-governance", "classification", "pii", "nlp", "profiling", "auto-classification", "classification-tags", "entity-recognition"]
related: ["auto-classification", "nlp-based-profiler-classification", "classification-tags", "pii-sample-data-masking", "data-profiling", "entity-recognition-engine", "column-name-scanner", "sample-data-storage-toggle", "system-classification", "ssl-certificate-troubleshooting", "agent-based-ingestion"]
sources: ["auto-classification-in-openmetadata---openmetadata-20260514.md", "auto-pii-tagging-guide-official-documentation---op-20260514.md"]
---
# Auto PII Tagging

Auto PII Tagging is a specific sub-workflow within the broader [[auto-classification]] system that automatically identifies and tags columns containing Personally Identifiable Information (PII). It classifies columns as either `PII.Sensitive` or `PII.NonSensitive` using two complementary detection methods.

## Dual Detection Approach

### Column Name Scanner
A regex-based scanner that validates column names against a set of patterns designed to identify common English patterns for sensitive data types:
- Email addresses
- Social Security Numbers (SSN)
- Bank account numbers
- Other common PII-bearing column name patterns

This method operates on schema metadata alone and does not require sample data access.

### Entity Recognition
An NLP-based engine that scans actual sample data rows for sensitive information using a trained model. This method is **only active when sample data ingestion is enabled** (see [[sample-data-storage-toggle]]). The engine uses the spaCy `en_core_web_md` model (see [[entity-recognition-engine]]) to detect a list of supported sensitive entities within the data content.

## Confidence Parameter

The `confidence` parameter allows users to tune the sensitivity threshold for entity recognition tagging. It controls the minimum score required for the NLP engine to tag a column as `PII.Sensitive`. Higher values require stronger evidence, reducing false positives but potentially missing borderline cases. Lower values increase recall at the cost of precision.

## Idempotency Rule

If a column is **already tagged as PII** (either `PII.Sensitive` or `PII.NonSensitive`), the auto-classification workflow **skips that column** during execution. This idempotency guarantee ensures that manual classifications are preserved and not overwritten by automated runs.

## Feature Gap: General Classification

The General Classification tags (such as `Address`, `Name`, `Date of Birth`, etc.) are **not available in the open-source version** of OpenMetadata. They exist only in the enterprise edition and are expected to be included in the open-source release starting from version 1.7.1. Users should be aware that the auto-classification workflow in open-source is limited to PII classification (`Sensitive` / `NonSensitive`) only.

## Relationship to Other Systems

- **Upstream dependency**: Requires the [[auto-classification]] agent to be configured and scheduled (see [[agent-based-ingestion]])
- **Data dependency**: Entity recognition requires [[sample-data-storage-toggle|sample data ingestion]] to be enabled
- **Downstream effect**: Tagged columns become subject to [[pii-sample-data-masking]] in the UI
- **Tag source**: Applies tags from the [[system-classification]] set (`PII.Sensitive`, `PII.NonSensitive`)

## Troubleshooting

See [[ssl-certificate-troubleshooting]] for the known SSL certificate verification issue on corporate Windows laptops that prevents the Entity Recognition model from downloading.