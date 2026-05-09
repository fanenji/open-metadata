---
type: entity
title: DuckDB Postgres Scanner Extension
created: 2026-02-13
updated: 2026-05-07
tags: [duckdb, postgresql, extension, query-engine, scanner]
related: [duckdb, duckdb-pushdown-mechanism, duckdb-iceberg-extension, postgresql, data-virtualization-pattern, elt-pattern]
sources: ["DuckDB Postgres Query Engine.md", "Querying Postgres Tables Directly from DuckDB.md"]
---

# DuckDB Postgres Scanner Extension

The `postgres_scanner` extension enables DuckDB to directly query tables stored in a running PostgreSQL database without data duplication. It connects to a PostgreSQL instance, reads data via PostgreSQL's binary transfer mode, and processes queries using DuckDB's vectorized query engine. The extension is installed with `INSTALL postgres_scanner` and loaded with `LOAD postgres_scanner`.

## Key Features

- **Binary Transfer Mode**: Uses PostgreSQL's binary protocol to avoid expensive string conversions, reading data in a format close to the on-disk representation.
- **TID Scan Parallelization**: Opens multiple connections to PostgreSQL and reads subsets of the table using Tuple ID (TID) ranges, enabling intra-query parallelism.
- **Snapshot Synchronization**: Uses `pg_export_snapshot()` and `SET TRANSACTION SNAPSHOT` to ensure all parallel connections see the same consistent view of the table.
- **Projection and Selection Pushdown**: DuckDB's optimizer pushes column selection and row filters (e.g., WHERE clauses) to PostgreSQL to reduce data transfer. Filter pushdown is optional via the `filter_pushdown` parameter. Note that arbitrary functions are not pushed down.

## Functions

- **`postgres_scan_pushdown`**: Scans a PostgreSQL table with pushdown of filters and projections. Example: `postgres_scan_pushdown('dbname=myshinydb', 'public', 'mytable')`.
- **`postgres_query`**: Sends a raw SQL string to PostgreSQL for native execution by the PostgreSQL engine. Use this when PostgreSQL-specific functions are required.
- **`postgres_attach`**: Attaches all tables from a PostgreSQL database. Example: `CALL postgres_attach('dbname=myshinydb')`.

## Execution Model

- **Default (pushdown)**: DuckDB's engine reads PostgreSQL data via binary transfer and processes the query, optimized for analytical (OLAP) workloads.
- **Native PostgreSQL**: By using `postgres_query`, the query is executed by the PostgreSQL engine. Results are returned to DuckDB. Useful for transactional queries or PostgreSQL-specific functions.

## Performance

- DuckDB's vectorized engine is optimized for complex analytical queries and can parallelize scanning of PostgreSQL tables via TID scan parallelization.
- Pushdown reduces network transfer by filtering and projecting data at the source.
- In TPC-H benchmark (SF1, ~1GB), DuckDB+Postgres Scanner completed all 22 queries, while PostgreSQL failed queries 17 and 20 (>60s timeout). The scanner was faster than stock PostgreSQL on roughly half the queries, though it is approximately 10x slower than native DuckDB storage.

## Limitations

- Only reads actual tables, not views.
- Filter pushdown can be slower when filters are not selective.
- TID-based parallelization may have edge cases with very active tables.
- Slower than native DuckDB storage on cached data.

## Comparison with pg_duckdb

`pg_duckdb` is a separate PostgreSQL extension that embeds DuckDB inside PostgreSQL (the reverse scenario). It allows PostgreSQL to use the DuckDB engine for certain queries.

## Related

- [[duckdb]]
- [[duckdb-pushdown-mechanism]]
- [[duckdb-iceberg-extension]]
- [[postgresql]]
- [[data-virtualization-pattern]]
- [[elt-pattern]]