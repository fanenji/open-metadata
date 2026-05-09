---
type: source
title: Querying Postgres Tables Directly from DuckDB
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, postgresql, postgres-scanner, performance, benchmark]
related: [duckdb, duckdb-postgres-scanner, duckdb-pushdown-mechanism, data-virtualization-pattern, elt-pattern]
sources: ["Querying Postgres Tables Directly from DuckDB.md"]
authors: [Hannes Mühleisen]
year: 2022
url: https://duckdb.org/2022/09/30/postgres-scanner?s=09
venue: DuckDB Blog
---

# Querying Postgres Tables Directly from DuckDB

**Author:** Hannes Mühleisen  
**Published:** 2022-09-30  
**Source:** [DuckDB Blog](https://duckdb.org/2022/09/30/postgres-scanner?s=09)

## Summary

This blog post introduces the DuckDB Postgres Scanner extension, which enables DuckDB to directly query tables stored in a running PostgreSQL database without data duplication. The extension uses PostgreSQL's binary transfer protocol, TID-based parallelization, and snapshot synchronization to achieve analytical query performance that often matches or exceeds native PostgreSQL on OLAP workloads.

## Key Claims

- DuckDB can query live PostgreSQL tables directly, often faster than PostgreSQL itself, without data duplication.
- The scanner enables incremental caching patterns (append-only tables) and easy Parquet export from PostgreSQL.
- The scanner is currently in preview.

## Evidence

- TPC-H benchmark (SF1, ~1GB data) shows DuckDB+Postgres Scanner completes all 22 queries; PostgreSQL fails queries 17 and 20 (>60s timeout).
- DuckDB+Scanner is faster than stock PostgreSQL on roughly half the queries.
- Experiment script is provided for reproducibility.

## Limitations

- The scanner is slower than native DuckDB storage (10x on average).
- Filter pushdown is optional and can be slower when filters are not selective.
- Only reads actual tables, not views.
- TID-based parallelization relies on `pg_export_snapshot`, which may have edge cases with very active tables.
- Single hardware configuration (M1 Max) limits generalizability.

## Connections

- Strengthens [[duckdb-postgres-scanner]] with detailed implementation and performance data.
- Extends [[duckdb-pushdown-mechanism]] with concrete PostgreSQL examples.
- Relates to [[data-virtualization-pattern]] as a direct example of querying data without moving it.
- Relates to [[elt-pattern]] by enabling ELT-like workflows without full data replication.