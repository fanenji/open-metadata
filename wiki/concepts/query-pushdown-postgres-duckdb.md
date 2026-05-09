---
type: concept
title: Query Pushdown from PostgreSQL to DuckDB
created: 2026-04-04
updated: 2026-04-04
tags: [postgres, duckdb, query-pushdown, analytics, hooks]
related: [postgres-native-analytics, duckdb, duckdb-postgres-scanner, duckdb-pushdown-mechanism, crunchy-bridge]
sources: ["Unleashing Postgres for Analytics With DuckDB Integration.md"]
---
# Query Pushdown from PostgreSQL to DuckDB

Query pushdown from PostgreSQL to DuckDB is a mechanism that uses Postgres hooks to decompose a query plan into parts that can be executed by [[DuckDB]] for vectorized, parallel processing. The Postgres extension framework intercepts the query planning process, identifies subplans suitable for DuckDB (e.g., filters, aggregates, joins), and constructs appropriate SQL queries to pass to DuckDB. In some cases, the entire query is pushed down; in others, different subplans are merged.

This is distinct from the [[duckdb-postgres-scanner]], which works in the opposite direction (DuckDB scanning Postgres tables). Here, Postgres is the orchestrator, and DuckDB is the embedded execution engine for analytical workloads.

The mechanism is central to the [[postgres-native-analytics]] pattern and is implemented in the [[Crunchy Bridge]] managed service.