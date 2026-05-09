---
type: source
title: DuckDB and GeoParquet Tutorial
created: 2026-04-08
updated: 2026-04-29
tags: [duckdb, geoparquet, spatial, tutorial, cloud-native]
related: [cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, duckdb-spatial-extension-usage, duckdb-geoparquet-workflow, duckdb]
sources: ["duckdb-geoparquet-tutorials.md"]
authors: [cholmes]
year: 2026
url: "https://github.com/cholmes/duckdb-geoparquet-tutorials"
venue: GitHub
---
# DuckDB and GeoParquet Tutorial

A practical tutorial demonstrating how to use DuckDB with its spatial and httpfs extensions to query, transform, and export cloud-hosted GeoParquet datasets. The tutorial uses Google Open Buildings data hosted on source.coop as a running example, covering S3 streaming, WKB-to-geometry conversion, table creation, and export to various GIS formats.

## Key Techniques

- **Direct S3 streaming**: Querying partitioned Parquet files directly on S3 using glob patterns without local persistence.
- **WKB conversion**: Using `ST_GEOMFROMWKB()` to convert binary geometry columns to DuckDB spatial types.
- **Format export**: Writing to FlatGeobuf, GeoParquet, and other formats via DuckDB's GDAL FORMAT output.
- **Multi-file aggregation**: Using `*` glob patterns to select multiple partitioned Parquet files as a single table.

## Limitations Acknowledged

- DuckDB does not natively output valid GeoParquet; requires external tool (gpq) for conversion.
- Spatial reference system (SRS) is not consistently set in output; requires ogr2ogr for cleanup.
- Progress reporting is inaccurate for remote files.

## Connections

This tutorial provides concrete implementation details for the [[cloud-native-geospatial-workflow]] pattern and extends the documented [[duckdb-geoparquet-limitations]] with specific workarounds. It is closely related to [[duckdb]] and [[duckdb-iceberg-extension]] as a practical usage guide for the same tool with a different data format.