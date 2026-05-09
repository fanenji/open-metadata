---
type: entity
title: DuckDB Spatial Extension Usage
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, spatial, extension, geometry, gis]
related: [duckdb, duckdb-geoparquet-workflow, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations]
sources: ["duckdb-geoparquet-tutorials.md"]
---
# DuckDB Spatial Extension Usage

Documentation of key DuckDB spatial extension functions and patterns for working with geospatial data, particularly in cloud-native workflows.

## Core Functions

- **`ST_GEOMFROMWKB(blob)`**: Converts Well-Known Binary geometry to DuckDB's spatial geometry type. Essential for working with GeoParquet files where geometry is stored as WKB.
- **`ST_AsWKB(geometry)`**: Converts DuckDB geometry back to WKB for export to formats that expect binary geometry.
- **`ST_AsWKT(geometry)`**: Converts geometry to Well-Known Text representation.

## GDAL FORMAT Output

DuckDB's spatial extension supports writing to over 50 GIS formats via GDAL drivers:

```sql
COPY (SELECT ...) TO 'output.fgb' WITH (FORMAT GDAL, DRIVER 'FlatGeobuf');
COPY (SELECT ...) TO 'output.geojson' WITH (FORMAT GDAL, DRIVER 'GeoJSON');
```

## Known Limitations

- No native GeoParquet output support — geometry is written as WKB, requiring external conversion.
- Spatial reference system (SRS) is not consistently set in output files.
- Progress reporting for remote file operations is inaccurate.

## Workarounds

- Use `gpq convert` to transform WKB Parquet to valid GeoParquet.
- Use `ogr2ogr -a_srs EPSG:4326` to fix missing SRS in output files.