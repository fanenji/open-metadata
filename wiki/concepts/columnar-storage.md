type: concept
title: Columnar Storage
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, storage, performance, analytics]
related: [duckdb, duckdb-performance-benchmarks, duckdb-vs-postgresql-for-analytics, data-lakehouse]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# Columnar Storage

Columnar storage is a data storage paradigm where values from the same column are stored contiguously on disk, rather than storing entire rows together (row-oriented storage). This is the fundamental architectural difference between analytical databases like DuckDB and transactional databases like PostgreSQL.

## How It Works

- **Row-oriented** (PostgreSQL, MySQL): All columns of a row are stored together. Good for point lookups and frequent updates.
- **Column-oriented** (DuckDB, Parquet): All values of a column are stored together. Good for analytical queries that read few columns but many rows.

## Why It Matters for Analytics

- **Reduced I/O**: Analytical queries typically read a subset of columns (e.g., `SELECT country, COUNT(*)` only needs two columns). Columnar storage reads only those columns, not entire rows.
- **Better compression**: Values in a single column tend to have similar characteristics, enabling better compression ratios (especially with dictionary encoding, run-length encoding).
- **Vectorized processing**: Columnar layout enables SIMD vectorization — processing multiple values with a single CPU instruction.

## DuckDB's Implementation

DuckDB uses columnar storage internally and can directly query columnar formats like Parquet without conversion. This is why DuckDB can scan 50GB Parquet files in 4.2 seconds while PostgreSQL takes 89 seconds — PostgreSQL must read entire rows even when only a few columns are needed.

## Limitations

- Poor performance for point lookups (single row by ID)
- Slow for frequent updates and inserts
- Higher memory overhead for row reconstruction

## Relevance

Columnar storage is the primary reason DuckDB outperforms PostgreSQL for analytical workloads. The article's benchmarks (21-33x speedup) are largely attributable to this architectural difference.