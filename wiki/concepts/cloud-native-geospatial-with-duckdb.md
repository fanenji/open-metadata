---
type: concept
title: Cloud-Native Geospatial with DuckDB
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, geospatial, cloud-native-geospatial, geoparquet, httpfs]
related: [duckdb, duckdb-spatial-extension, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, geoparquet-vs-iceberg-metadata]
sources: ["DuckDB The Indispensable Geospatial Tool You Didn't Know You Were Missing.md"]
---
# Cloud-Native Geospatial with DuckDB

The pattern of using [[duckdb]] as a lightweight, embeddable query engine for cloud-native geospatial workflows. DuckDB enables direct querying of remote GeoParquet and Parquet files on S3 or HTTPS without data loading or server setup, leveraging the [[httpfs extension]] for range-request-based access.

## Key Characteristics

- **No Server Required**: DuckDB runs as a file-based, serverless database; the entire database is a single file on disk.
- **Remote File Support**: Query data directly from S3 or HTTPS using `read_parquet('s3://...')` or `select * from 'https://...'`.
- **Columnar Performance**: Columnar storage enables fast aggregations (e.g., sub-second `count(*)` on 800M rows) and efficient multi-core utilization.
- **Progressive Adoption**: Users can start with simple SQL queries on Parquet files and gradually adopt spatial operations.

## Workflow Pattern

1. **Access**: Load the `httpfs` and `spatial` extensions.
2. **Query**: Use SQL directly on remote Parquet files (e.g., `select * from 's3://bucket/*.parquet'`).
3. **Filter**: Apply spatial filters (e.g., `ST_Within`) and attribute filters.
4. **Materialize**: Optionally create local tables for faster repeated queries.
5. **Export**: Write results to Parquet or other formats via GDAL/OGR.

## Advantages Over Traditional Approaches

- **Vs. PostGIS**: Faster for analytical queries on large datasets; no server maintenance; easier setup.
- **Vs. Pandas**: No out-of-memory errors; uses disk when memory is exhausted; multi-core by default.
- **Vs. GDAL/OGR**: SQL interface instead of command-line; embedded GDAL avoids installation conflicts.

## Limitations

- Not suitable for OLTP or write-heavy workloads.
- Lacks spatial indexing (compensates with brute force and quadkeys).
- No native GeoParquet output (as of 2023).
- WASM version enables browser-based geospatial analytics.
