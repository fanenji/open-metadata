---
type: concept
title: Geometry Validation PostGIS
created: 2026-04-29
updated: 2026-04-29
tags: [gis, postgis, data-quality, geometry]
related: [airflow-geospatial-etl-pattern, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# Geometry Validation PostGIS

Geometry Validation PostGIS is a post-processing step in the Oracle-to-PostGIS spatial ETL pipeline that fixes invalid geometries after transfer. It ensures data quality by correcting polygons that fail PostGIS validity checks.

## Implementation

After ogr2ogr imports spatial data, the pipeline runs:

```sql
UPDATE {schema}.{table}
SET wkb_geometry = st_multi(st_collectionextract(st_makevalid(wkb_geometry), 3))
WHERE NOT ST_IsValid(wkb_geometry)
  AND ST_GeometryType(wkb_geometry) = 'ST_Polygon'
```

## Key Functions

- **ST_IsValid**: Checks if a geometry is valid according to OGC standards
- **ST_MakeValid**: Attempts to repair invalid geometries
- **ST_CollectionExtract**: Extracts components from a geometry collection (parameter 3 = polygons)
- **ST_Multi**: Converts single geometries to multi-geometries for consistency

## Importance

Oracle Spatial and PostGIS may have different geometry validation rules. Invalid geometries can cause:
- Query failures in downstream applications
- Incorrect spatial analysis results
- Performance degradation in spatial indexes

This step is critical for maintaining data quality in the geospatial cache.