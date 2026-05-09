---
type: concept
title: Spark for Geospatial ETL
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, etl, spark, big-data, iceberg, nessie, geoparquet]
related: [postgis-as-staging-layer-for-geospatial-etl, crs-transformation-strategies-for-geospatial-etl, geospatial-etl-hypothesis-comparison, geospatial-etl-pipeline-iceberg, nessie-catalog-versioning, iceberg-table-versioning, geoparquet-vs-iceberg-metadata]
sources: ["ETL VETTORIALI SINTESI.md"]
---
# Spark for Geospatial ETL

Apache Spark as the ETL engine for scalable geospatial data processing, particularly in the context of the vector ETL pipeline modernization.

## Role in Vector ETL

In hypothesis 1d, Spark is used in Phase 2 of the two-phase ETL pipeline:
- **Reads from PostGIS** via JDBC (where CRS transformation via `ST_Transform` has already been applied)
- **Writes to S3** as GeoParquet files (or optionally Iceberg tables)
- **Orchestrates scalable I/O** without performing CRS transformation itself

## Advantages

### Scalability
- Spark is the only evaluated technology that can scale beyond single-node
- Can handle large vector datasets (10M+ features) efficiently
- Distributed processing for both reads and writes

### Iceberg/Nessie Integration
- Spark has a mature Iceberg connector
- Can write directly to Iceberg tables with ACID transactions
- Supports Nessie catalog for Git-like versioning (branching, merging, atomic commits)
- Enables time travel, schema evolution, and query optimization

### Strategic Flexibility
- Can start with GeoParquet output and migrate to Iceberg with minimal code changes
- Changing `.write.format("parquet").save(path)` to `.write.format("iceberg").save(table_name)` is straightforward
- Configuration for Nessie catalog is a one-time setup

## Limitations
- **Infrastructure complexity**: Requires Spark cluster (e.g., on Kubernetes)
- **PostGIS bottleneck risk**: Concurrent JDBC reads may overload PostGIS
- **Not needed for small datasets**: Overkill for datasets that fit in single-node memory

## When to Use
- Large vector datasets (10M+ features)
- When Iceberg/Nessie integration is desired
- When scalability is a primary requirement
- When PostGIS can handle the JDBC read load