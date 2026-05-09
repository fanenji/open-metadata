---
type: concept
title: pg_export_snapshot Pattern
created: 2026-04-04
updated: 2026-04-04
tags: [postgresql, transactions, consistency, duckdb]
related: [duckdb-postgres-scanner, duckdb-postgres-scanner-implementation, tid-scan-parallelization]
sources: ["Querying Postgres Tables Directly from DuckDB.md"]
---

# pg_export_snapshot Pattern

The `pg_export_snapshot` pattern is a PostgreSQL feature that allows exporting the current transaction context from one connection and importing it into other connections using `SET TRANSACTION SNAPSHOT`. This ensures all connections see the same consistent view of the database.

## Usage in DuckDB Postgres Scanner

The DuckDB Postgres Scanner uses this pattern to synchronize parallel TID scans:

1. Create a read-only transaction in DuckDB's bind phase (query planning).
2. Export the snapshot using `pg_export_snapshot()`.
3. Import the snapshot into parallel read connections using `SET TRANSACTION SNAPSHOT ...`.

This ensures all connections related to one table scan see the table state exactly as it appeared at the beginning of the scan, throughout the potentially lengthy read process.

## Benefits

- Enables consistent parallel reads from an actively used PostgreSQL database.
- Avoids issues with concurrent transactions modifying the table during the scan.
- Works with the TID scan parallelization approach.

## Limitations

- `pg_export_snapshot` is a little-known PostgreSQL feature.
- May have edge cases with very active tables or long-running transactions.
- Requires careful transaction management to avoid holding snapshots for too long.