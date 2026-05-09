---
type: concept
title: DuckDB-Iceberg Limitations
created: 2025-02-10
updated: 2025-02-10
tags: [duckdb, iceberg, limitations, data-architecture]
related: [duckdb, iceberg, duckdb-iceberg-sufficiency, single-user-database-limitation, predicate-pushdown-iceberg, iceberg-catalog-read-support, duckdb-iceberg-write-support]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# DuckDB-Iceberg Limitations

A focused summary of the key limitations of using [[duckdb]] with [[iceberg]] tables, as identified in community discussions and practical experience.

## Missing Iceberg Catalog Read Support

DuckDB cannot read Iceberg Catalogs natively. This limits its ability to discover and manage Iceberg tables through the standard catalog interface. Workarounds involve using [[PyIceberg]] to handle catalog operations and pass data to DuckDB via [[PyArrow]].

## Missing Native Iceberg Write Support

DuckDB does not support writing to Iceberg tables directly. Transformations must output to intermediate formats (Parquet, Arrow) and then be written to Iceberg using other tools (PyIceberg, Spark).

## Poor Predicate Pushdown

DuckDB's predicate pushdown for Iceberg files is inefficient. When querying large Iceberg datasets on S3, DuckDB may scan more data than necessary, leading to poor performance and higher S3 request costs.

## Single-User Design

DuckDB is designed as a single-user, in-process database. Multiple concurrent users or applications cannot safely write to the same DuckDB instance. While reading Iceberg files on shared S3 is possible, concurrent writes require careful orchestration.

## No RBAC or Column-Level Security

DuckDB lacks built-in role-based access control and column-level security. Access control must be delegated to the storage layer (IAM policies on S3) or handled at the application level.

## Performance Degradation at Scale

Beyond a few TB, DuckDB's single-node architecture shows unpredictable performance degradation. Unlike cloud warehouses, there are no built-in query profiling tools to diagnose issues like spilling or inefficient pruning.

## Mitigation Strategies

- Use [[PyIceberg]] + [[PyArrow]] as an intermediate layer for catalog operations and writes.
- Use [[dlthub]] for ingestion into the bronze layer.
- Limit DuckDB to transformation steps within Python pipelines, not as a multi-user query engine.
- Plan for migration to a dedicated warehouse if data volume grows beyond 2-3 TB.