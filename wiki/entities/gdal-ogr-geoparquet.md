---
type: entity
title: GDAL/OGR GeoParquet Support
created: 2026-05-07
updated: 2026-05-07
tags: [gdal, ogr, geoparquet, geoarrow, column-oriented]
related: [geoparquet-ecosystem, gpq, geoarrow, cloud-native-geospatial-workflow]
sources: ["The GeoParquet Ecosystem at 1.0.0.md"]
---
# GDAL/OGR GeoParquet Support

GDAL/OGR, the foundational geospatial data access library, added drivers for GeoParquet and GeoArrow, implemented by [[Even Rouault]] and sponsored by [[Planet]]. This support is critical for the ecosystem as GDAL/OGR is the backend for many geospatial tools.

## Key Contributions

- **GeoParquet driver**: Read and write GeoParquet files
- **GeoArrow driver**: Read and write GeoArrow format
- **Column-Oriented Read API (RFC 86)**: Enables OGR to retrieve batches of features with a column-oriented memory layout, greatly speeding up columnar format reading

## Impact

- Enables [[QGIS]] to read GeoParquet (via GDAL/OGR backend)
- Provides ogr2ogr command-line conversion to/from GeoParquet
- Powers FME GeoParquet support
- Serves as the reference implementation for the GeoParquet spec

## Relevance to Project

GDAL/OGR's GeoParquet support is essential for any workflow that needs to convert between traditional geospatial formats and GeoParquet, or that uses tools built on GDAL/OGR (e.g., QGIS, FME).