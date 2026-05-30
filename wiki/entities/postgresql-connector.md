---
type: entity
title: PostgreSQL Connector
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, connector, ingestion, openmetadata]
related: [openmetadata-connectors, pg-stat-statements, postgresql-iam-authentication, postgresql-ssl-modes, stored-procedure-lineage, data-lineage, ingestion-framework, metadata-ingestion-workflow, dbt-integration, data-profiling, data-quality, oracle-connector]
sources: ["PostgreSQL Connector  OpenMetadata Database Integration.md"]
---
# PostgreSQL Connector

The PostgreSQL connector is a turnkey [[openmetadata-connectors|OpenMetadata connector]] for ingesting metadata from PostgreSQL databases. It supports the full suite of ingestion workflows: metadata, query usage, lineage, data profiling, data quality, and [[dbt-integration|dbt integration]].

## Requirements

- Only officially supported PostgreSQL versions are supported.
- For usage and lineage workflows, the `pg_stat_statements` extension must be enabled and the OpenMetadata user must have read access (`GRANT pg_read_all_stats`).

## Key Configuration Areas

### Usage & Lineage via `pg_stat_statements`

The connector relies on [[pg-stat-statements|pg_stat_statements]] to read query history. This extension has significant limitations (eviction, normalization, no timestamps) that affect lineage completeness. See the dedicated [[pg-stat-statements]] concept page for details and mitigation strategies.

### Query Statement Source

A connection property allows pointing OpenMetadata to a custom view or table instead of `pg_stat_statements`. The custom source must expose columns matching the expected schema: `userid` (oid), `dbid` (oid), `query` (text), and either `total_exec_time` (PostgreSQL 13+) or `total_time` (PostgreSQL < 13).

### Stored Procedure Lineage

PostgreSQL does not track internal queries of stored procedures in `pg_stat_statements` by default. To capture lineage from stored procedures, both `log_statement = 'all'` and `pg_stat_statements.track = 'all'` must be set in `postgresql.conf`. See [[stored-procedure-lineage]].

### SSL Connection Security

SSL modes (`prefer`, `verify-ca`, `allow`, etc.) are configurable under Advanced Config, along with the CA certificate for validation. See [[postgresql-ssl-modes]].

### IAM Authentication (AWS RDS)

For AWS RDS PostgreSQL, IAM authentication requires IAM DB authentication enabled on the RDS instance, a database user granted the `rds_iam` role, and an IAM policy with `rds-db:connect` permission. See [[postgresql-iam-authentication]].

## Related Workflows

- [[metadata-ingestion-workflow|Metadata Ingestion]]
- [[data-lineage|Lineage Workflow]]
- [[data-profiling|Profiler Workflow]]
- [[data-quality|Data Quality Workflow]]
- [[dbt-integration|dbt Integration]]