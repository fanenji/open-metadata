---
type: concept
title: Postgres-Native Analytics
created: 2026-04-04
updated: 2026-04-04
tags: [postgres, analytics, olap, duckdb, query-pushdown]
related: [query-pushdown-postgres-duckdb, crunchy-bridge, duckdb, duckdb-postgres-scanner, data-lakehouse]
sources: ["Unleashing Postgres for Analytics With DuckDB Integration.md"]
---
# Postgres-Native Analytics

Postgres-native analytics refers to the pattern of extending PostgreSQL to perform analytical (OLAP) workloads without moving data to a separate analytics platform. This is achieved by integrating specialized query engines (such as [[DuckDB]]) into Postgres via the extension framework, using hooks to transparently push down parts of a query plan for vectorized, parallel execution.

Key characteristics:
- Data remains in S3 (or similar object storage) in open formats like Parquet or Iceberg.
- Queries are executed through standard PostgreSQL interfaces (SQL, views, materialized views, stored procedures).
- Access controls, monitoring (pg_stat_statements), and scheduling (pg_cron) work as usual.
- The complexity of hooks and pushdown mechanics is abstracted, often via a managed service like [[Crunchy Bridge]].

This approach contrasts with traditional solutions that require forking Postgres or replicating data to third-party analytics platforms. It aligns with the trend toward separation of compute and storage, with S3 as the center of gravity for analytical data.

**Note:** The term "native" is somewhat aspirational — the solution relies on an external engine (DuckDB) and is typically offered as a managed service, which may introduce vendor lock-in and complexity.