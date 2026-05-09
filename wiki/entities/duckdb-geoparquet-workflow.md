---
type: entity
title: DuckDB GeoParquet Workflow
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, geoparquet, workflow, spatial, cloud-native]
related: [cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, duckdb-spatial-extension-usage, duckdb, geoparquet-vs-iceberg-metadata]
sources: ["duckdb-geoparquet-tutorials.md"]
---
# DuckDB GeoParquet Workflow

A structured pattern for using DuckDB to query, transform, and export cloud-hosted GeoParquet datasets. This workflow consolidates the techniques demonstrated in the DuckDB and GeoParquet tutorial into a repeatable process.

## Workflow Steps

1. **Setup**: Install DuckDB, load `spatial` and `httpfs` extensions, configure S3 region.
2. **Stream query**: Use glob patterns (`*.parquet`) on S3 URLs to select and query partitioned data directly.
3. **Convert WKB to geometry**: Use `ST_GEOMFROMWKB(geometry)` to create spatial types from binary geometry columns.
4. **Create local table**: Optionally persist data locally with `CREATE TABLE ... AS SELECT ...` for faster repeated access.
5. **Export**: Use `COPY ... TO ... WITH (FORMAT GDAL, DRIVER '...')` to write to GIS formats (FlatGeobuf, GeoJSON, etc.).
6. **Post-process**: Use `gpq convert` for valid GeoParquet output, and `ogr2ogr -a_srs EPSG:4326` to fix missing SRS.

## Key SQL Patterns

```sql
-- Direct S3 query with filter
SELECT * FROM 's3://bucket/path/*.parquet' WHERE area_in_meters > 1000;

-- Create local table with geometry conversion
CREATE TABLE my_table AS 
SELECT * EXCLUDE geometry, ST_GEOMFROMWKB(geometry) AS geometry 
FROM 's3://bucket/path/*.parquet';

-- Export to FlatGeobuf
COPY (SELECT * EXCLUDE geometry, ST_AsWKB(geometry) AS geometry FROM my_table)
TO 'output.fgb' WITH (FORMAT GDAL, DRIVER 'FlatGeobuf');
```

## Limitations

- No native GeoParquet output — requires external `gpq` tool.
- SRS not consistently set — requires `ogr2ogr -a_srs EPSG:4326`.
- Progress reporting inaccurate for remote files.