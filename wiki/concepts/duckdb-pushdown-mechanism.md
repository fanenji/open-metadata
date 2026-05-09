---
type: concept
title: DuckDB Pushdown Mechanism
created: 2026-02-13
updated: 2026-02-13
tags: [duckdb, pushdown, query-optimization, postgresql]
related: [duckdb, duckdb-postgres-scanner, duckdb-iceberg-extension]
sources: ["DuckDB Postgres Query Engine.md"]
---
# DuckDB Pushdown Mechanism

DuckDB's pushdown mechanism allows certain query operations to be offloaded to the source database (e.g., PostgreSQL) before data is transferred to DuckDB's engine. This reduces network transfer and can improve performance.

## Supported Pushdown Operations

- **Filters (WHERE clauses):** DuckDB can push down filtering conditions to PostgreSQL, so only matching rows are transferred.
- **Projections (column selection):** DuckDB can push down column selection, so only needed columns are transferred.

## Limitations

- **No arbitrary function pushdown:** DuckDB does not push down arbitrary SQL functions to PostgreSQL. Only basic filtering and column selection are supported.
- **Use `postgres_query` for native functions:** If PostgreSQL-specific functions are needed, use `postgres_query` with a raw SQL string to execute the query on the PostgreSQL engine.

## Generalization

The pushdown concept applies to other DuckDB extensions as well (e.g., `duckdb-iceberg-extension`), where filters and projections can be pushed down to the data source to reduce data movement.

## Performance Implications

- Pushdown is most beneficial when the source database can efficiently filter or project data, reducing the volume of data transferred over the network.
- For complex analytical queries, DuckDB's engine is typically faster than PostgreSQL, so pushdown of filters/projections combined with DuckDB processing is often optimal.