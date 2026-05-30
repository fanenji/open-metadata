---
type: source
title: "PostgreSQL Connector | OpenMetadata Database Integration"
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, connector, ingestion, lineage, usage, ssl, iam]
related: [postgresql-connector, pg-stat-statements, openmetadata-connectors, data-lineage, ingestion-framework, metadata-ingestion-workflow, dbt-integration, data-profiling, data-quality, postgresql-iam-authentication, postgresql-ssl-modes, stored-procedure-lineage]
sources: ["PostgreSQL Connector  OpenMetadata Database Integration.md"]
---
# PostgreSQL Connector | OpenMetadata Database Integration

Official documentation for the PostgreSQL connector in OpenMetadata v1.12.x. Covers requirements, metadata ingestion, usage and lineage workflows, stored procedure lineage configuration, SSL connection security, and IAM authentication for AWS RDS.

## Key Takeaways

- **`pg_stat_statements` is essential but limited**: It is a fixed-size, in-memory statistics collector — not a query log. Entries can be silently evicted, queries are normalized, and there are no timestamps. This directly impacts lineage and usage completeness.
- **Mitigation strategies**: Increase `pg_stat_statements.max` to 10000+, set `track = 'all'`, schedule frequent ingestion (1–2 hours), and avoid premature resets.
- **Custom query source option**: Organizations can point OpenMetadata to a custom view/table instead of `pg_stat_statements` if it matches the expected column schema.
- **Stored procedure lineage**: Requires explicit configuration (`log_statement = 'all'` and `pg_stat_statements.track = 'all'`) to capture internal procedure queries.
- **SSL and IAM authentication**: SSL uses standard PostgreSQL modes with CA certificate; IAM is AWS RDS-specific with documented IAM policy permissions.