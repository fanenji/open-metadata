type: entity
title: DuckLake
created: 2026-04-29
updated: 2026-04-29
tags: [open-table-format, lakehouse, duckdb, metadata]
related: [duckdb, apache-iceberg, delta-lake, data-lakehouse, ducklake-small-write-inlining, ducklake-snapshot-model, mark-raasveldt, hannes-muhleisen, amin-siddique]
sources: ["iceberg-built-a-maze-ducklake-just-handed-you-a-map.md"]
---
# DuckLake

DuckLake is an open table format developed by the DuckDB team that stores all lakehouse metadata in a SQL database instead of file-based metadata on blob storage. It ships as a DuckDB extension and is licensed under MIT.

## Architecture

DuckLake's architecture consists of two components:

1. **Catalog Database (SQL metadata store):** Stores snapshots, schemas, file paths, column statistics, and transaction logs. Any ACID-compliant database works (PostgreSQL, MySQL, SQLite, or DuckDB itself).
2. **Blob Storage (Parquet data files):** Immutable Parquet files named with UUIDs, stored on local disk, S3, GCS, or Azure Blob. Fully compatible with Apache Iceberg data file format.

When a query runs, the engine fires a single SQL query at the catalog database, returning the current snapshot, relevant Parquet file paths (pre-filtered by partition and column statistics), and schema information in one round trip.

## Key Properties

- **Single round trip** to resolve full table metadata (vs. 6-10+ for Iceberg)
- **Snapshots without compaction tax** — snapshots are SQL rows; adding is an insert, expiring is a delete
- **Small write inlining** — writes below a configurable threshold can inline data directly into the catalog database, bypassing Parquet writes
- **Multi-table ACID transactions** — cross-table transactions supported natively
- **Native encryption** — encryption specified at the format level with keys managed by the catalog database
- **Metadata-only migration** — data files are Iceberg-compatible Parquet, enabling migration without rewriting data

## Limitations

- DuckDB-only engine support (v0.1)
- Catalog database becomes critical infrastructure for every read and write
- No production war stories or enterprise-scale stress testing
- Ecosystem has not yet formed

## Setup

DuckLake ships as a DuckDB extension. Setup requires a SQL database for the catalog and a storage location for Parquet files. For development, a local DuckDB file can serve as the catalog.