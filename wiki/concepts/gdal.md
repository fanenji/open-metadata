---
type: concept
title: GDAL
created: 2026-04-04
updated: 2026-04-04
tags: [gdal, geospatial, raster, vector, library]
related: [duckdb-spatial-extension, duckdb-raster-tile-serving, geoparquet]
sources: ["DuckDB Geospatial Vector Tiles, Rasters, and Fast Maps on Parquet.md"]
---
# GDAL

GDAL (Geospatial Data Abstraction Library) is a powerful open-source library for reading and writing raster and vector geospatial data formats. It is used under the hood by the [[duckdb-spatial-extension]] to provide format support and raster operations.

In the context of DuckDB geospatial, GDAL integration enables:
- Reading vector formats (Shapefile, GeoJSON, etc.) via table functions.
- Managing satellite imagery and raster operations through the spatial extension.
- The emerging [[duckdb-raster-tile-serving]] pattern, where GDAL reads only the necessary window from Cloud Optimized GeoTIFFs (COGs) to serve raster map tiles.