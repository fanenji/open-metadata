---
type: source
title: "DuckDB Spatial: Supercharged Geospatial SQL — Summary"
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, geospatial, spatial, sql, python, mapping]
related: [duckdb, duckdb-spatial-extension, duckdb-execution-model, duckdb-python-integration, duckdb-spatial-workflow, cloud-native-geospatial-workflow, geospatial-analytics-with-dbt, duckdb-geoparquet-limitations, duckdb-iceberg-extension, iceberg-geospatial-support, dremio-geospatial-limitations]
sources: ["DuckDB Spatial Supercharged Geospatial SQL - Summary.md"]
---
# DuckDB Spatial: Supercharged Geospatial SQL — Summary

**Speaker:** Max Gabrielsson, Software Engineer @ DuckDB Labs
**Event:** GeoPython 2024
**Video:** https://www.youtube.com/watch?v=hoyQnP8CiXE
**Slides:** https://blobs.duckdb.org/papers/duckdb-spatial-geopython-2024.pdf

## Overview

This talk presents DuckDB Spatial, the geospatial extension for DuckDB, covering the core architecture (vector-at-a-time execution, columnar storage, in-process deployment), Python integration (three APIs, zero-copy dataframe interoperability), and a complete geospatial workflow demo using 1 million NYC taxi rides. The extension provides 100+ ST_ functions, 3000+ built-in CRS definitions, and bundled GDAL/PROJ dependencies with no runtime configuration.

## Key Takeaways

- DuckDB is not an in-memory database; it has proper columnar on-disk storage with compression (3-5× reduction) and ACID transactions
- The vector-at-a-time execution model balances row-at-a-time and column-at-a-time tradeoffs, processing chunks sized for CPU cache
- Graceful degradation spills to disk when out of RAM instead of crashing
- Zero-copy dataframe interoperability with Pandas, Polars, NumPy, and PyArrow
- The spatial extension is PostGIS-compatible with full 3D support (Z, M, ZM)
- No runtime dependencies — GDAL and PROJ are statically bundled
- Spatial indexes are planned but not yet available
- Raster support is experimental and faces fundamental challenges with the vectorized execution model
- For datasets fitting in RAM, GeoPandas alone is comparably fast; DuckDB Spatial's advantage grows with larger data and complex multi-join queries

## Related Projects

- QuackOSM (Camille Rochette) — OSM data with DuckDB
- IBIS (Voltron Labs) — universal database interface with DuckDB Spatial expression support
- GEOG 414 (Prof. Krishanu Sankar) — free spatial data management course
