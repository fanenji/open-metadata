---
type: concept
title: Cloud Optimized GeoTIFF (COG)
created: 2026-04-29
updated: 2026-05-07
tags: [raster, geotiff, cloud, object-storage, format, cloud-native, geospatial, COG]
related: [raster-data-ingestion-pipeline, minio, stac-server-implementation, raster-cataloging-strategy, geospatial-etl-pipeline-iceberg, dremio-geospatial-limitations, flatgeobuf-fgb, georaster-layer-for-leaflet, serverless-geospatial-architecture, stac-spatiotemporal-asset-catalog, cloud-native-geospatial-workflow, formati-e-standard, legacy-geospatial-etl-pipeline]
sources: ["ETL RASTER.md", "How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Cloud Optimized GeoTIFF (COG)

A Cloud Optimized GeoTIFF (COG) is a GeoTIFF file structured for efficient cloud access. It enables HTTP range-request streaming, allowing clients to fetch only the portions of a file they need (e.g., specific resolution levels or geographic extents) without requiring an intermediate tile server or downloading the entire file. COG is the de facto standard for storing and serving raster data on object storage systems like S3 or MinIO, and a core enabler of [[serverless-geospatial-architecture]].

## Key Characteristics

- **Internal Tiling:** Data is organized in tiles for efficient partial reads.
- **Overview Layers:** Multiple resolution levels are stored within the file, enabling fast zoom-out operations.
- **HTTP Range Requests:** Clients can request specific byte ranges, enabling streaming access.
- **Standard GeoTIFF Structure:** Backward compatible with standard GeoTIFF readers.
- **GDAL Support:** Fully supported by GDAL, making it a mature and reliable format.

## Role in the Data Platform

COG is the primary format for raster data in the Data Platform. The Geoscript/Python+GDAL pipeline generates COG files in EPSG:7791 and stores them on MinIO. Unlike vector data, which is managed through Iceberg/Nessie, COG files are accessed directly via their S3 path.

## Access Patterns

- **Direct S3 Access:** Tools like QGIS, Python with Rasterio, and other GIS clients can access COG files directly via their S3 path.
- **Catalog-Mediated Discovery:** The S3 path is stored in the Data Catalog (DataHub/OpenMetadata) and/or STAC server, enabling users to discover and access the data.
- **Dremio Not Recommended:** Dremio is not optimized for COG analysis; direct S3 access is the correct pattern.

## Usage in Postholer

[[scott-parks]] uses COG for all raster layers in his [[postholer]] maps, displayed via the [[georaster-layer-for-leaflet]] JavaScript API. COG data is updated hourly/daily using GDAL utilities wrapped in BaSH scripts and scheduled with cron.

## Limitations

- For multi-layer point queries, 14 separate COG requests are less efficient than a single server-side VRT query.
- COG is a raster format; vector data requires a different approach (e.g., [[flatgeobuf-fgb]]).

## Relationship to STAC

[[stac-spatiotemporal-asset-catalog]] (STAC) is the metadata catalog that makes COG collections queryable by bounding box, forming the "STAC-COG marriage" that [[scott-parks]] considers essential for managing many rasters.