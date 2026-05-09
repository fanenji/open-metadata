---
type: entity
title: DuckDB Spatial Extension
created: 2026-04-04
updated: 2026-05-07
tags:
  - duckdb
  - geospatial
  - spatial-extension
  - gdal
  - spatial
  - extension
  - geos
  - proj
  - geopandas
related:
  - duckdb
  - geoparquet
  - duckdb-vector-tile-generation
  - duckdb-raster-tile-serving
  - cloud-native-geospatial-workflow
  - gdal
  - duckdb-execution-model
  - duckdb-python-integration
  - duckdb-spatial-workflow
  - postgis
  - proj
  - geopandas
  - quackosm
  - ibis
  - duckdb-geoparquet-limitations
  - cloud-native-geospatial-with-duckdb
  - geoparquet-vs-iceberg-metadata
  - geospatial-etl-pipeline-iceberg
sources: ["DuckDB Geospatial Vector Tiles", "Rasters", "and Fast Maps on Parquet.md", "DuckDB Spatial Supercharged Geospatial SQL - Summary.md", "DuckDB The Indispensable Geospatial Tool You Didn't Know You Were Missing.md", "DuckDb.md", "DuckDB Geospatial Vector Tiles, Rasters, and Fast Maps on Parquet.md"]
---
# DuckDB Spatial Extension

The DuckDB Spatial extension is the official DuckDB extension for geospatial data processing. Modeled after [[PostGIS]], it adds geospatial capabilities to [[duckdb]] via a compiled module (plugin) downloadable and loadable at runtime. The extension leverages [[GEOS]] (the same spatial engine used by PostGIS) for core spatial operations like comparisons and joins, and [[GDAL/OGR]] for reading and writing a wide variety of geospatial formats. It provides a GEOMETRY type, a PostGIS-like set of `ST_` functions, table functions for reading vector formats, and integration with GDAL, PROJ, and GEOS under the hood. It works seamlessly with DuckDB’s SQL engine and other extensions, and provides spatial indexing support via quadkey-based optimization.

## Installation

```sql
INSTALL spatial;
LOAD spatial;
```

Pre-built binaries are available for Windows, Linux, macOS (including ARM), and WebAssembly.

Once loaded, the extension can be used for querying GeoParquet files, performing spatial joins, and transforming coordinate reference systems.

## Core Capabilities

- **Simple Features geometry type** — points, linestrings, polygons, multi-geometries, geometry collections
- **100+ `ST_` functions** (counting overloads) — covering most of what PostGIS offers
- **Full 3D support** — Z, M, and ZM coordinate dimensions, including intersection and all standard geometric operations
- **3,000+ built-in CRS definitions** — the entire default PROJ database is embedded; no local PROJ installation needed
- **GDAL/OGR integration** — reads any GDAL-supported spatial format (shapefiles, GeoJSON, GeoPackage, etc.) via `ST_Read()`, and enables raster tile serving from Cloud Optimized GeoTIFFs (COGs) in object storage
- **No runtime dependencies** — GDAL, PROJ, and GEOS are statically bundled into the binary; no version conflicts with local installs
- **WKT/WKB Conversion** — easy conversion between Well Known Text, Well Known Binary, and geometry columns
- **Coordinate Reprojection** — `ST_Transform(geom, src_crs, dst_crs)` for reprojecting between coordinate reference systems
- **Seamless Integration** — works with DuckDB’s SQL engine and other extensions
- **Spatial Indexing** — provides indexing performance via quadkey-based optimization; full spatial indexes (e.g., R-tree) are planned but not yet available

## Key Functions

- `ST_Point(lon, lat)` — create a point geometry
- `ST_Transform(geom, src_crs, dst_crs)` — reproject between coordinate reference systems
- `ST_Distance(geom1, geom2)` — compute distance between geometries
- `ST_Within(geom1, geom2)` — test if one geometry is within another
- `ST_Intersects(geom1, geom2)` — test if geometries intersect
- `ST_Read(path)` — read any GDAL-supported spatial format
- `ST_Drivers()` — list available GDAL drivers
- `ST_AsText(geom)` — convert geometry to WKT for interoperability
- `ST_AsWKB(geom)` — convert geometry to WKB for binary transfer
- `ST_AsMVT(geom, ...)` — aggregate geometries into Mapbox Vector Tiles
- `ST_AsMVTGeom(geom, ...)` — clip and transform a geometry to MVT tile coordinates

## Limitations

- **No spatial indexes** — a significant limitation compared to PostGIS for production workloads; brute-force performance with quadkey-based optimization is used (planned but no timeline)
- **No persistent CRS** — geometry columns do not carry projection information; users must manually specify source and target CRS for transformations (automatic propagation is planned)
- **No native GeoParquet output** — cannot write GeoParquet directly; workaround is to write "compatible" Parquet and fix with GPQ (future support planned)
- **Raster support is experimental** — the vectorized execution model creates fundamental challenges (e.g., 2 GB per vector batch for 512×512×4 band rasters)
- **Visualization requires external libraries** — geometry must be converted to WKT and then to GeoPandas for plotting; GeoArrow integration (enabling zero-copy) is future work
- **Maturity gap** — fewer spatial operations than mature databases like PostGIS; development is ongoing

## Use Cases

- **Vector tile generation** — `ST_AsMVT` and `ST_AsMVTGeom` enable direct production of Mapbox Vector Tiles (MVT) from SQL queries over GeoParquet.
- **Raster tile serving** — GDAL integration allows windowed reads from Cloud Optimized GeoTIFFs (COGs), serving raster tiles from object storage.
- **Parameterized tile queries** — each tile request (z/x/y) becomes a scoped SQL query that executes in milliseconds.
- **Analytics-first map backend** — the extension enables the [[analytics-first-map-backend-pattern]], where geospatial is treated as just another analytic dimension alongside business metrics, avoiding separate GIS infrastructure.

## Future Directions

According to extension author Max Gabrielsson, development priorities include:
- **Native GeoParquet output** — direct writing of GeoParquet files
- **Better CRS handling** — persistent CRS on geometry columns and automatic propagation
- **Spatial indices** — to improve spatial join performance
- **GeoArrow integration** — enabling zero-copy vectorized access to spatial data

These developments are partially dependent on funded contracts.

## Related Projects

- [[quackosm]] — OSM data with DuckDB (Camille Rochette)
- [[ibis]] — universal database interface with DuckDB Spatial expression support (Noel Mani)
- [[geospatial-etl-pipeline-iceberg]] — multi-step ETL pattern for spatial data
- GEOG 414 — free spatial data management course (Prof. Krishanu Sankar)