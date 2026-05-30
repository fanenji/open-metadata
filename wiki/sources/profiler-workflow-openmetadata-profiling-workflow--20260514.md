---
type: source
title: "Source: profiler-workflow-openmetadata-profiling-workflow--20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["profiler-workflow-openmetadata-profiling-workflow--20260514.md"]
tags: []
related: []
---

# Source: profiler-workflow-openmetadata-profiling-workflow--20260514.md

## Key Entities

- **Profiler Agent** — Central entity; a configurable, schedulable pipeline that computes metrics and runs data quality tests on tables. Likely already exists in wiki under [[data-profiling]] or [[metadata-agent]].
- **Profiler Workflow** — The specific pipeline configuration for profiling; supports multiple workflows per service with different schedules/filters. Likely already exists in wiki.
- **OpenMetadata UI** — Primary configuration interface for the profiler (Agents tab, Profiler tab, Settings > Preferences). Already exists in wiki.
- **CLI** — Alternative execution method via `metadata profile -c FILENAME.yaml`. Already exists in wiki as [[metadata-cli]].
- **Airflow SDK** — Mentioned as an execution option for YAML-based workflows. Already exists in wiki.
- **Druid** — Database noted as unsupported for sampling. Already exists in wiki as a connector.
- **Snowflake** — Mentioned with a specific recommendation (thread count = 1). Already exists in wiki.
- **Google BigQuery** — Mentioned with a partitioning limitation (month/year intervals unsupported for timestamp/datetime columns). Already exists in wiki.

## Key Concepts

- **Data Profiling** — Process of analyzing data to understand its structure, content, and quality. Already exists in wiki as [[data-profiling]].
- **Profile Sample** — Percentage or row count used to limit the data scanned by the profiler. Not explicitly in wiki; should be added.
- **Partitioning** — Strategy to limit data scanned by dividing tables into logical segments (TIME-UNIT, INGESTION-TIME, COLUMN-VALUE, INTEGER-RANGE). Not explicitly in wiki; should be added.
- **Compute Metrics** — Toggle to enable/disable metric computation; useful when only sample data ingestion is desired. Not in wiki.
- **Table-Level Configuration** — Per-table overrides for profile sample, column inclusion/exclusion, and partitioning. Not in wiki.
- **Platform-Level Configuration** — Global settings to disable metrics by data type or specific metric by data type. Not in wiki.
- **Debug Logging** — Toggle to enable debug-level logging for troubleshooting. Already exists in wiki under [[ingestion-pipeline-troubleshooting]].
- **Include Views** — Option to profile view entity types; noted as potentially performance-negative. Not in wiki.
- **Use FQN For Filtering** — Option to apply filters on Fully Qualified Names instead of raw names. Not in wiki.
- **Timeout in Seconds** — Per-table profiling timeout (default 12 hours); profiler waits for hanging queries to terminate. Not in wiki.
- **Thread Count** — Number of threads for metric computation; Snowflake-specific recommendation of 1. Not in wiki.
- **Sample Data Rows Count** — Number of rows to ingest when sample data toggle is on (default 50). Not in wiki.
- **Datalake NaN Handling** — NaN values dropped via `dropna()` but null values retained for metric computation. Not in wiki.

## Main Arguments & Findings

- **Core Claim**: The Profiler Workflow is a configurable pipe
