---
type: concept
title: DuckDB Spatial Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, spatial, gis, architecture]
related: [duckdb, duckdb-execution-model, cloud-native-geospatial-workflow, geoparquet-vs-iceberg-metadata]
sources: ["DuckDB Spatial Supercharged Geospatial SQL.md"]
---
# DuckDB Spatial Architecture

DuckDB Spatial is an official extension for [[DuckDB]] that adds geospatial capabilities via a Simple Features vector geometry type (points, polygons, linestrings). It is modeled after [[PostGIS]] and provides 100+ ST functions.

## Technical Architecture

- **No runtime dependencies:** GDAL and PROJ are statically bundled into the extension binary, avoiding conflicts with locally installed versions.
- **CRS support:** The entire default PROJ prediction database is embedded, recognizing over 3,000 common CRS definitions out of the box.
- **Cross-platform:** Pre-built binaries are shipped for 10+ platforms including Windows, Linux, macOS, and WebAssembly.
- **Extension loading:** Loaded at runtime via `INSTALL spatial; LOAD spatial;` with no other setup required.

## Integration with DuckDB Core

- Spatial operations leverage DuckDB's vectorized execution model, though large geometries (e.g., rasters) can be challenging because the standard vector size of 248 elements can result in very large memory footprints.
- GDAL integration is exposed through table functions like `ST_Read()` for reading spatial data formats (shapefiles, GeoJSON, etc.) and `ST_Drivers()` for listing available drivers.

## Limitations and Future Work

- **Spatial indexes:** Not yet implemented; planned for future releases.
- **Projection handling:** Currently requires manual juggling of CRS information; improved handling is planned.
- **GeoArrow integration:** Limited; currently geometries must be converted to WKT for interoperability with GeoPandas. Better GeoArrow support is planned.
- **Documentation:** Acknowledged as lacking; a new documentation system is underway.
- **Raster support:** Experimental third-party contribution exists, but rasters may not fit well with DuckDB's vectorized execution model due to large per-element sizes.

## Related

- [[duckdb-execution-model]] — The underlying execution model that spatial operations run on
- [[cloud-native-geospatial-workflow]] — Pattern for using DuckDB Spatial with remote GeoParquet
- [[geoparquet-vs-iceberg-metadata]] — GeoParquet interoperability considerations