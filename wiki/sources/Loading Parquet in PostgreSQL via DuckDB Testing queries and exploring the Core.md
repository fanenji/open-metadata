---
type: source
title: "Loading Parquet in PostgreSQL via DuckDB: Testing queries and exploring the Core"
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, postgresql, parquet, foreign-data-wrapper, integration]
related: [duckdb-fdw, postgresql-foreign-data-wrappers, duckdb-postgres-scanner, duckdb-pushdown-mechanism, duckdb-performance-guide]
sources: ["Loading Parquet in PostgreSQL via DuckDB Testing queries and exploring the Core.md"]
authors: [ah]
year: 2023
url: "https://medium.com/@ahuarte/loading-parquet-in-postgresql-via-duckdb-testing-queries-and-exploring-the-core-1d667ae67dc2"
venue: Medium
---
# Loading Parquet in PostgreSQL via DuckDB: Testing queries and exploring the Core

This article by **ah** (ahuarte) demonstrates how to integrate DuckDB into PostgreSQL using the [[duckdb-fdw]] (Foreign Data Wrapper) extension to load Parquet files as foreign tables. The author benchmarks the setup using the NYC Taxi Data dataset (21 million records, ~400MB) and explores the performance characteristics and limitations of the integration.

## Key Findings

- **Core Claim**: DuckDB FDW enables PostgreSQL to query Parquet files as foreign tables with good performance.
- **Benchmark Results**: Sub-second `COUNT(*)` and ~4 seconds for filtered queries on old hardware (9-year-old SATA disk).
- **Function Support Limitation**: The FDW only supports a subset of SQL functions (`sum`, `min`, `max`, `avg`, `count`) for full delegation to DuckDB. Unsupported functions like `array_agg` cause a two-stage execution: DuckDB applies the WHERE clause, then PostgreSQL applies GROUP BY locally — wasting resources.
- **Contribution**: The author implemented `array_agg` support in a pull request to enable full delegation.

## Architecture

The integration uses PostgreSQL's Foreign Data Wrapper mechanism to create a server pointing to an in-memory DuckDB instance (`:memory:`). Foreign tables are defined with the `read_parquet()` function as the data source, allowing PostgreSQL to delegate query execution to DuckDB's analytical engine.

## Limitations

- Only a subset of aggregate functions are supported for full delegation.
- Two-stage execution degrades performance for complex queries with unsupported functions.
- Performance depends on query complexity and function selection.

## Connections

- Related to [[duckdb-postgres-scanner]] (reverse direction: DuckDB queries PostgreSQL).
- Extends [[duckdb-pushdown-mechanism]] concept to the PostgreSQL-to-DuckDB direction.
- Parquet format is also covered in [[Formati e Standard]].