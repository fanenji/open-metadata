---
type: concept
title: Sedona ST_Transform Limitations
created: 2026-05-07
updated: 2026-05-07
tags: [gis, sedona, coordinate-transformation, gsb, library-interface-gap]
related: [apache-sedona, geotools, grid-shift-transformations, postgis, dremio-geospatial-limitations, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg]
sources: ["Sedona e file grigliati GSB.md"]
---
# Sedona ST_Transform Limitations

This page documents the specific limitations of Apache Sedona's `ST_Transform` function regarding grid-based coordinate transformations, and the workaround patterns available.

## The Limitation

Apache Sedona's `ST_Transform` function, in its standard implementations for Apache Spark and Apache Flink, **does not support**:

- Specifying paths to GSB (Grid Shift Binary) files
- Using `+nadgrids` directives within PROJ strings
- Selecting specific NTv2 transformation pipelines
- Passing complete PROJ strings that reference grid files

The function only accepts EPSG codes (e.g., `'EPSG:4326'`) and, in newer versions, OGC WKT v1 strings for CRS specification.

## Root Cause: Library-Interface Gap

This is a **library-interface gap**: the underlying GeoTools library (version 28.x in Sedona 1.7.1) does support grid-based transformations via the `NADCONTransform` class and NTv2 grid file auto-detection. However, Sedona's SQL/DataFrame API does not expose the parameters needed to invoke and control these operations.

This pattern is similar to [[dremio-geospatial-limitations]], where Dremio's underlying engine supports geospatial operations but the exposed API has limitations.

## Evidence

- **Documentation**: No mention of GSB, NADGRIDS, NTv2, or PROJ strings in ST_Transform docs across versions 1.3.x-1.7.x
- **GitHub Issue #1397**: User request for transformation method selection; response confirms Sedona uses GeoTools but does not expose fine-grained control
- **Community silence**: No discussions about direct GSB support on Stack Overflow or forums
- **Snowflake exception**: SedonaSnow Native App handles grid transformations, proving engine capability exists

## Workaround Patterns

### Pattern 1: Spark UDF with pyproj
- Encapsulate pyproj transformation in a Python UDF
- Distribute GSB files to all worker nodes
- Configure `PROJ_LIB` environment variable on workers
- **Trade-off**: High integration with Spark, but Python UDF overhead and dependency management complexity

### Pattern 2: External Preprocessing with ogr2ogr
- Use GDAL's ogr2ogr as a separate preprocessing step
- Transform data before ingestion into Sedona
- Write output to GeoParquet or other Sedona-readable formats
- **Trade-off**: Better performance (C++ implementation), but adds an ETL step and requires orchestration

### Pattern 3: SedonaSnow Native App (Snowflake only)
- Install SedonaSnow from Snowflake Marketplace
- Use `sedonasnow.sedona.ST_TRANSFORM` which handles grid transformations internally
- **Trade-off**: Simple integration, but Snowflake-specific

## Related Pages

- [[apache-sedona]] — The distributed spatial computing system
- [[geotools]] — The underlying library with GSB capability
- [[grid-shift-transformations]] — Concept page on GSB/NTv2 transformations
- [[postgis]] — Comparison: PostGIS supports `+nadgrids` directly
- [[dremio-geospatial-limitations]] — Similar library-interface gap pattern
- [[legacy-geospatial-etl-pipeline]] — Legacy pipeline using GDAL/OGR
- [[geospatial-etl-pipeline-iceberg]] — Modern pipeline that could benefit from GSB transformations