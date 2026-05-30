---
type: concept
title: External Profiler Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, profiler, workflow, external]
related: [external-profiler-workflow, data-profiling, metadata-cli, personal-access-token, sample-data-external-storage, sample-data-storage-toggle, pull-based-ingestion-model]
sources: ["external-profiler-workflow-official-documentation--20260514.md"]
---

# External Profiler Workflow

The External Profiler Workflow is a profiling pattern in OpenMetadata that enables running a single profiler workflow for an entire data source, even when that source's assets are distributed across multiple OpenMetadata services. This is a distinct pattern from the standard (internal) profiler workflow, which requires one pipeline per service.

## Core Principle

The key architectural difference is the **absence of a Service Name** in the YAML configuration. Standard profiler workflows require a Service Name to identify which service's assets to profile. The external workflow omits this, allowing it to discover and profile all assets from the underlying source regardless of which OpenMetadata service they belong to.

## Use Case

Large database sources with multiple databases and schemas maintained by different teams. For example, a Snowflake instance with multiple databases where each database is managed by a separate team, and multiple OpenMetadata services have been created with different filter patterns. Instead of running a profiler pipeline per service, a single external workflow profiles the entire source.

## Relationship to Pull-Based Ingestion

The External Profiler Workflow is an example of the [[pull-based-ingestion-model]] — the workflow actively pulls metadata (profiling data) from the source on demand. However, unlike standard pull-based ingestion, this workflow is executed externally rather than being scheduled from within OpenMetadata.

## Granular Control

The workflow supports three levels of granular configuration:

1. **tableConfig**: Per-table settings (e.g., `sampleDataCount`)
2. **schemaConfig**: Per-schema settings (sample data count, profile sample, storage config)
3. **databaseConfig**: Per-database settings (same options as schemaConfig)

This allows fine-grained control over profiling behavior at different levels of the source hierarchy.

## Limitations and Caveats

- **External-only**: Cannot be configured or run from the OpenMetadata UI.
- **Version requirement**: Requires OpenMetadata 1.2.1 or higher.
- **Temporary dependency**: The `trino` plugin is noted as "only needed temporarily" — the reason for this is not documented.
- **No troubleshooting guidance**: The official documentation does not cover edge cases or failure modes.

## Open Questions

- How does the external profiler handle conflicts when the same table appears in multiple services?
- What happens to profiling results if the service mapping changes after the workflow runs?
- Are there performance or resource considerations for running a single workflow against a very large source?
- Why is the trino plugin only needed temporarily? Is there a migration path away from it?