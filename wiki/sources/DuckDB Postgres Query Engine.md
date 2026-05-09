---
type: source
title: DuckDB Postgres Query Engine
created: 2026-02-13
updated: 2026-02-13
tags: [duckdb, postgresql, query-engine, postgres-scanner]
related: [duckdb, duckdb-postgres-scanner, duckdb-pushdown-mechanism, duckdb-iceberg-extension]
sources: ["DuckDB Postgres Query Engine.md"]
---
# DuckDB Postgres Query Engine

A conversation transcript (likely from Google AI Studio) clarifying the query execution model of DuckDB's `postgres_query` function. The source explains that by default, DuckDB's own vectorized engine processes queries on PostgreSQL data, not the PostgreSQL engine. It also covers how to force native PostgreSQL execution using `postgres_query` with a raw SQL string, and the limitations of pushdown optimization.

## Key Points

- **Default Behavior:** `postgres_query` uses DuckDB's vectorized engine, reading PostgreSQL data via binary transfer mode.
- **Native PostgreSQL Execution:** Passing a raw SQL string to `postgres_query('pg_db', 'SELECT ...')` executes the query on the PostgreSQL engine.
- **Pushdown:** `postgres_scan_pushdown` pushes filters (WHERE) and projections (column selection) to PostgreSQL, but not arbitrary functions.
- **Performance:** DuckDB's engine is optimized for OLAP workloads and can parallelize table scanning.
- **Contrast:** `pg_duckdb` is a separate extension that embeds DuckDB inside PostgreSQL (reverse scenario).

## Relevance

This source clarifies a common architectural confusion about DuckDB's PostgreSQL interaction, with implications for performance, function availability, and data movement.