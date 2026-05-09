---
type: concept
title: DuckDB Postgres Scanner Implementation
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, postgresql, implementation, performance]
related: [duckdb-postgres-scanner, duckdb-pushdown-mechanism, data-virtualization-pattern]
sources: ["Querying Postgres Tables Directly from DuckDB.md"]
---

# DuckDB Postgres Scanner Implementation

The DuckDB Postgres Scanner is implemented as a plug-in extension providing a table scan function. It uses the standard `libpq` library, statically linked, and employs several optimization techniques to overcome the inherent slowness of PostgreSQL's client-server protocol.

## Binary Transfer Mode

The scanner uses PostgreSQL's rarely-used binary transfer mode, which avoids expensive to-string and from-string conversions. For example, reading an `int32` from the protocol message only requires a byte order swap (`ntohl`). Internally, the scanner issues a query like:

```sql
COPY (SELECT * FROM lineitem) TO STDOUT (FORMAT binary);
```

## TID Scan Parallelization

DuckDB's pipeline parallelism is extended to PostgreSQL scans by opening multiple connections and reading subsets of the table using TID (Tuple ID) ranges. Each scan task reads 1000 pages. TIDs have the form `(page, tuple)`. The query is extended to:

```sql
COPY (
   SELECT * FROM lineitem 
   WHERE ctid BETWEEN '(P_MIN,0)'::tid AND '(P_MAX,0)'::tid
) TO STDOUT (FORMAT binary);
```

## Snapshot Synchronization

To ensure consistent reads across parallel connections, the scanner:
1. Creates a read-only transaction in DuckDB's bind phase.
2. Exports the snapshot using `pg_export_snapshot()`.
3. Imports the snapshot into parallel connections using `SET TRANSACTION SNAPSHOT ...`.

This ensures all connections see the table state as it appeared at the beginning of the scan.

## Projection and Selection Pushdown

DuckDB's optimizer pushes projections (removal of unused columns) and selections (row filters) to PostgreSQL. Projections reduce bytes transferred. Selections construct SQL filter expressions from pushed-down filters. Filter pushdown is optional via the `filter_pushdown` parameter and may be slower when filters are not selective.

## Incremental Caching Pattern

The scanner enables incremental caching for append-only tables:

```sql
INSERT INTO my_table_duckdb_cache
SELECT * FROM postgres_scan('dbname=myshinydb', 'public', 'my_table') 
WHERE incrementing_id_column > (SELECT max(incrementing_id_column) FROM my_table_duckdb_cache);
```

## Parquet Export

The scanner provides a simple way to export PostgreSQL tables to Parquet:

```sql
COPY (SELECT * FROM postgres_scan('dbname=myshinydb', 'public', 'lineitem')) TO 'lineitem.parquet' (FORMAT parquet);
```