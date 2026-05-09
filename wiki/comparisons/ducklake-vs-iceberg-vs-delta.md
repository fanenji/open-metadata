type: comparison
title: DuckLake vs Iceberg vs Delta Lake
created: 2026-04-29
updated: 2026-04-29
tags: [open-table-formats, comparison, lakehouse]
related: [ducklake, apache-iceberg, delta-lake, data-lakehouse, iceberg-query-engine-comparison, data-lakehouse-versioning-strategies]
sources: ["iceberg-built-a-maze-ducklake-just-handed-you-a-map.md"]
---
# DuckLake vs Iceberg vs Delta Lake

A comparison of three open table formats for data lakehouses, focusing on metadata architecture, performance characteristics, and operational properties.

## Comparison Table

| Property | Apache Iceberg | Delta Lake | DuckLake |
|----------|---------------|------------|----------|
| Metadata storage | JSON + Avro files on blob storage | Transaction log files on blob storage | SQL database (Postgres/MySQL/SQLite/DuckDB) |
| Metadata round trips | 6-10+ HTTP calls per query | 4-7 HTTP calls per query | 1 SQL query |
| Multi-table ACID | No (single-table only) | No (single-table only) | Yes — cross-table transactions |
| Small write handling | Produces many small files; needs compaction | Produces transaction log entries; needs OPTIMIZE | Optional inlining into catalog DB |
| Snapshot cost | Grows per snapshot; needs EXPIRE_SNAPSHOTS | Log entries accumulate; needs VACUUM | Rows in SQL table; cheap deletes |
| External catalog needed | Yes (Glue, Unity, Nessie, etc.) | Yes (Unity Catalog for cross-engine) | No — catalog is the SQL DB itself |
| Engine support | Spark, Flink, Trino, DuckDB, many more | Spark, Flink, Trino, some others | DuckDB today; spec is open for others |
| Data file compatibility | Parquet (standard) | Parquet (standard) | Parquet, Iceberg-compatible deletion files |
| Encryption | External / engine-level | External / engine-level | Native, key-managed by catalog |
| License | Apache 2.0 | Apache 2.0 (Linux Foundation) | MIT |
| Maturity | Production-grade, wide adoption | Production-grade within Databricks ecosystem | v0.1, early release |

## Key Architectural Differences

### Metadata Storage
Iceberg and Delta Lake store metadata as files on blob storage, requiring multiple network round trips to resolve table state. DuckLake stores all metadata in a SQL database, requiring a single SQL query.

### Snapshot Management
Iceberg snapshots accumulate in a growing root metadata file requiring periodic EXPIRE_SNAPSHOTS. Delta Lake transaction logs accumulate requiring VACUUM. DuckLake snapshots are SQL rows — adding is an insert, expiring is a delete.

### Small Write Handling
Iceberg and Delta Lake produce small files for every append, requiring compaction. DuckLake can inline small writes directly into the catalog database, bypassing Parquet writes.

## When to Choose Each

- **Iceberg:** Multi-engine environments, production-grade maturity, existing Spark/Flink/Trino pipelines
- **Delta Lake:** Databricks ecosystem, Unity Catalog integration, ML workflows
- **DuckLake:** DuckDB-native workflows, greenfield projects, teams wanting to eliminate compaction overhead