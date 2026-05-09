---
type: concept
title: DuckDB Iceberg Extension
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, iceberg, extension, query-engine]
related: [duckdb, iceberg-query-engine-comparison, data-lakehouse, predicate-pushdown]
sources: ["Duckdb and Iceberg  Definite.md"]
---
# DuckDB Iceberg Extension

The DuckDB Iceberg extension enables DuckDB to directly query and manipulate Apache Iceberg tables. It is installed via SQL commands within a DuckDB session and provides the `iceberg_scan()` function for reading Iceberg tables.

## Installation and Usage

```sql
INSTALL iceberg;
LOAD iceberg;
```

After loading the extension, Iceberg tables can be queried using:

```sql
SELECT * FROM iceberg_scan('path/to/iceberg/table', allow_moved_paths = true);
```

## Known Issues and Rough Edges

- **Predicate pushdown:** Filtering conditions may not always be pushed down to the storage layer, potentially impacting query performance on large datasets.
- **Partitioning:** Partition pruning may not work optimally in all cases.
- **Metadata synchronization:** Manual helper functions may be required to ensure catalog and metadata are properly synced (see GitHub issue [#29](https://github.com/duckdb/duckdb_iceberg/issues/29)).

## Use Cases

- Querying Iceberg tables from a local development environment.
- Running analytical queries on medium-to-large Iceberg datasets (sub-terabyte) without distributed infrastructure.
- Performing CRUD operations on Iceberg tables using DuckDB's in-memory engine.

## Connections

- [[duckdb]] — The parent query engine.
- [[iceberg-query-engine-comparison]] — How DuckDB compares to other Iceberg query engines.
- [[data-lakehouse]] — DuckDB + Iceberg as a lightweight lakehouse pattern.
- [[predicate-pushdown]] — Optimization technique with known limitations in this extension.