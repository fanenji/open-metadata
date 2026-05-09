---
type: source
title: DuckDB and Iceberg | Definite
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, iceberg, query-engine, lakehouse]
related: [duckdb-iceberg-extension, iceberg-query-engine-comparison, data-lakehouse, data-lakehouse-versioning-strategies]
sources: ["Duckdb and Iceberg  Definite.md"]
---
# DuckDB and Iceberg | Definite

**Source:** [https://www.definite.app/blog/iceberg-query-engine?s=09](https://www.definite.app/blog/iceberg-query-engine?s=09)

**Author:** Definite.app

**Published:** 2024-07-03

## Summary

This article evaluates DuckDB as a lightweight, open-source query engine for Apache Iceberg tables, comparing it to Snowflake, Spark, and Trino. It argues that DuckDB strikes a compelling balance between performance and operational simplicity for medium-to-large datasets (sub-terabyte). The article includes a detailed demo using 42 million rows of NYC Yellow Cab trip data on a MacBook M1 (32GB RAM), demonstrating sub-second to few-second query times for aggregations and joins. It acknowledges limitations for multi-terabyte datasets and rough edges between DuckDB and Iceberg, particularly around predicate pushdown and partitioning.

## Key Points

- DuckDB is open-source, single-machine, in-memory, and installable via `pip install duckdb`.
- DuckDB consistently ranks near the top of analytical benchmarks.
- The DuckDB Iceberg extension (`iceberg_scan()`) enables direct querying of Iceberg tables.
- DuckDB + Iceberg provides CRUD operations on static Parquet files, enabling database-like functionality.
- Rough edges exist between DuckDB and Iceberg, including predicate pushdown and partitioning issues.
- DuckDB is not suitable for very large (multi-terabyte) datasets due to memory constraints.
- The article positions DuckDB as a simpler alternative to Spark/Trino for teams without dedicated cluster management resources.

## Connections

- Strengthens the [[data-lakehouse]] concept by providing a concrete lightweight implementation pattern.
- Extends [[data-lakehouse-versioning-strategies]] by adding DuckDB as a query engine option.
- Related to [[dremio]] as an alternative Iceberg query engine.
- Related to [[elt-pattern]] for local/lightweight transformations.