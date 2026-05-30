---
type: entity
title: External Profiler Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, profiler, workflow]
related: [data-profiling, metadata-cli, personal-access-token, sample-data-external-storage, sample-data-storage-toggle, snowflake]
sources: ["external-profiler-workflow-official-documentation--20260514.md"]
---

# External Profiler Workflow

The External Profiler Workflow is a feature in OpenMetadata (v1.2.1+) that allows running a single profiler workflow for an entire data source, irrespective of which OpenMetadata service the assets belong to. This is useful when a large database source with multiple databases and schemas is maintained by different teams, and multiple database services have been created with different filters.

## Key Differentiator

Unlike a standard profiler workflow, the External Profiler Workflow YAML configuration does **not** include a Service Name. This enables cross-service profiling.

## Critical Limitation

Running a single profiler workflow is **only supported externally** — it cannot be configured or run from the OpenMetadata UI.

## Requirements

Install the required packages:

```bash
pip install "openmetadata-ingestion[<connector>,datalake,trino]~=1.2.1"
```

Where `<connector>` is the name of the connector (e.g., `snowflake`, `athena`). The `datalake` plugin enables S3 sample data management. The `trino` plugin is noted as "only needed temporarily."

## YAML Configuration Structure

The YAML config has the following sections:

- **source**: Defines the source type and connection details (no Service Name).
- **sourceConfig**: Profiler configuration (`type: Profiler`, `generateSampleData`, `computeMetrics`, filter patterns).
- **processor**: Type `orm-profiler` with optional `tableConfig`, `schemaConfig`, and `databaseConfig` blocks for granular control.
- **sink**: Typically `type: metadata-rest`.
- **workflowConfig**: OpenMetadata server connection and JWT token authentication.

### Granular Configuration Levels

- **tableConfig**: Per-table settings (e.g., `sampleDataCount`).
- **schemaConfig**: Per-schema settings (`sampleDataCount`, `profileSample`, `profileSampleType`, `sampleDataStorageConfig`).
- **databaseConfig**: Per-database settings (same options as schemaConfig).

## Execution Methods

### CLI

```bash
metadata profile -c <path-to-yaml>
```

### Python SDK

```python
from metadata.workflow.profiler import ProfilerWorkflow
from metadata.workflow.workflow_output_handler import print_status

CONFIG = """
# YAML configuration here
"""

workflow_config = yaml.safe_load(CONFIG)
workflow = ProfilerWorkflow.create(workflow_config)
workflow.execute()
workflow.raise_from_status()
print_status(workflow)
workflow.stop()
```

## Related Pages

- [[data-profiling]] — Core profiling concept; the external workflow is a distinct pattern.
- [[metadata-cli]] — CLI tool; the `metadata profile -c` command is a variant of CLI ingestion.
- [[personal-access-token]] — JWT token authentication used in the workflow config.
- [[sample-data-external-storage]] — External sample data storage configuration.
- [[sample-data-storage-toggle]] — The `generateSampleData` toggle in the config.