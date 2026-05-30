---
type: concept
title: External Ingestion Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [ingestion, yaml, cli, orchestration, metadata-ingestion]
related: [metadata-cli, pull-based-ingestion-model, metadata-ingestion-workflow, cli-ingestion-with-basic-auth, postgresql-connector, data-quality, data-profiling, auto-classification]
sources: ["run-the-postgresql-connector-externally---openmeta-20260514.md"]
---
# External Ingestion Workflow

The External Ingestion Workflow is a method for running OpenMetadata ingestion pipelines outside the OpenMetadata UI using YAML configuration files and CLI commands. This approach provides flexibility for custom orchestration, allowing users to manage workflows on their preferred orchestrator (e.g., Airflow, Kubernetes, cron jobs) instead of relying on the built-in UI-based scheduler.

## Workflow Types

The external ingestion framework supports six distinct workflow types, each with its own YAML configuration and CLI command:

1. **Metadata Ingestion** (`metadata ingest`): Extracts database metadata (tables, views, schemas, stored procedures) from the source system.
2. **Query Usage** (`metadata usage`): Extracts query history from the source system to understand data usage patterns.
3. **Lineage** (`metadata ingest` with `DatabaseLineage` type): Extracts data lineage from query history, including view lineage, query lineage, and stored procedure lineage.
4. **Data Profiler** (`metadata profile`): Computes data profile metrics (row counts, column statistics) using the `orm-profiler` processor.
5. **Auto Classification** (`metadata classify`): Automatically tags columns with PII classifications using the `orm-profiler` processor.
6. **Data Quality** (`metadata test`): Executes test cases defined in YAML or via the UI.

## YAML Configuration Structure

All external ingestion workflows follow a common YAML structure:

- **source**: Defines the source type, service name, connection details, and source configuration.
- **processor**: Defines the processing logic (e.g., `orm-profiler`, `query-parser`, `orm-test-runner`).
- **sink**: Defines where to send the metadata (typically `metadata-rest` for the OpenMetadata server).
- **workflowConfig**: Defines the OpenMetadata server connection, authentication, and logging configuration.

## Key Toggles

- **`overrideMetadata`**: Controls whether fetched metadata (description, tags, owner, displayName) overwrites existing metadata in OpenMetadata.
- **`storeServiceConnection`**: Controls whether sensitive connection information is persisted in the database or used only at runtime. Default is `true`.
- **`markDeletedTables`/`markDeletedSchemas`/`markDeletedDatabases`/`markDeletedStoredProcedures`**: Soft-deletion toggles for entities no longer present in the source.

## Critical Design Details

- The Data Quality workflow executes ALL tests present on the table, regardless of what is defined in the YAML. Tests defined in YAML are added to the table, but execution scope is the entire test suite.
- The `incremental` extraction configuration is marked as Beta and currently only implemented for BigQuery, Redshift, and Snowflake.
- The `threads` parameter for metadata extraction is marked as Beta.

## Relationship to UI-Based Workflow

The external ingestion workflow is an alternative to the [[metadata-ingestion-workflow|UI-based workflow]]. Both approaches use the same underlying ingestion framework and produce the same metadata. The external approach is preferred for:
- Custom orchestration requirements
- Environments where the UI-based scheduler is not available
- Integration with existing CI/CD pipelines
- Fine-grained control over execution parameters
