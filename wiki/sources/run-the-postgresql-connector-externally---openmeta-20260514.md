---
type: source
title: "Run the PostgreSQL Connector Externally - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, connector, ingestion, yaml, cli, metadata-ingestion, data-quality, data-profiling, auto-classification, lineage, usage]
related: [postgresql-connector, pg-stat-statements, postgresql-ssl-modes, postgresql-iam-authentication, metadata-cli, external-ingestion-workflow, data-quality, data-profiling, auto-classification, cli-ingestion-with-basic-auth, dbt-integration]
sources: ["run-the-postgresql-connector-externally---openmeta-20260514.md"]
---
# Run the PostgreSQL Connector Externally - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for running the PostgreSQL connector externally (outside the OpenMetadata UI) using YAML configuration files and CLI commands. It provides complete, working YAML examples for six distinct workflow types: Metadata Ingestion, Query Usage, Lineage, Data Profiler, Auto Classification, and Data Quality.

## Key Content

- **Metadata Ingestion**: YAML configuration for extracting database metadata (tables, views, schemas, stored procedures) using the `metadata ingest` CLI command. Covers authentication (basic and IAM), SSL configuration, connection options, and source config toggles (markDeletedTables, includeViews, overrideMetadata, etc.).
- **Query Usage**: YAML configuration for extracting query history from `pg_stat_statements` using the `metadata usage` CLI command. Includes queryLogDuration, stageFileLocation, and resultLimit parameters.
- **Lineage**: YAML configuration for extracting data lineage from query history using the `metadata ingest` CLI command with `DatabaseLineage` type. Covers view lineage, query lineage, and stored procedure lineage with process toggles.
- **Data Profiler**: YAML configuration for computing data profile metrics using the `metadata profile` CLI command with the `orm-profiler` processor. Supports table-level configuration, partition config, and custom profile queries.
- **Auto Classification**: YAML configuration for automatically tagging columns with PII classifications using the `metadata classify` CLI command. Includes confidence threshold and sample data storage toggle.
- **Data Quality**: YAML configuration for executing test cases using the `metadata test` CLI command. Critical design detail: the workflow executes ALL tests present on the table, regardless of what is defined in the YAML.

## Critical Design Details

- The Data Quality workflow executes ALL tests on the table, not just those defined in the YAML. Tests defined in YAML are added to the table, but execution scope is the entire test suite.
- The `overrideMetadata` toggle controls whether fetched metadata (description, tags, owner, displayName) overwrites existing metadata in OpenMetadata.
- The `storeServiceConnection` toggle (default: true) controls whether sensitive connection information is persisted in the database or used only at runtime.
- The `incremental` extraction configuration is marked as Beta and only implemented for BigQuery, Redshift, and Snowflake — not for PostgreSQL.
- The `threads` parameter for metadata extraction is marked as Beta.

## Connections

- Strengthens [[postgresql-connector]] with complete YAML-based external execution workflow.
- Strengthens [[pg-stat-statements]] with specific configuration requirements for Usage and Lineage workflows.
- Strengthens [[postgresql-ssl-modes]] and [[postgresql-iam-authentication]] with YAML configuration syntax.
- Extends [[cli-ingestion-with-basic-auth]] with additional CLI commands (`metadata usage`, `metadata profile`, `metadata classify`, `metadata test`).
- References [[dbt-integration]] for model definitions and lineage.
