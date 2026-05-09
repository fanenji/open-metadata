---
type: concept
title: CRS Transformation Strategy
created: 2026-02-13
updated: 2026-02-13
tags: [geospatial, crs, transformation, postgis]
related: [postgis, postgis-crs-gridded-transformation, sdi-data-platform-integration, geospatial-etl-pipeline-iceberg]
sources: ["SDI Data Integration to Data Platform.md"]
---
# CRS Transformation Strategy

The approach to coordinate reference system (CRS) transformation for geospatial data being ingested from the SDI into the Data Platform. The target CRS is EPSG:7791 (RDN2008 / UTM zone 32N).

## Key Challenge

The transformation from source CRS (e.g., EPSG:3003 or EPSG:32632) to EPSG:7791 requires gridded data files for accurate conversion. These grid files are natively supported by PostGIS but are complex to manage in Spark/Python environments.

## Recommended Approach

The recommended strategy (Alternative B) keeps CRS transformation in PostGIS where gridded data is natively supported:

1. **Phase 1 (PostGIS)**: `ST_Transform(geometry, 7791)` using gridded data files installed on the database server
2. **Phase 2 (Spark/Python)**: Read already-transformed data from PostGIS via JDBC, export geometry as WKB/WKT

## Technical Implementation

- Spark JDBC query includes `ST_AsBinary(ST_Transform(geometry, 7791)) AS geom_wkb`
- PostGIS executes the transformation using native grid files
- Spark receives WKB and converts to appropriate format for GeoParquet/Iceberg
- Materialized Views can pre-compute transformed data for performance

## Alternatives Considered

- **In-Spark Transformation**: Complex and potentially unreliable due to grid file management
- **In-Geoscript Transformation**: Loses PostGIS optimizations, adds complexity to Geoscript
- **PostGIS Materialized View**: Pre-computes transformed data, reducing runtime load on PostGIS