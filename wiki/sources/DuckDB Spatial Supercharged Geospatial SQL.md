---
type: source
title: "DuckDB Spatial: Supercharged Geospatial SQL (GeoPython 2024)"
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, duckdb, spatial-sql, vectorized-execution]
related: [duckdb, duckdb-spatial-architecture, max-gabrielsson, duckdb-execution-model, cloud-native-geospatial-workflow, geoparquet-vs-iceberg-metadata]
sources: ["DuckDB Spatial Supercharged Geospatial SQL.md"]
---
# DuckDB Spatial: Supercharged Geospatial SQL (GeoPython 2024)

**Speaker:** [[Max Gabrielsson]] (DuckDB Labs)
**Event:** GeoPython 2024
**Published:** 2024-08-02
**Slides:** https://blobs.duckdb.org/papers/duckdb-spatial-geopython-2024.pdf

## Summary

This talk presents [[DuckDB]] as an embedded analytical SQL database and introduces the [[DuckDB Spatial]] extension. Max Gabrielsson covers DuckDB's vector-at-a-time execution model, its persistent storage format, and the "friendly SQL" user experience. The spatial extension is demonstrated using NYC taxi data, showing how it provides PostGIS-compatible functionality without external dependencies by statically bundling GDAL and PROJ. The talk also discusses limitations, future work (spatial indexes, GeoArrow integration), and community projects like [[QuackOSM]] and [[Ibis]].

## Key Points

- DuckDB's vector-at-a-time execution model balances memory efficiency and CPU utilization by processing rows in chunks sized for CPU cache.
- DuckDB is not just in-memory; it has a persistent database file format with ACID transactions, columnar storage, per-column statistics, and lightweight compression (3-5x savings).
- The in-process deployment model eliminates data transfer overhead and enables zero-copy interoperability with pandas, Polars, NumPy, and PyArrow.
- DuckDB Spatial provides 100+ ST functions modeled after PostGIS, statically bundles GDAL/PROJ, supports 3000+ CRS definitions, and ships pre-built binaries for 10+ platforms.
- The spatial extension is still maturing: missing spatial indexes, limited GeoArrow integration, and documentation gaps.
- DuckDB Spatial may be slower than pure GeoPandas for small in-memory datasets; its value proposition is for larger-than-memory or complex workflows.
- Raster support is experimental and may not fit DuckDB's vectorized execution model well due to large geometry sizes.

## Connections to Existing Wiki

- Extends [[duckdb]] with execution model details, storage architecture, and UX philosophy.
- Provides technical depth on [[duckdb-spatial-architecture]] (GDAL/PROJ bundling, CRS support).
- Demonstrates the [[cloud-native-geospatial-workflow]] pattern with DuckDB + remote Parquet + spatial operations.
- Relevant to [[geoparquet-vs-iceberg-metadata]] for understanding DuckDB's GeoParquet capabilities.
- Introduces [[max-gabrielsson]] as a key entity.