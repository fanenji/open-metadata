---
type: entity
title: PostGIS
created: 2024-05-22
updated: 2026-05-07
tags: ["database", "spatial-extension", "geospatial", "postgresql", "gis", "crs-transformation", "postgis", "spatial-database"]related:
  - automated-geometry-validation
  - legacy-geospatial-etl-pipeline
  - oracle-to-postgresql-gdal-etl
  - geospatial-etl-pipeline-iceberg
  - postgis-as-staging-layer-for-geospatial-etl
  - crs-transformation-strategies-for-geospatial-etl
  - spark-for-geospatial-etl
  - duckdb
  - dbt
  - h3-geospatial-indexing
  - postgis-as-central-hub
  - duckdb-postgis-integration
  - modern-geospatial-data-stack
  - cloud-native-geospatial-workflow
sources:
  - "CONVERSION_GROOVY -> PYTHON.md"
  - "ETL VETTORIALI SINTESI.md"
  - "spatial-sql-the-modern-data-stack-and-postgis.md"
related: ["automated-geometry-validation", "legacy-geospatial-etl-pipeline", "oracle-to-postgresql-gdal-etl", "geospatial-etl-pipeline-iceberg", "postgis-as-staging-layer-for-geospatial-etl", "crs-transformation-strategies-for-geospatial-etl", "spark-for-geospatial-etl", "duckdb", "dbt", "h3-geospatial-indexing", "postgis-as-central-hub", "duckdb-postgis-integration", "modern-geospatial-data-stack", "cloud-native-geospatial-workflow"]
---
# PostGIS

PostGIS is a spatial database extension for PostgreSQL that adds support for geographic objects and spatial queries. It is the most mature and feature-rich open-source spatial database, providing hundreds of spatial functions, raster support, and integration with a wide ecosystem of tools. In the Data Platform, PostGIS serves as the primary destination for spatial data and as a critical staging and transformation layer for vector geospatial ETL pipelines.

## Role in the Modern Geospatial Data Stack

As argued by [[Matt Forrest]] in his talk "Spatial SQL, the Modern Data Stack, and PostGIS," PostGIS acts as the central hub connecting a variety of modern tools:

- **[[DuckDB]]** — via the DuckDB Foreign Data Wrapper for hybrid processing (DuckDB handles bulk/long data, PostGIS handles complex spatial analysis)
- **[[dbt]]** — via the dbt-postgres connector for automated spatial data pipeline orchestration
- **[[h3-geospatial-indexing]]** — via H3 extension for efficient polygon polyfill and string-based spatial joins
- **Remote rasters** — via Cloud-Optimized GeoTIFF (COG) reading from S3/STAC endpoints
- **Output tools** — QGIS, GeoPandas, Leafmap for visualization and analysis

## Role in Vector ETL

PostGIS is central to the vector ETL modernization, particularly in migrating from legacy Oracle systems. The key architectural decision is whether to use PostGIS as a validated staging layer (two-phase ETL) or to bypass it (one-phase ETL).

### PostGIS as Staging Layer (Two-Phase ETL)
- **Phase 1**: Oracle → PostGIS (via Geoscript/ogr2ogr)
- **Phase 2**: PostGIS → S3 (via Spark, Python, DuckDB, or GDAL)
- **Benefits**: Validated intermediate storage, SDI compatibility, optimal environment for grid-based CRS transformation via `ST_Transform`
- **Drawback**: Adds latency due to two phases

### CRS Transformation with ST_Transform
PostGIS's `ST_Transform` function is the optimal environment for grid-based CRS transformations (e.g., EPSG:7791). In hypothesis 1d (Spark), CRS transformation is delegated to PostGIS during JDBC reads, leveraging PostGIS's mature grid support while using Spark only for scalable I/O.

## Key Capabilities

- **Spatial functions**: Including `ST_IsValid`, `ST_GeometryType`, `ST_Transform` for coordinate transformations, and `ST_Intersects` for performant spatial joins.
- **Raster support**: The most comprehensive raster functions among spatial databases.
- **H3 polyfill**: The H3 extension provides "incredibly fast" and "most efficient" polygon-to-hex conversion.
- **Foreign Data Wrappers**: Connect to external data sources (DuckDB, other databases) as foreign tables.
- **Full-Text Search**: Can be combined with spatial data for text-based classification (e.g., flash flood event narratives).

## Architecture Patterns

### Hybrid Modern Stack
The modern recommendation is a hybrid approach:
1. Use DuckDB for bulk CSV processing, remote file reading, and large-scale joins on non-spatial data.
2. Use PostGIS for complex spatial analysis, raster processing, and H3 aggregation.
3. Use dbt to orchestrate the pipeline end-to-end.

### Two-Phase ETL for Legacy Migration
In the context of migrating from Oracle, the two-phase pattern (Oracle → PostGIS → S3) provides validated intermediate storage and leverages PostGIS's mature CRS transformation capabilities.

## Related

- [[automated-geometry-validation]]
- [[legacy-geospatial-etl-pipeline]]
- [[oracle-to-postgresql-gdal-etl]]
- [[geospatial-etl-pipeline-iceberg]]
- [[postgis-as-staging-layer-for-geospatial-etl]]
- [[crs-transformation-strategies-for-geospatial-etl]]
- [[spark-for-geospatial-etl]]
- [[duckdb]]
- [[dbt]]
- [[h3-geospatial-indexing]]
- [[postgis-as-central-hub]]
- [[duckdb-postgis-integration]]
- [[modern-geospatial-data-stack]]
- [[cloud-native-geospatial-workflow]]