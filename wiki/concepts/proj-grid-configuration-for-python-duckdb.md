---
type: concept
title: PROJ Grid Configuration for Python and DuckDB
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, proj, crs, transformation, python, duckdb, gis]
related: [crs-transformation-strategies-for-geospatial-etl, geospatial-etl-hypothesis-comparison, postgis-as-staging-layer-for-geospatial-etl]
sources: ["ETL VETTORIALI SINTESI.md"]
---
# PROJ Grid Configuration for Python and DuckDB

The configuration requirements for PROJ grid files when performing CRS transformations (especially grid-based transformations like EPSG:7791) in Python/GeoPandas and DuckDB environments.

## Why PROJ Grid Configuration Matters

Grid-based CRS transformations (e.g., EPSG:7791) require PROJ grid files to achieve sub-meter accuracy. Unlike PostGIS, which has mature PROJ integration, Python and DuckDB environments require explicit configuration.

## Configuration Requirements

### Python/GeoPandas (PyProj)
- PROJ grid files must be available in the environment
- `PROJ_LIB` environment variable must point to the correct directory
- Grid files may need to be downloaded separately (not always bundled with PyProj)
- Configuration must be validated with test transformations

### DuckDB Spatial Extension
- DuckDB's spatial extension uses PROJ internally
- Grid files must be accessible to the DuckDB process
- Configuration may require setting PROJ environment variables before DuckDB initialization
- Less mature than PostGIS for grid-based transforms

## Risks
- Missing or incorrect grid files can cause silent accuracy degradation
- Grid file licensing may restrict distribution
- Environment-specific configuration can lead to inconsistent results across development, testing, and production

## Mitigation
- Validate CRS transformation accuracy with known test points
- Use Docker images with pre-configured PROJ grids
- Consider delegating CRS transformation to PostGIS (hypothesis 1d) to avoid this complexity