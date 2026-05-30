---
type: source
title: "External Auto Classification Workflow - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, ingestion-framework, cli, pii, data-governance]
related: [auto-classification, auto-classification-external-workflow, metadata-classify-command, pii-processor, metadata-cli, ingestion-framework, agent-based-ingestion]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/external-workflow"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# External Auto Classification Workflow - OpenMetadata Documentation

Official documentation for executing Auto Classification workflows externally — via Python code using the `AutoClassificationWorkflow` class or via the `metadata classify` CLI command — as an alternative to the UI-based agent configuration.

The source covers:
- **Pipeline Configuration Parameters**: `enableAutoClassification`, `confidence` (0–100), `storeSampleData`, `useFqnForFiltering`, and filter patterns.
- **Python Workflow Execution**: Installing the `openmetadata-ingestion[pii-processor]` extra, defining a YAML config, and running programmatically.
- **CLI Execution**: Using `metadata classify -c <path-to-yaml>` as a distinct command from `metadata ingest`.
- **Workflow Execution via Pipeline**: Creating a pipeline with the Auto Classification JSON configuration and triggering it through OpenMetadata or an external scheduler like Argo.

Key findings:
- The `orm-profiler` processor is used for Auto Classification, profiling data to detect sensitive columns.
- The `pii-processor` extra is a required dependency not included in the base `openmetadata-ingestion` package.
- The `confidence` parameter provides a tunable precision-recall trade-off for PII detection.
- Auto Classification requires prior metadata ingestion; it reuses the same `serviceName` to retrieve connection details from the server.