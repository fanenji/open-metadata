---
type: source
title: "Sedona e file grigliati GSB: Analysis of GSB Grid Shift File Support in Apache Sedona ST_Transform"
created: 2026-03-18
updated: 2026-03-18
tags: [gis, sedona, coordinate-transformation, gsb, geotools, spark]
related: [apache-sedona, sedona-st-transform-limitations, grid-shift-transformations, geotools, postgis, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg, dremio-geospatial-limitations]
sources: ["Sedona e file grigliati GSB.md"]
---
# Sedona e file grigliati GSB: Analysis of GSB Grid Shift File Support in Apache Sedona ST_Transform

This document is a detailed technical analysis of whether Apache Sedona's `ST_Transform` function supports GSB (Grid Shift Binary) and NTv2 grid shift files for high-precision coordinate transformations, particularly those involving datum changes. The analysis covers Sedona versions up to 1.7.1, community discussions, GitHub issues, and the underlying GeoTools library.

## Key Finding

Apache Sedona's `ST_Transform` function, in its standard implementations for Apache Spark and Apache Flink, **does not directly support** the use of GSB grid shift files via explicit parameters or PROJ strings referencing them. The official documentation describes the use of EPSG codes and WKT strings but omits any reference to parameters for specifying grid files or grid-based transformations like `+nadgrids`.

## Evidence Summary

- **Documentation gap**: No mention of GSB, NADGRIDS, NTv2, or complete PROJ strings in the ST_Transform API documentation for Spark/Flink versions.
- **Community silence**: No GitHub issues or Stack Overflow discussions specifically about direct GSB support in ST_Transform.
- **Library capability**: The underlying GeoTools library (used by Sedona) does support grid-based transformations via the `NADCONTransform` class and NTv2 grid files, but this capability is not exposed through Sedona's standard ST_Transform interface.
- **Snowflake exception**: The SedonaSnow Native App for Snowflake appears to handle grid-based transformations, suggesting the core engine has the capability but it is not universally exposed.

## Workarounds

The document identifies three primary workaround approaches:

1. **Spark UDF with pyproj**: Encapsulate transformation logic in a Python UDF using the pyproj library, with GSB files distributed to worker nodes and PROJ_LIB configured.
2. **External preprocessing with ogr2ogr**: Perform the GSB transformation as a separate preprocessing step using GDAL's ogr2ogr utility, writing transformed data to a format readable by Sedona (e.g., GeoParquet).
3. **SedonaSnow Native App**: For Snowflake users, the SedonaSnow app provides integrated grid-based transformation support.

## Relevance to the Data Platform

This analysis is directly relevant to the geospatial data pipeline architecture, particularly for high-precision transformations required in cadastral, civil engineering, and environmental monitoring applications. The library-interface gap pattern documented here mirrors similar limitations found in [[dremio-geospatial-limitations]] and reinforces the need for preprocessing patterns using tools like [[postgis]] and GDAL.

## References

- Apache Sedona Documentation: https://sedona.apache.org/
- GeoTools Documentation: https://geotools.org/
- PROJ Documentation: https://proj.org/
- pyproj Documentation: https://pyproj4.github.io/pyproj/stable/
- GDAL Documentation: https://gdal.org/
- PostGIS ST_Transform: https://postgis.net/docs/ST_Transform.html
- Sedona GitHub Issue #1397: https://github.com/apache/sedona/issues/1397
- Snowflake Community Article on ST_TRANSFORM: https://community.snowflake.com/s/article/100405-P0000-Failed-to-transform-the-coordinates-from-SRID-to-another-when-using-ST-TRANSFORM-function