---
type: entity
title: Crunchy Bridge
created: 2026-04-04
updated: 2026-04-04
tags: [postgres, managed-service, analytics, duckdb]
related: [crunchy-data, duckdb, postgres-native-analytics, query-pushdown-postgres-duckdb]
sources: ["Unleashing Postgres for Analytics With DuckDB Integration.md"]
---
# Crunchy Bridge

Crunchy Bridge is a managed PostgreSQL service offered by [[Crunchy Data]]. It provides a Postgres-native analytics capability by integrating [[DuckDB]] as an embedded query engine via the Postgres extension framework. The service uses Postgres hooks to transparently push down parts of a query plan to DuckDB for vectorized, parallel execution, enabling users to query data stored in S3 (in Parquet or Iceberg formats) alongside standard Postgres tables.

Key features include:
- Access controls, views, materialized views, stored procedures, and pg_cron jobs.
- Long-lived NVMe and in-memory caches for analytical data.
- Integration with pg_stat_statements for query performance insights.
- A developer-focused UX that abstracts the complexity of hooks and query pushdown.

Crunchy Bridge is positioned as a solution for organizations that want to keep analytical workloads within the Postgres ecosystem without replicating data to third-party analytics platforms.