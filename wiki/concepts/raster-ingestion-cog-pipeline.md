---
type: concept
title: Raster Ingestion COG Pipeline
created: 2026-04-29
updated: 2026-04-29
tags: [raster, cog, gdal, geospatial, ingestion]
related: [sdi-dp-integration-strategies, geoscript-etl-system, sdi-regione-liguria, cloud-native-geospatial-workflow]
sources: ["Integrazione SDI DP Analisi.md"]
---
# Raster Ingestion COG Pipeline

This concept page documents the pattern for ingesting raster geospatial data into the Data Platform using GDAL tools to produce Cloud-Optimized GeoTIFF (COG) format.

## Pipeline Steps

1. **Coordinate Transformation**: Using `gdalwarp` to reproject raster data to the target coordinate reference system
2. **Format Conversion**: Using `gdal_translate` to convert to COG format with appropriate tiling and compression
3. **Storage**: Writing COG files directly to S3 object storage in the Data Platform

## Current Implementation

The pipeline runs within the Geoscript system using Python scripts on a Windows Server 2019 VM. It is scheduled via Windows Task Scheduler.

## Advantages

- COG is a widely supported standard optimized for HTTP range requests
- Explicit control over reprojection, tiling, and compression parameters
- Reuses the existing Geoscript codebase and infrastructure

## Limitations

- Single-node batch processing can saturate CPU and RAM
- No automatic retry mechanisms or centralized metrics
- Hybrid orchestration (Windows cron + S3 storage) adds operational complexity
- Limited scalability for large raster datasets or high update frequencies

## Alternative Approaches

- **Serverless GDAL**: Cloud functions (AWS Lambda, Google Cloud Functions) triggered by S3 events or schedulers, offering auto-scaling but with timeout/memory constraints
- **Containerized Batch Jobs**: Docker containers running on Kubernetes with job orchestration for better scalability and monitoring

## Related Pages

- [[sdi-dp-integration-strategies]] — Overall integration strategies
- [[geoscript-etl-system]] — The legacy ETL system running this pipeline
- [[sdi-regione-liguria]] — The parent SDI system
- [[cloud-native-geospatial-workflow]] — Related cloud-native workflow patterns