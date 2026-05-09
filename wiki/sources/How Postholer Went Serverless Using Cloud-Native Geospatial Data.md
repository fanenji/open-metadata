---
type: source
title: How Postholer Went Serverless Using Cloud-Native Geospatial Data
created: 2026-04-29
updated: 2026-04-29
tags: [cloud-native, geospatial, serverless, COG, FlatGeobuf, Leaflet, GDAL, STAC]
related: [cloud-optimized-geotiff-cog, flatgeobuf-fgb, georaster-layer-for-leaflet, serverless-geospatial-architecture, stac-spatiotemporal-asset-catalog, postholer, scott-parks, cloud-native-geospatial-workflow, legacy-geospatial-etl-pipeline, formati-e-standard]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
authors: [Scott Parks]
year: 2023
url: "https://cloudnativegeo.org/blog/2023/09/how-postholer-went-serverless-using-cloud-native-geospatial-data/?s=09"
venue: "Cloud Native Geo Blog"
---
# How Postholer Went Serverless Using Cloud-Native Geospatial Data

An interview with Scott Parks, founder of Postholer, describing his transition from a traditional OGC tile server stack (PostgreSQL/PostGIS, MapServer, MapCache on EC2) to a fully serverless architecture using Cloud Optimized GeoTIFF (COG) and FlatGeobuf (FGB) served directly from S3 to a Leaflet-based web client.

## Key Takeaways

- **Serverless architecture**: COG and FGB enable direct client-to-cloud-storage access, eliminating tile servers, databases, caches, and their maintenance costs.
- **Hybrid approach**: Cloud-native is not always optimal — for multi-layer point queries, a server-side VRT is more efficient than 14 separate COG requests.
- **GDAL as gatekeeper**: Scott uses GDAL format support as a litmus test for technology maturity and longevity.
- **STAC-COG marriage**: STAC catalogs make COG collections queryable by bounding box, essential for managing many rasters.
- **Thoughtful data creation**: Pre-computing attributes (e.g., polygon area) avoids repetitive client-side calculations.
- **Zoom-level management**: FGB requires careful zoom-level management to avoid downloading 10GB at low zoom levels.

## Connections

- Extends the wiki's [[cloud-native-geospatial-workflow]] concept to a COG/FGB + Leaflet stack, complementing the existing DuckDB + GeoParquet pattern.
- Scott's old stack (PostgreSQL/PostGIS, MapServer) mirrors the [[legacy-geospatial-etl-pipeline]] pattern documented in the wiki.
- COG and STAC are mentioned in [[Formati e Standard]]; FGB is a new addition.