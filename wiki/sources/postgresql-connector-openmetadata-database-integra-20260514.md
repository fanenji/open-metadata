---
type: source
title: "PostgreSQL Connector | OpenMetadata Database Integration"
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, connector, metadata-ingestion, database, openmetadata]
related: [postgresql-connector, pg-stat-statements, stored-procedure-lineage, postgresql-ssl-modes, postgresql-iam-authentication, autopilot, hybrid-ingestion-runner-secret-management, incremental-metadata-extraction]
sources: ["postgresql-connector-openmetadata-database-integra-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/postgres"
venue: "OpenMetadata Documentation"
---

# PostgreSQL Connector | OpenMetadata Database Integration

Official documentation for the PostgreSQL connector in OpenMetadata v1.12.x. Covers requirements, `pg_stat_statements` limitations, IAM authentication, stored procedure lineage, SSL configuration, and the full metadata ingestion workflow.

## Key Topics

- **Requirements**: Officially supported PostgreSQL versions only.
- **Usage & Lineage**: Relies on `pg_stat_statements` extension; documents critical limitations (entry eviction, query normalization, no timestamps, reset vulnerability).
- **Custom Query Statement Source**: Alternative to `pg_stat_statements` using a custom view/table with specific column requirements (`userid`, `dbid`, `query`, `total_exec_time`/`total_time`).
- **IAM Authentication**: AWS RDS-specific setup with `rds_iam` role grant and `rds-db:connect` IAM permission.
- **Stored Procedures**: Requires `log_statement = 'all'` and `pg_stat_statements.track = 'all'` for lineage extraction.
- **SSL Configuration**: CA certificate only required; IAM auth recommends `allow` mode.
- **Hybrid Ingestion Runner**: Secret management format (`password: secret:/my/database/password`).
- **AutoPilot**: Automated handling of usage tracking, data lineage, and similar workflows.
- **Incremental Metadata Extraction (Beta)**: Not available for PostgreSQL (only BigQuery, Redshift, Snowflake).
- **Threads (Beta)**: Multithread approach for Metadata Extraction.

## Connection Details

- **Auth Types**: Basic Auth (username/password) or IAM Based Auth (AWS credentials, Assume Role).
- **SSL Modes**: `disable`, `allow`, `prefer`, `require`, `verify-ca`, `verify-full`.
- **Filter Patterns**: Database, schema, and table level inclusion/exclusion via regex.
- **Ingestion Options**: Include/exclude tables, views, tags, owners, stored procedures, DDL statements.

## Recommendations

- Increase `pg_stat_statements.max` to at least 10000.
- Set `pg_stat_statements.track = 'all'`.
- Schedule frequent ingestion runs (every 1–2 hours).
- Avoid `pg_stat_statements_reset()` before ingestion.

## Related Pages

- [[postgresql-connector]] — Entity page for the PostgreSQL connector.
- [[pg-stat-statements]] — Detailed concept page on `pg_stat_statements` limitations and alternatives.
- [[stored-procedure-lineage]] — Configuration requirements for stored procedure lineage.
- [[postgresql-ssl-modes]] — SSL connection modes for PostgreSQL.
- [[postgresql-iam-authentication]] — IAM authentication setup for AWS RDS PostgreSQL.
- [[autopilot]] — Automated workflow management feature.
- [[hybrid-ingestion-runner-secret-management]] — Secret management for hybrid runners.
- [[incremental-metadata-extraction]] — Beta feature for changed-table detection.