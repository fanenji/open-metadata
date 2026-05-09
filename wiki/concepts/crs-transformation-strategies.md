---
type: concept
title: CRS Transformation Strategies for Geospatial ETL
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, crs, transformation, etl, postgis, spark, sedona]
related: [apache-sedona, postgis-performance-tuning-for-etl, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline, dremio-geospatial-limitations, duckdb]
sources: ["ETL VETTORIALI.md"]
---
# CRS Transformation Strategies for Geospatial ETL

This concept page documents the decision framework for where and how to perform Coordinate Reference System (CRS) transformations in the geospatial vector ETL pipeline, specifically for transforming data to EPSG:7791 (RDN2008 / UTM zone 32N).

## Transformation Locations

### 1. PostGIS (via JDBC Query)
The transformation is performed by PostGIS during a JDBC read using `ST_Transform(geometry, target_srid)`. This is the most reliable approach for grid-based transformations because PostGIS has native access to PROJ grid files.

**Pros:**
- Correct grid file handling (NTv2, `.gsb` files)
- No need to manage grid files in Spark/Python environments
- Leverages PostGIS's robust implementation

**Cons:**
- Performance bottleneck on PostGIS during reads
- Requires careful server tuning and monitoring
- May need Materialized Views for acceptable performance

### 2. Apache Sedona (in Spark)
Transformation is performed within Spark using Sedona's spatial functions after reading raw geometries.

**Pros:**
- Distributed processing, scales horizontally
- Single pipeline end-to-end in Spark

**Cons:**
- Sedona does not natively handle PROJ grid files
- Complex configuration required for grid-based transformations
- May produce inaccurate results without proper grid setup

### 3. Python/GeoPandas (with PyProj)
Transformation is performed in a Python script using GeoPandas' `.to_crs()` method, which uses PyProj/PROJ.

**Pros:**
- Familiar Python stack
- PyProj handles grid files correctly if configured

**Cons:**
- Single-node processing, limited scalability
- Requires careful PROJ configuration (PROJ_LIB, grid file paths)
- Complex Iceberg integration

### 4. DuckDB (with Spatial Extension)
Transformation is performed using DuckDB's `ST_Transform` function from the spatial extension.

**Pros:**
- Efficient single-node processing
- SQL-based, familiar syntax

**Cons:**
- Single-node, limited scalability
- Requires PROJ/grid configuration in the DuckDB environment

## Decision Matrix

| Strategy | Accuracy | Scalability | Complexity | Grid Support |
|----------|----------|-------------|------------|--------------|
| PostGIS (ST_Transform) | High | Limited by DB | Low | Native |
| Spark/Sedona | Medium | High | High | Limited |
| Python/GeoPandas | High | Low | Medium | Configurable |
| DuckDB | High | Low | Medium | Configurable |

## Recommendation

For the initial implementation, **delegate CRS transformation to PostGIS** via JDBC queries with `ST_Transform`. This ensures correct grid file handling and avoids complex configuration in the DP environment. If performance becomes a bottleneck, consider:

1. **Materialized Views** in PostGIS with pre-transformed geometries.
2. **PoC validation** of Sedona's grid file handling for potential future migration to a fully Spark-based pipeline.

## Related
- [[apache-sedona]] — The Spark geospatial library used for alternative transformation approaches.
- [[postgis-performance-tuning-for-etl]] — Mitigation strategies for PostGIS bottlenecks.
- [[geospatial-etl-pipeline-iceberg]] — The overall ETL pipeline pattern.
- [[dremio-geospatial-limitations]] — Dremio's limited native GEO support, relevant for querying transformed data.