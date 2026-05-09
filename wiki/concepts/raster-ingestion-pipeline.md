---
type: concept
title: Raster Ingestion Pipeline
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, data-platform, raster, ingestion, geospatial]
related: [geoscript-system, sdi-dp-integration-strategy, geoscript-modernization-plan]
sources: ["Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# Raster Ingestion Pipeline

The raster data ingestion pipeline is a separate approach from vector data ingestion in the SDI-DP integration. It operates within the Geoscript system using Python scripts.

## Process

1. **CRS Transformation**: Using `gdalwarp` to transform coordinate reference systems.
2. **Format Transformation**: Using `gdal_translate` to convert to the target format.
3. **Output**: Data is saved in COG (Cloud Optimized GeoTIFF) format to the DP's S3 object storage (MinIO).

## Key Characteristics

- Operates within the Geoscript system (not the DP's orchestration).
- Uses Python scripts (part of the Geoscript modernization).
- Output format is COG, a cloud-optimized raster format suitable for direct access and streaming.

## Open Questions

- The target CRS for raster data is not specified in the source document.
- The relationship between raster and vector ingestion schedules is not defined.