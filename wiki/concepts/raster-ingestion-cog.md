---
type: concept
title: Raster Ingestion with COG
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, raster, cog, ingestion]
related: [ingestion-dati-geo-strategy, regione-liguria-sdi, geoscript-etl-system]
sources: ["Ingestion Dati Geo.md"]
---
# Raster Ingestion with COG

The raster ingestion process for the Data Platform (DP) involves converting raster geospatial data into Cloud Optimized GeoTIFF (COG) format and storing it on S3 Object Storage.

## Process

The ingestion uses Python scripts that perform:
1. **Coordinate System Transformation**: Using `gdalwarp` command
2. **Format Transformation**: Using `gdal_translate` command
3. **Target Format**: COG (Cloud Optimized GeoTIFF)
4. **Target Storage**: S3 Object Storage of the DP

The process can run within the Geoscript system or within the DP itself.

## Related Pages

- [[ingestion-dati-geo-strategy]] — The overall ingestion strategy
- [[regione-liguria-sdi]] — The Spatial Data Infrastructure
- [[geoscript-etl-system]] — The current ETL system