---
type: concept
title: GSB Grid Shift Files
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, crs, transformation, proj, gis]
related: [gdal-ogr, apache-sedona, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# GSB Grid Shift Files

GSB (Grid Shift Binary) files are binary grid files used for precise datum transformations in geodetic coordinate reference system conversions. They are a critical requirement for the geospatial data ingestion pipeline.

## Purpose

GSB files enable accurate transformations between different geodetic datums (e.g., from local datums to WGS84) by providing a grid of offset values at regular intervals. Unlike simple mathematical transformations (which use only parameters like translation, rotation, and scale), grid shift methods account for local variations in the Earth's surface, providing higher accuracy for regional transformations.

## Role in the Pipeline

The current GDAL-based pipeline relies on GDAL's integration with the PROJ library to use GSB files for CRS transformations. This capability is essential for converting source data from regional coordinate systems (e.g., Italian Gauss-Boaga, EPSG:3003/3004) to standard global systems.

## Support Across Alternatives

| Tool | GSB Support | Notes |
|------|-------------|-------|
| GDAL/OGR | Native | Via PROJ integration, well-documented |
| GeoPandas (pyproj) | Supported | Via PROJ, requires correct environment configuration |
| Apache Sedona | Unclear | ST_Transform documentation emphasizes EPSG/WKT; GSB support not explicitly documented |

## Configuration Requirements

- PROJ library must be properly configured with access to GSB files
- PROJ_LIB environment variable must point to the grid directory
- GDAL and PROJ versions must be aligned with GSB file versions
- Version mismatches can introduce subtle, hard-to-diagnose transformation errors

## Related

- [[gdal-ogr]] — Primary tool with native GSB support
- [[apache-sedona]] — Alternative with unclear GSB support
- [[legacy-geospatial-etl-pipeline]] — Current pipeline relying on GSB support
- [[geospatial-etl-pipeline-iceberg]] — Proposed pipeline that must address GSB support
