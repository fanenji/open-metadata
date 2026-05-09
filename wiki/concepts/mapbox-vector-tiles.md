---
type: concept
title: Mapbox Vector Tiles
created: 2026-04-04
updated: 2026-04-04
tags: [mvt, vector-tiles, mapping, geospatial, web-maps]
related: [duckdb-vector-tile-generation, duckdb-spatial-extension, analytics-first-map-backend-pattern]
sources: ["DuckDB Geospatial Vector Tiles, Rasters, and Fast Maps on Parquet.md"]
---
# Mapbox Vector Tiles

Mapbox Vector Tiles (MVT) are a modern tile format for web maps that encode geographic data as vector geometries rather than pre-rendered raster images. They enable dynamic styling, smooth zooming, and smaller file sizes compared to raster tiles.

In the context of DuckDB geospatial, MVT tiles are generated directly from SQL queries using the `ST_AsMVT` and `ST_AsMVTGeom` functions from the [[duckdb-spatial-extension]]. This enables serving interactive web maps from Parquet/GeoParquet data without a dedicated tile server or PostGIS cluster.

The MVT format is consumed by client-side rendering libraries such as MapLibre GL JS and Mapbox GL JS, which apply styling rules to the vector geometries on the client side.