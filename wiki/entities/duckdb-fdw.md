---
type: entity
title: DuckDB FDW
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, postgresql, foreign-data-wrapper, extension]
related: [duckdb, postgresql, parquet, duckdb-postgres-scanner, postgresql-foreign-data-wrappers]
sources: ["Loading Parquet in PostgreSQL via DuckDB Testing queries and exploring the Core.md"]
---
# DuckDB FDW

**DuckDB FDW** (Foreign Data Wrapper) is a PostgreSQL extension that enables PostgreSQL to load DuckDB as a foreign data wrapper, allowing PostgreSQL to query Parquet files and other DuckDB-supported data sources as foreign tables.

## Key Features

- Loads DuckDB as an in-process analytical engine within PostgreSQL.
- Supports in-memory DuckDB databases (`:memory:`) for transient query processing.
- Delegates query execution to DuckDB for supported functions.
- Enables PostgreSQL to leverage DuckDB's columnar storage and analytical performance.

## Installation

The extension is maintained by **alitrack** and is available at [github.com/alitrack/duckdb_fdw](https://github.com/alitrack/duckdb_fdw). Installation requires building the extension from source and installing it into the PostgreSQL environment.

## Configuration

```sql
CREATE EXTENSION duckdb_fdw;
CREATE SERVER duckdb_svr FOREIGN DATA WRAPPER duckdb_fdw OPTIONS (database ':memory:');
CREATE FOREIGN TABLE taxi_table (...) SERVER duckdb_svr OPTIONS (table 'read_parquet("/path/to/*.parquet")');
```

## Known Limitations

- Only supports a subset of aggregate functions for full delegation: `sum`, `min`, `max`, `avg`, `count`.
- Unsupported functions (e.g., `array_agg`) cause two-stage execution: DuckDB applies WHERE clause, PostgreSQL applies GROUP BY locally.
- This two-stage execution can degrade performance significantly for complex queries.

## Related

- [[duckdb-postgres-scanner]] — The reverse direction: DuckDB queries PostgreSQL.
- [[postgresql-foreign-data-wrappers]] — Broader FDW patterns.
- [[duckdb-pushdown-mechanism]] — Pushdown limitations from the PostgreSQL side.