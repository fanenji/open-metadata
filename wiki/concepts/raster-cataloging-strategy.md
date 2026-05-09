---
type: concept
title: Raster Cataloging Strategy
created: 2026-04-29
updated: 2026-04-29
tags: [cataloging, raster, stac, datahub, openmetadata, discovery]
related: [cloud-optimized-geotiff-cog, stac-server-implementation, raster-data-ingestion-pipeline, datahub, openmetadata, minio]
sources: ["ETL RASTER.md"]
---
# Raster Cataloging Strategy

The raster cataloging strategy defines how Cloud Optimized GeoTIFF (COG) files stored on MinIO are made discoverable, understandable, and usable through the Data Platform's cataloging systems.

## Two-Tier Cataloging Architecture

The recommended approach uses two complementary cataloging systems:

### 1. General Data Catalog (DataHub/OpenMetadata)
- **Purpose:** Enterprise-wide discovery and governance of all data assets (tabular, raster, vector, documents, BI reports)
- **Granularity:** Dataset-level (e.g., "Ortofoto Regione Liguria 2023")
- **Metadata:** Technical (format, CRS, resolution, BBOX, S3 path) and business (name, description, owner, tags, license, lineage)
- **Population:** The ingestion process pushes metadata via the catalog's API

### 2. Specialized STAC Server
- **Purpose:** Standards-compliant spatiotemporal search optimized for geospatial assets
- **Granularity:** Can support both dataset-level (Collections) and file-level (Items)
- **Metadata:** STAC standard fields with extensions (EO, Projection, etc.)
- **Population:** The ingestion process generates STAC JSON using `pystac` and submits it via the STAC API

## Dataset-Level vs. File-Level Cataloging

### Dataset-Level (Recommended for Orthophoto Mosaics)
- A logical collection of COG files is registered as a single catalog entry
- **Pros:** Avoids catalog bloat, simpler search, matches user expectation of finding the complete dataset
- **Cons:** Less granularity for individual file metadata
- **Use Case:** Orthophoto mosaics, where tiles are part of a single coherent dataset

### File-Level (For Distinct Scenes)
- Each individual COG file is registered as a separate catalog entry
- **Pros:** Maximum granularity, specific metadata per file
- **Cons:** Potentially enormous number of catalog entries, higher maintenance overhead
- **Use Case:** Individual satellite scenes acquired on different dates

## User Workflow

1. User searches the Data Catalog (e.g., "ortofoto liguria 2023")
2. Finds the raster dataset entry with description, CRS, resolution, BBOX, owner
3. Retrieves the S3 base path (e.g., `s3://bucket/raster/ortofoto/anno=2023/`)
4. Uses the S3 path in their analysis tool (QGIS, Python with Rasterio, etc.) to stream COG data
