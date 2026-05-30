---
type: concept
title: NLP-Based Profiler Classification
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, nlp, profiling, ingestion]
related: [auto-classification, auto-pii-tagging, data-profiling, ingestion-framework]
sources: ["auto-classification-in-openmetadata---openmetadata-20260514.md"]
---
# NLP-Based Profiler Classification

NLP-Based Profiler Classification is the technical mechanism underlying OpenMetadata's [[auto-classification]] and [[auto-pii-tagging]] capabilities. It refers to the use of Natural Language Processing (NLP) techniques during the [[data-profiling|data profiling]] step of the [[ingestion-framework|metadata ingestion pipeline]] to analyze column names and sample data for sensitive content detection.

## Technical Context

The NLP engine operates within the profiler component of the ingestion pipeline. During profiling, the system:

1. Extracts column metadata (names, data types, descriptions).
2. Retrieves sample data rows from the source table.
3. Applies NLP models to classify columns and data as potentially sensitive.
4. Assigns or suggests appropriate [[classification-tags]] based on detection results.

## Detection Scope

The NLP analysis covers:

- **Column name semantics**: Understanding that names like `last_name`, `SSN`, or `email_address` indicate PII.
- **Data pattern recognition**: Identifying PII patterns in sample data (e.g., email formats, social security number patterns, phone number formats) even when column names are non-descriptive.
- **Contextual inference**: Recognizing that certain data patterns are sensitive regardless of naming conventions.

## Relationship to Profiling

This feature is not independent — it is a capability extension of the data profiler. Key implications:

- **Profiler dependency**: If profiling is disabled or not configured, NLP-based classification does not run.
- **Sample data dependency**: Detection quality depends on the availability and quality of sample data from the source.
- **Pipeline integration**: Classification happens during ingestion, not as a separate post-hoc process. Re-classification requires re-running ingestion with profiling enabled.

## Limitations and Unknowns

- The specific NLP models or techniques used are not documented.
- No configuration parameters for sensitivity thresholds, custom patterns, or model selection are described.
- Detection accuracy metrics (precision, recall) are not provided.
- The feature's behavior with non-English column names or data is not addressed.