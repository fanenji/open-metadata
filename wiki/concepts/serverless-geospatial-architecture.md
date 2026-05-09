---
type: concept
title: Serverless Geospatial Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, serverless, geospatial, cloud-native]
related: [cloud-optimized-geotiff-cog, flatgeobuf-fgb, georaster-layer-for-leaflet, cloud-native-geospatial-workflow, legacy-geospatial-etl-pipeline, postholer, scott-parks]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Serverless Geospatial Architecture

An architectural pattern for web mapping that eliminates tile servers, databases, caches, and their associated maintenance costs by serving geospatial data directly from cloud storage (e.g., S3) to the client browser using cloud-native formats.

## Core Components

- **Raster data**: [[cloud-optimized-geotiff-cog]] (COG) — enables HTTP range-request streaming of raster tiles.
- **Vector data**: [[flatgeobuf-fgb]] (FGB) — enables HTTP range-request streaming of vector features.
- **Client library**: [[georaster-layer-for-leaflet]] — JavaScript API for displaying COGs in Leaflet maps.
- **Mapping framework**: [[leaflet]] — open-source JavaScript library for interactive web maps.
- **Cloud storage**: S3 or compatible object storage.

## Benefits

- No tile servers, databases, or caches to maintain in production.
- Reduced infrastructure costs ([[scott-parks]] removed an r5.large EC2 server with 400GB disk).
- Simplified architecture: only a web browser and cloud storage are needed for serving maps.
- Fully open-source stack.

## Limitations and Hybrid Approaches

- **Static vs. dynamic content**: Cloud-native pushes spatial analysis to the client. For complex multi-layer point queries, a server-side virtual raster (VRT) is more efficient.
- **Base maps**: Most base maps (OSM, Satellite, Topo) are best served by third-party tile servers and CDNs — don't reinvent the wheel.
- **Zoom-level management**: FGB requires careful zoom-level management to avoid downloading entire datasets at low zoom levels.
- **Data updates**: Back-end resources are still needed for data processing and updates (GDAL + cron).

## Comparison to DuckDB + GeoParquet

The wiki's existing [[cloud-native-geospatial-workflow]] focuses on DuckDB + GeoParquet for analytical queries. The COG/FGB + Leaflet pattern documented here is a complementary approach optimized for web mapping rather than analytical processing.