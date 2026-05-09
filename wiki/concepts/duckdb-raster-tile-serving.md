---
type: concept
title: DuckDB Raster Tile Serving
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, rasters, cog, gdal, geospatial, mapping]
related: [duckdb, duckdb-spatial-extension, gdal, cloud-native-geospatial-workflow, analytics-first-map-backend-pattern]
sources: ["DuckDB Geospatial Vector Tiles, Rasters, and Fast Maps on Parquet.md"]
---
# DuckDB Raster Tile Serving

DuckDB Raster Tile Serving is the pattern of serving raster map tiles (e.g., satellite imagery, NDVI, heatmaps) through DuckDB using GDAL integration and Cloud Optimized GeoTIFFs (COGs) stored in object storage.

The emerging pattern involves:
1. Storing imagery as COGs in object storage (S3, GCS).
2. Maintaining a footprint/metadata table in Parquet or DuckDB with raster ID, path, bounding box, resolution, and band info.
3. For each map request, finding overlapping rasters via `ST_Intersects` on the footprints, then using GDAL-backed functions to read only the tile-sized window from each raster.
4. Optionally computing indices (e.g., NDVI) or color ramps, and serving as PNG/JPEG tiles or derived vector contours.

**Important caveat**: This capability is not yet mature. The article describes a "simplified SQL-ish pseudo-interface" (`ST_RenderRasterTile`) that is aspirational rather than a real, stable function. Raster support is significantly less developed than vector tile generation in DuckDB's spatial extension.