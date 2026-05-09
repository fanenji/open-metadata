---
type: concept
title: PostgreSQL Foreign Data Wrappers
created: 2026-04-29
updated: 2026-04-29
tags: [postgresql, foreign-data-wrapper, integration, data-access]
related: [duckdb-fdw, duckdb-postgres-scanner, duckdb-pushdown-mechanism]
sources: ["Loading Parquet in PostgreSQL via DuckDB Testing queries and exploring the Core.md"]
---
# PostgreSQL Foreign Data Wrappers

**Foreign Data Wrappers (FDWs)** are a PostgreSQL extension mechanism that allows PostgreSQL to access external data sources as if they were local tables. FDWs implement the SQL/MED (Management of External Data) standard, enabling seamless integration with remote databases, file formats, and other data systems.

## How FDWs Work

1. A **foreign server** is defined with connection parameters to the external data source.
2. **Foreign tables** are created with column definitions matching the external data.
3. PostgreSQL's query planner can delegate parts of query execution to the foreign server via **pushdown** of filters, projections, and aggregations.
4. The FDW extension handles the translation between PostgreSQL's query plan and the external data source's API.

## Key FDWs in the Data Platform

- **[[duckdb-fdw]]** — Loads DuckDB as a foreign data wrapper, enabling PostgreSQL to query Parquet files and other DuckDB-supported formats.
- **[[duckdb-postgres-scanner]]** — DuckDB extension for querying PostgreSQL databases (reverse direction).

## Design Considerations

- **Function Support**: FDWs only support a subset of SQL functions for full delegation. Unsupported functions cause two-stage execution, degrading performance.
- **Pushdown Capabilities**: The extent to which filters, projections, and aggregations are pushed to the foreign server determines query performance.
- **Memory vs. Persistent**: In-memory FDWs (like DuckDB FDW with `:memory:`) are suitable for read-only analytical workloads but lose data on process exit.

## Related

- [[duckdb-fdw]] — DuckDB FDW implementation.
- [[duckdb-pushdown-mechanism]] — Pushdown limitations.
- [[duckdb-postgres-scanner]] — Reverse direction integration.