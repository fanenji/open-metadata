---
type: concept
title: CRS Transformation Strategies for Geospatial ETL
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, etl, crs, coordinate-reference-system, gis, transformation]
related: [postgis-as-staging-layer-for-geospatial-etl, spark-for-geospatial-etl, geospatial-etl-hypothesis-comparison, proj-grid-configuration-for-python-duckdb, legacy-geospatial-etl-pipeline]
sources: ["ETL VETTORIALI SINTESI.md"]
---
# CRS Transformation Strategies for Geospatial ETL

Coordinate Reference System (CRS) transformation is the core technical challenge in the vector geospatial ETL pipeline. The target CRS is EPSG:7791, which requires grid-based transformations.

## Transformation Approaches

### 1. PostGIS ST_Transform (Recommended for Grid-Based CRS)
- **Location**: Transformation happens in PostGIS during JDBC reads
- **Technology**: PostGIS `ST_Transform` function
- **Advantages**: Optimal environment for grid-based transforms, mature PROJ integration, no additional configuration needed
- **Used in**: Hypothesis 1d (Spark)
- **Risk**: Potential PostGIS overload under concurrent reads

### 2. Python/PyProj Transformation
- **Location**: Transformation happens in Python worker
- **Technology**: PyProj library
- **Advantages**: Familiar Python stack, flexible
- **Disadvantages**: Requires impeccable PROJ grid configuration, single-node scalability limitation
- **Used in**: Hypotheses 1b, 2b

### 3. DuckDB Spatial/PROJ Transformation
- **Location**: Transformation happens in DuckDB
- **Technology**: DuckDB spatial extension with PROJ
- **Advantages**: Potentially fast, SQL-based
- **Disadvantages**: Requires PROJ grid configuration, single-node limitation
- **Used in**: Hypotheses 1c, 2c

### 4. GDAL/OGR Transformation
- **Location**: Transformation happens in GDAL/OGR
- **Technology**: GDAL's built-in CRS transformation
- **Advantages**: Mature, reliable, fast
- **Disadvantages**: Single-node limitation
- **Used in**: Hypotheses 1a, 2a

## Key Considerations
- **Grid-based transformations** (like EPSG:7791) require PROJ grid files to be correctly configured
- **PostGIS is the most reliable environment** for grid-based transforms due to its mature PROJ integration
- **Python/DuckDB environments** require explicit PROJ grid configuration, which must be validated via PoCs
- **Scalability**: Only Spark-based approaches can scale beyond single-node for the transformation step