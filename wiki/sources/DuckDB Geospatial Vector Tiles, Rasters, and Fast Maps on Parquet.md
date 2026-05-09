---
type: source
title: "DuckDB Geospatial: Vector Tiles, Rasters, and Fast Maps on Parquet"
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, geospatial, vector-tiles, rasters, mapping, parquet]
related: [duckdb, duckdb-spatial-extension, geoparquet, cloud-native-geospatial-workflow, duckdb-vector-tile-generation, duckdb-raster-tile-serving, analytics-first-map-backend-pattern, duckdb-geoparquet-limitations]
sources: ["DuckDB Geospatial Vector Tiles, Rasters, and Fast Maps on Parquet.md"]
authors: [Codastra]
year: 2025
url: "https://medium.com/@2nick2patel2/duckdb-geospatial-vector-tiles-rasters-and-fast-maps-on-parquet-f08ae70c73b8"
venue: Medium
---
# DuckDB Geospatial: Vector Tiles, Rasters, and Fast Maps on Parquet

This article by Codastra describes how to use DuckDB's spatial extension to build production-ready web maps directly from Parquet and GeoParquet files, without requiring a heavyweight GIS stack such as PostGIS, dedicated tile servers, or cache layers.

The core architectural pattern is that DuckDB serves as the compute layer over data stored in object storage (S3, GCS, local FS). Each tile request becomes a parameterized SQL query scoped to a small geographic extent, enabling millisecond execution. The article covers vector tile generation using `ST_AsMVT` and `ST_AsMVTGeom`, raster tile serving via GDAL integration with Cloud Optimized GeoTIFFs (COGs), and the "analytics-first" approach where geospatial is treated as just another analytic dimension alongside business metrics.

Key use cases include analytics-first map backends (store locators, delivery coverage, IoT sensors), mobility and transport dashboards (GPS trajectories, congestion analysis), and environmental/remote sensing analytics (combining raster tiles from COGs with vector layers). The article acknowledges that raster capabilities are not yet mature and that the vector tile generation API may evolve.