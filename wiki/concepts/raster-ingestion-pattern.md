---
type: concept
title: Raster Ingestion Pattern
created: 2026-02-13
updated: 2026-02-13
tags: [geospatial, raster, ingestion, cog, gdal]
related: [sdi-data-platform-integration, geoscript-modernization]
sources: ["SDI Data Integration to Data Platform.md"]
---
# Raster Ingestion Pattern

The approach for ingesting raster geospatial data from the SDI into the Data Platform. This pattern is considered valid and standard practice.

## Workflow

1. **Source**: Raster data from Oracle or file-based sources in the SDI
2. **Transformation**: Evolved Geoscript (Python/GDAL) performs:
   - CRS transformation using `gdalwarp` to EPSG:7791
   - Format conversion using `gdal_translate`
3. **Output**: Cloud Optimized GeoTIFF (COG) files
4. **Storage**: Direct S3 upload to MinIO object storage

## Key Considerations

- **Computational Resources**: Raster transformation is CPU, I/O, and RAM intensive — server must be adequately sized
- **Error Handling**: Robust error handling for GDAL commands is essential
- **Orchestration**: Must be scheduled and monitored (cron or DP orchestrator)
- **Cataloging**: COG files need to be registered in the Data Catalog (DataHub/OpenMetadata) for discoverability — typically via S3 scan or explicit registration
- **Update Strategy**: Define how existing COG files are updated/overwritten

## Advantages

- COG is the de facto standard for efficient raster access on object storage
- GDAL (via Python) is the correct tool for this workflow
- Direct S3 upload avoids unnecessary intermediate storage