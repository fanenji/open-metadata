---
type: concept
title: PostGIS as Staging Layer for Geospatial ETL
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, etl, postgis, staging, architecture, sdi]
related: [crs-transformation-strategies-for-geospatial-etl, spark-for-geospatial-etl, geospatial-etl-hypothesis-comparison, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["ETL VETTORIALI SINTESI.md"]
---
# PostGIS as Staging Layer for Geospatial ETL

The pattern of using PostGIS as an intermediate validated storage layer between source systems (Oracle) and the Data Platform (S3/GeoParquet/Iceberg).

## Architecture

### Two-Phase ETL with PostGIS Staging
1. **Phase 1 (Ingestion)**: Oracle → PostGIS via Geoscript/ogr2ogr
   - Transfers raw vector data from legacy Oracle database
   - Validates geometry integrity during ingestion
   - Maintains SDI compatibility

2. **Phase 2 (Transformation & Output)**: PostGIS → S3
   - CRS transformation (EPSG:7791) via `ST_Transform` in PostGIS (optimal)
   - Output as GeoParquet files on S3
   - Optional Iceberg/Nessie integration via Spark

### Benefits
- **Validated staging**: Data quality checks before final output
- **SDI compatibility**: Maintains alignment with existing Spatial Data Infrastructure
- **Optimal CRS transformation**: PostGIS is the ideal environment for grid-based transforms
- **Separation of concerns**: Ingestion and output phases are independent

### Drawbacks
- **Latency**: Two-phase pipeline adds processing time
- **Storage overhead**: Intermediate storage in PostGIS
- **Potential bottleneck**: PostGIS may become overloaded during Phase 2 reads

## When to Use
- When SDI compatibility is a requirement
- When grid-based CRS transformation is needed (e.g., EPSG:7791)
- When data validation before final output is critical
- When the latency of two phases is acceptable

## When to Bypass
- When latency is the primary concern
- When PostGIS infrastructure is not available or too expensive
- When data validation can be performed in the output pipeline