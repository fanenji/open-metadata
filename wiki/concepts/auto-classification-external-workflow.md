---
type: concept
title: Auto Classification External Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, ingestion-framework, cli, python, pii, data-governance]
related: [auto-classification, auto-classification-workflow, metadata-classify-command, pii-processor, orm-profiler, metadata-cli, ingestion-framework, agent-based-ingestion, confidence-parameter, use-fqn-for-filtering]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# Auto Classification External Workflow

The External Auto Classification Workflow refers to the programmatic and CLI-based execution paths for running auto-classification of sensitive data, as distinct from the UI-based agent configuration. It provides two primary execution methods:

1. **Python Programmatic**: Using the [[auto-classification-workflow|AutoClassificationWorkflow]] class directly in Python code.
2. **CLI-based**: Using the `metadata classify` command with a YAML configuration file.

Both methods serve as alternatives to the UI-based Auto Classification Agent documented in [[auto-classification]] and [[adding-auto-classification-workflow-through-ui---o-20260514]].

## Execution Methods

### Python Programmatic Execution

```python
from openmetadata.ingestion.workflow import AutoClassificationWorkflow

# Configuration dictionary equivalent to YAML structure
config = { ... }
workflow = AutoClassificationWorkflow.create(config)
workflow.execute()
workflow.stop()
```

This method is suitable for automation scripts, CI/CD pipelines, and programmatic orchestration where generating and managing YAML files is undesirable.

### CLI Execution

```bash
metadata classify -c <path-to-yaml>
```

This method mirrors the familiar `metadata ingest` workflow but uses the dedicated `classify` subcommand. See [[metadata-classify-command]] for details.

## Prerequisites

1. **Prior Metadata Ingestion**: The target service must have been ingested first, as the classification workflow reuses the `serviceName` to retrieve connection details from the OpenMetadata server.
2. **PII Processor Installation**: The `openmetadata-ingestion[pii-processor]` extra must be installed (see [[pii-processor]]).
3. **Valid JWT Token**: Authentication requires a valid JWT token in the `securityConfig` section, same as other CLI-based workflows (see [[cli-ingestion-with-basic-auth]]).

## Configuration Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `enableAutoClassification` | Boolean | `false` | Enables automatic detection and tagging of sensitive columns |
| `confidence` | Number (0–100) | `80` | Confidence threshold for tagging; higher = fewer false positives, lower = more detections |
| `storeSampleData` | Boolean | `true` | Whether to store sample rows during ingestion |
| `sampleDataCount` | Integer | `50` | Number of sample rows to fetch per table |
| `useFqnForFiltering` | Boolean | `false` | Apply filter patterns to Fully Qualified Names instead of raw names |
| `includeViews` | Boolean | `true` | Include or exclude views during processing |

### Confidence Parameter

The [[confidence-parameter|confidence]] parameter (0–100) controls the precision-recall trade-off:
- **Higher values (e.g., 90)**: Stricter detection, fewer false positives, may miss some sensitive data.
- **Lower values (e.g., 70)**: More aggressive detection, catches more sensitive columns, may produce false positives.

### useFqnForFiltering

When `true`, filter patterns match against Fully Qualified Names (`service_name.db_name.schema_name.table_name`). When `false`, patterns match against raw table names only. See [[use-fqn-for-filtering]].

## Processor

The external workflow uses the [[orm-profiler|orm-profiler]] processor — the same profiling engine used for general [[data-profiling]]. It samples data from configured tables and applies PII detection patterns from the [[pii-processor]] module.

## Relationship to UI Agent

Both the external workflow and the UI-based agent ([[auto-classification]]) achieve the same outcome: automatic detection and tagging of sensitive columns. The key differences are:

| Aspect | External Workflow | UI Agent |
|--------|-------------------|----------|
| Invocation | Python code or CLI command | Scheduled agent via UI |
| Configuration | YAML file or Python dict | UI form fields |
| Scheduling | External (cron, Argo, CI/CD) | Built-in scheduler |
| Use Case | Automation, CI/CD, programmatic control | Manual setup, ad-hoc runs |