---
type: source
title: External Profiler Workflow | Official Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, external-workflow, profiler]
related: [external-profiler-workflow, data-profiling, metadata-cli, personal-access-token, sample-data-external-storage, sample-data-storage-toggle]
sources: ["external-profiler-workflow-official-documentation--20260514.md"]
---

# External Profiler Workflow | Official Documentation

This source is the official OpenMetadata documentation page for the External Profiler Workflow (v1.12.x). It describes how to run a single profiler workflow for an entire data source, even when that source's assets are split across multiple OpenMetadata services. The document covers requirements, YAML configuration structure, and two execution methods (CLI and Python SDK).

**Key points from the source:**
- Requires OpenMetadata 1.2.1 or higher.
- The YAML config does **not** include a Service Name, unlike typical profiler workflows.
- The workflow is only supported when run externally (not from the OpenMetadata UI).
- The processor type is `orm-profiler`.
- Supports granular configuration at the table, schema, and database levels.
- Execution via CLI (`metadata profile -c <path-to-yaml>`) or Python SDK (`ProfilerWorkflow.create()`).
- Requires `openmetadata-ingestion[<connector>,datalake,trino]~=1.2.1` packages.
- The trino plugin is noted as "only needed temporarily."

**Use case:** Large database sources with multiple databases/schemas maintained by different teams, where multiple services have been created with different filters.