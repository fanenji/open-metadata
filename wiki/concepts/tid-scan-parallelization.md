---
type: concept
title: TID Scan Parallelization
created: 2026-04-04
updated: 2026-04-04
tags: [postgresql, parallelization, performance, duckdb]
related: [duckdb-postgres-scanner, duckdb-postgres-scanner-implementation, binary-transfer-mode]
sources: ["Querying Postgres Tables Directly from DuckDB.md"]
---

# TID Scan Parallelization

TID Scan (Tuple ID Scan) is a PostgreSQL operator that allows querying a specific range of tuple IDs from a table. Tuple IDs have the form `(page, tuple)`, where `page` is the database page number and `tuple` is the tuple index within that page.

## Usage in DuckDB Postgres Scanner

The DuckDB Postgres Scanner uses TID scans to parallelize reads from PostgreSQL tables. Each scan task reads 1000 pages. For a table with 2500 pages, three tasks would be created with TID ranges:

- `[(0,0),(999,0)]`
- `[(1000,0),(1999,0)]`
- `[(2000,0),(UINT32_MAX,0)]`

The last range has an open bound because `relpages` in `pg_class` is merely an estimate.

## Benefits

- Enables efficient intra-query parallelism for PostgreSQL scans.
- Does not rely on the table schema.
- Equalizes effort across tasks because page size is fixed.

## Limitations

- TIDs are not stable and may be changed by operations like `VACUUM ALL`.
- Requires snapshot synchronization to ensure consistent reads across parallel connections.
- May have edge cases with very active tables.