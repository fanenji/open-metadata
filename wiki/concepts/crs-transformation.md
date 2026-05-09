---
type: concept
title: CRS Transformation
created: 2026-03-18
updated: 2026-03-18
tags: [sdi, geospatial, coordinate-systems, transformation, data-quality]
related: [sdi-spatial-data-infrastructure, ogc-standards, inspire-directive, sdi-dp-integration-patterns, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline]
sources: ["Integrazione SDI e Data Platform.md"]
---
# CRS Transformation

Coordinate Reference System (CRS) transformation is the process of converting geographic coordinates from one reference system to another. It is a critical technical challenge in integrating Spatial Data Infrastructures (SDI) with Data Platforms (DP), as geospatial data from different sources often uses different coordinate systems.

## Common CRS Types

- **Geographic CRS**: Uses latitude/longitude (e.g., WGS84, ETRS89)
- **Projected CRS**: Uses Cartesian coordinates (e.g., UTM zones, national grid systems)
- **Local CRS**: Custom systems for specific regions or projects (e.g., EPSG:7tro for regional applications)

## Transformation Challenges

- **Datum shifts**: Converting between different earth models (e.g., WGS84 to local datums)
- **Projection distortions**: Different map projections introduce different types of distortion
- **Accuracy requirements**: High-precision applications (cadastre, engineering) require careful transformation
- **Grid shift files**: Some transformations require specialized grid files (.gsb) for high accuracy
- **Metadata management**: Each dataset must carry its CRS metadata to enable correct transformation

## Tools and Libraries

- **PROJ**: The standard geodetic transformation library, used by GDAL, PostGIS, and many other tools
- **GDAL/OGR**: Geospatial data abstraction library with comprehensive CRS transformation support
- **PostGIS**: Spatial database extension with ST_Transform function
- **Apache Sedona**: Distributed spatial processing with CRS transformation capabilities
- **Iceberg GEO**: Modern lakehouse format with CRS specification support

## Best Practices

1. **Standardize on a common CRS** for the Data Platform (e.g., WGS84 for global data, ETRS89/UTM for European regional data)
2. **Preserve original CRS metadata** for all ingested datasets
3. **Transform at ingestion time** for frequently used layers, transform on-demand for exploratory analysis
4. **Validate transformations** by comparing known control points
5. **Use authoritative transformation grids** from national mapping agencies for high-precision work

## Related Concepts

- [[sdi-spatial-data-infrastructure]] — SDI data comes in diverse CRS
- [[ogc-standards]] — OGC standards define CRS handling in web services
- [[inspire-directive]] — INSPIRE mandates specific CRS for European data
- [[sdi-dp-integration-patterns]] — CRS transformation is a key consideration in integration pattern selection
- [[geospatial-etl-pipeline-iceberg]] — CRS transformation in modern lakehouse pipelines
- [[legacy-geospatial-etl-pipeline]] — CRS transformation in traditional ETL workflows