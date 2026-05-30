---
type: entity
title: metadata classify command
created: 2026-05-14
updated: 2026-05-14
tags: [cli, auto-classification, ingestion-framework, metadata-cli]
related: [metadata-cli, auto-classification, auto-classification-external-workflow, cli-ingestion-with-basic-auth]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# metadata classify command

`metadata classify` is a CLI subcommand of the [[metadata-cli|metadata CLI]] specifically for executing Auto Classification workflows. It is distinct from the `metadata ingest` command used for general metadata ingestion.

## Usage

```bash
metadata classify -c <path-to-yaml>
```

## Distinction from `metadata ingest`

| Command | Purpose |
|---------|---------|
| `metadata ingest` | Runs metadata ingestion pipelines (schema extraction, lineage, profiling, etc.) |
| `metadata classify` | Runs Auto Classification workflows (PII detection and tagging) |

Both commands accept a YAML configuration file via the `-c` flag and share the same authentication mechanism (JWT token in `securityConfig`). However, `metadata classify` is specialized for the classification workflow type (`type: AutoClassification`) and uses the [[orm-profiler|orm-profiler]] processor.

## Prerequisites

1. Prior metadata ingestion must have been completed for the target service, as the classification workflow reuses the `serviceName` to retrieve connection details from the OpenMetadata server.
2. The `openmetadata-ingestion[pii-processor]` package extra must be installed.