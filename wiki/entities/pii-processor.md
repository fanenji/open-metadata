---
type: entity
title: pii-processor
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, ingestion-framework, pii, python, dependencies]
related: [auto-classification, auto-classification-external-workflow, orm-profiler, ingestion-framework]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# pii-processor

The `pii-processor` is a Python package extra for the OpenMetadata ingestion framework that provides PII (Personally Identifiable Information) detection capabilities. It is required for running Auto Classification workflows.

## Installation

```bash
pip install "openmetadata-ingestion[pii-processor]"
```

The base `openmetadata-ingestion` package does not include PII detection modules. Attempting to run an Auto Classification workflow without this extra will result in missing dependency errors.

## Capabilities

- Pattern recognition for common PII types (names, emails, SSNs, credit card numbers, etc.)
- Confidence scoring for detected sensitive columns
- Integration with the [[orm-profiler|orm-profiler]] processor for data sampling and analysis
- Automatic tagging of sensitive columns based on predefined criteria and configurable confidence thresholds

## Relationship to Auto Classification

The `pii-processor` extra is the engine that powers the detection logic within the Auto Classification workflow. When `enableAutoClassification: true` is set in the workflow configuration, the [[orm-profiler|orm-profiler]] processor invokes the PII detection modules from this package to analyze sample data and identify sensitive columns.