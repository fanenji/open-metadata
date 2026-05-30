---
type: entity
title: AutoClassificationWorkflow
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, ingestion-framework, python, pii]
related: [auto-classification, auto-classification-external-workflow, pii-processor, ingestion-framework, orm-profiler]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# AutoClassificationWorkflow

The `AutoClassificationWorkflow` is a Python class in the OpenMetadata ingestion framework that provides programmatic execution of auto-classification tasks. It serves as the entry point for running classification workflows directly from Python code, bypassing the need for YAML configuration files and CLI commands.

## Purpose

This class enables developers and automation scripts to trigger auto-classification of sensitive data (PII detection and tagging) without going through the UI-based agent configuration or the `metadata classify` CLI command. It accepts a configuration dictionary (equivalent to the YAML structure) and executes the classification pipeline using the [[orm-profiler|orm-profiler]] processor.

## Relationship to Other Execution Methods

- **UI Agent**: Configured via Settings → Applications → Auto Classification Agent (see [[auto-classification]]).
- **CLI**: Executed via `metadata classify -c <path-to-yaml>` (see [[metadata-classify-command]]).
- **Programmatic**: Direct instantiation of `AutoClassificationWorkflow` in Python code.

All three methods share the same underlying processor and configuration parameters, differing only in the invocation mechanism.

## Dependencies

Requires the `openmetadata-ingestion[pii-processor]` package extra to be installed:

```bash
pip install "openmetadata-ingestion[pii-processor]"
```

The standard `openmetadata-ingestion` package does not include the PII detection capabilities needed for auto-classification.