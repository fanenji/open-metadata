---
type: concept
title: Geospatial ETL Pipeline for Iceberg
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, etl, iceberg, pipeline, duckdb]
related: [duckdb, cloud-native-geospatial-workflow, geoparquet-vs-iceberg-metadata, duckdb-iceberg-extension]
sources: ["duckdb geoparquet tutorials.md"]
---
# Geospatial ETL Pipeline for Iceberg

Multi-step ETL pattern for ingesting spatial data into Apache Iceberg tables. The traditional pipeline uses GDAL → GeoParquet → Spark → Iceberg, but [[DuckDB]] offers a simpler alternative for many use cases.

## DuckDB as an Alternative to Spark

The [[cloud-native-geospatial-workflow]] documented in the DuckDB GeoParquet tutorial demonstrates a lightweight approach: query remote GeoParquet files directly from S3 using DuckDB, transform geometry with the `spatial` extension, and output to local formats. This avoids the complexity of Spark clusters for smaller to medium-scale geospatial ETL tasks.

### When to Use DuckDB vs Spark
- **DuckDB**: Suitable for single-machine workflows, ad-hoc queries, and datasets that fit within memory or local storage. Simpler setup and faster iteration.
- **Spark**: Required for distributed processing of very large datasets (terabytes+), complex multi-stage pipelines, or when native Iceberg writing with GeoParquet is needed.

### Current Limitations
- DuckDB cannot natively write valid GeoParquet output, requiring the `gpq` CLI tool for conversion.
- For production Iceberg ingestion at scale, Spark remains the more mature and feature-complete option.

For a detailed comparison of query engines for Iceberg, see [[iceberg-query-engine-comparison]].