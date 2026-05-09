---
type: concept
title: DuckDB Vector Tile Generation
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, vector-tiles, mvt, mapping, geospatial]
related: [duckdb, duckdb-spatial-extension, geoparquet, cloud-native-geospatial-workflow, analytics-first-map-backend-pattern, mapbox-vector-tiles]
sources: ["DuckDB Geospatial Vector Tiles, Rasters, and Fast Maps on Parquet.md"]
---
# DuckDB Vector Tile Generation

DuckDB Vector Tile Generation is the pattern of producing Mapbox Vector Tiles (MVT) directly from DuckDB SQL queries over GeoParquet data, using the `ST_AsMVT` and `ST_AsMVTGeom` functions from the [[duckdb-spatial-extension]].

The core pattern involves a parameterized tile query where each HTTP tile request (`/tiles/{z}/{x}/{y}.mvt`) becomes a SQL query scoped to a small geographic extent. The query:
1. Computes the tile envelope in Web Mercator (EPSG:3857) using `ST_TileEnvelope`.
2. Projects source geometries to Web Mercator with `ST_Transform`.
3. Clips and encodes geometries with `ST_AsMVTGeom`.
4. Aggregates into MVT binary with `ST_AsMVT`.

A thin HTTP layer (Flask, FastAPI, Node) passes the z/x/y parameters into DuckDB and returns the MVT blob with the appropriate MIME type (`application/vnd.mapbox-vector-tile`).

This pattern enables fast, interactive web maps without a dedicated tile server or PostGIS cluster. The API surface may evolve as DuckDB's spatial extension matures.