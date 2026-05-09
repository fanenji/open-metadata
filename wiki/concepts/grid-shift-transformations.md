---
type: concept
title: Grid Shift Transformations
created: 2026-05-07
updated: 2026-05-07
tags: [gis, coordinate-transformation, datum, gsb, nt-v2, proj]
related: [apache-sedona, sedona-st-transform-limitations, geotools, postgis, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg]
sources: ["Sedona e file grigliati GSB.md"]
---
# Grid Shift Transformations

Grid shift transformations are high-precision coordinate transformation methods that use grid-based correction files to model local distortions between geodetic datums. They provide significantly more accurate results than parameter-based methods (e.g., 3- or 7-parameter Helmert transformations).

## File Formats

- **GSB (Grid Shift Binary)**: Binary format for storing grid shift data, commonly used for NTv2 transformations
- **NTv2 (National Transformation version 2)**: Canadian standard format widely adopted internationally
- **NADCON**: US-specific format using `.las`/`.los` or `.laa`/`.loa` files for NAD27/NAD83 transformations

## How They Work

Grid shift files contain a regular grid of correction values (offsets in latitude, longitude, and optionally height) that are interpolated to compute the transformation at any given point. This allows accurate modeling of local distortions in the Earth's crust, which parameter-based methods cannot capture.

## Importance

Grid shift transformations are essential in domains requiring high positional accuracy:

- Cadastral mapping and land registry
- Civil engineering and construction
- Environmental monitoring and change detection
- Cross-border data integration with different national datums

## Support in the Data Platform Stack

| Tool | GSB/NTv2 Support | Method |
|------|------------------|--------|
| **PostGIS** | Yes | `+nadgrids` in PROJ strings |
| **GDAL/ogr2ogr** | Yes | Automatic via PROJ configuration |
| **GeoTools** | Yes | Grid files in classpath resource directory |
| **Apache Sedona (Spark/Flink)** | No | Not exposed via ST_Transform API |
| **SedonaSnow (Snowflake)** | Yes | Internal handling by the Native App |
| **PROJ/pyproj** | Yes | Automatic via PROJ_LIB configuration |

## Workaround Patterns

For environments where direct GSB support is unavailable (e.g., Apache Sedona on Spark/Flink), the recommended approaches are:

1. **Preprocessing with ogr2ogr**: Transform data before ingestion using GDAL
2. **UDF with pyproj**: Encapsulate transformation in a Spark UDF with proper PROJ configuration
3. **PostGIS intermediate**: Use PostGIS as a transformation layer before loading into the data lakehouse

## Related Pages

- [[sedona-st-transform-limitations]] — The specific limitation in Apache Sedona
- [[apache-sedona]] — Distributed spatial computing system
- [[geotools]] — Underlying library with GSB capability
- [[postgis]] — Spatial database with direct `+nadgrids` support
- [[legacy-geospatial-etl-pipeline]] — Legacy pipeline using GDAL/OGR
- [[geospatial-etl-pipeline-iceberg]] — Modern pipeline that could benefit from GSB transformations