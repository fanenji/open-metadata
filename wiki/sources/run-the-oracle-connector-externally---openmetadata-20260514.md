---
type: source
title: "Source: run-the-oracle-connector-externally---openmetadata-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["run-the-oracle-connector-externally---openmetadata-20260514.md"]
tags: []
related: []
---

# Source: run-the-oracle-connector-externally---openmetadata-20260514.md

## Analysis of: Run the Oracle Connector Externally - OpenMetadata Documentation

### Key Entities

- **Oracle Database** (central) — The source system; supported versions 12c, 18c, 19c, 21c. Already exists in wiki as [[oracle-connector]].
- **python-oracledb** (peripheral) — Python library used for Oracle connectivity. Not in wiki.
- **OpenMetadata Ingestion Framework** (central) — The external orchestrator running the YAML-defined workflows. Already exists in wiki as [[ingestion-framework]].
- **Metadata CLI** (central) — Command-line tool (`metadata ingest`, `metadata profile`, `metadata classify`, `metadata test`). Already exists in wiki as [[metadata-cli]].
- **JWT Token** (peripheral) — Authentication mechanism for CLI-based ingestion. Already exists in wiki as [[personal-access-token]].
- **orm-profiler** (peripheral) — Processor type used for Profiler and Auto Classification workflows. Not in wiki.
- **orm-test-runner** (peripheral) — Processor type used for Data Quality test execution. Not in wiki.

### Key Concepts

- **External Connector Execution** — Running ingestion workflows outside the OpenMetadata UI using YAML configuration files and CLI commands. Already exists in wiki as [[cli-ingestion-with-basic-auth]].
- **Oracle Connection Types** — Two modes: `oracleServiceName` (TNS alias) and `databaseSchema`. Not explicitly in wiki.
- **Oracle Instant Client** — Thick client binaries required for Oracle connectivity; shipped by default at `/instantclient` in the ingestion Docker image. Not in wiki.
- **Oracle Schema-Level SELECT Limitation** — No native Oracle routine to grant SELECT to a full schema; workarounds required for Profiler/Data Quality. Already exists in wiki as [[oracle-schema-select-limitation]].
- **Soft Deletion** — Flagging absent tables, schemas, databases, and stored procedures as deleted rather than removing them. Already exists in wiki as [[soft-deletion]].
- **Incremental Extraction (beta)** — Configuration for extracting only changed metadata since last run; currently implemented for BigQuery, Redshift, Snowflake. Not in wiki.
- **Auto Classification Workflow** — Automatic PII tagging using the `orm-profiler` processor with configurable confidence threshold. Already exists in wiki as [[auto-classification]].
- **Data Quality Test Execution** — Running tests defined in YAML or via UI; `forceUpdate` strategy for existing test cases. Already exists in wiki as [[data-quality]].

### Main Arguments & Findings

- **Core Claim**: The Oracle connector can be run externally (outside the OpenMetadata UI) using YAML configuration files and CLI commands, supporting metadata ingestion, profiling, auto-classification, data quality, lineage, and dbt integration.
- **Evidence**: Detailed YAML configuration examples for each workflow type (metadata, profiler, auto-classification, data quality, lineage) with CLI commands (`metadata ingest`, `metadata profile`, `metadata classify`, `metadata test`).
- **Evidence Strength**: Strong 
