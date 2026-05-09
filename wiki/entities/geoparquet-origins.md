---
type: entity
title: GeoParquet Origins
created: 2026-04-29
updated: 2026-04-29
tags: [geoparquet, parquet, geospatial, ogc, geoarrow]
related: [iceberg-v3-geo-types, geoparquet-vs-iceberg-metadata, spatial-predicate-pushdown, duckdb-iceberg-extension]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet - Summary.md"]
---
# GeoParquet Origins

GeoParquet was created to standardize how geospatial data is stored in Parquet files. It emerged from the convergence of two parallel efforts.

## The Two Parallel Efforts

1. **OGC initiative** — Javier Deator from Carto pushed for OGC engagement with cloud data warehouses. The pain point was the lack of a standard format to pass data between BigQuery, Snowflake, and Redshift.

2. **GeoArrow community** — Had already implemented GeoParquet/GeoArrow in R (geopandas) and was looking for a standard.

## Key Insight

BigQuery, Snowflake, and Redshift all support Parquet natively. If you standardize the geospatial metadata in Parquet, all three can interoperate without custom code — you don't need to convince mainstream data tools to support a "crazy new format."

## How GeoParquet Works

Parquet has a metadata system that allows attaching key-value metadata at the file and column level. GeoParquet uses this mechanism to store:
- CRS (Coordinate Reference System) definition
- Geometry encoding (WKB — Well-Known Binary)
- Bounding box / covering information
- Edge interpolation behavior (spherical vs. planar)

No changes to the Parquet file format itself — just standardized metadata conventions.

## Performance Characteristics

GeoParquet is approximately the size of a zipped shapefile — but you don't unzip it. Reading is much faster than any row-wise format. It is compact, fast, columnar, supports nesting, and is interoperable with all major data platforms.
