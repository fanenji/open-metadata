---
type: entity
title: Scott Parks
created: 2026-04-29
updated: 2026-04-29
tags: [person, geospatial, cloud-native, postholer]
related: [postholer, cloud-optimized-geotiff-cog, flatgeobuf-fgb, georaster-layer-for-leaflet, serverless-geospatial-architecture, stac-spatiotemporal-asset-catalog, legacy-geospatial-etl-pipeline]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Scott Parks

Founder of [[postholer]], a hiking resource featuring interactive trail maps with 87 raster/vector layers. Scott is a trailblazer in cloud-native geospatial web mapping, having transitioned from a traditional OGC tile server stack (PostgreSQL/PostGIS, MapServer, MapCache on EC2) to a fully serverless architecture using [[cloud-optimized-geotiff-cog]] and [[flatgeobuf-fgb]] served directly from S3 to a [[georaster-layer-for-leaflet]]-based Leaflet client.

## Key Contributions

- Demonstrated that cloud-native geospatial formats enable fully serverless web mapping, eliminating the need for tile servers, databases, and caches.
- Developed femaFHZ.com, a hazard mapping site using a hybrid COG/FGB approach.
- Advocates for using GDAL format support as a litmus test for technology maturity.
- Promotes the STAC-COG marriage for managing large raster collections.

## Philosophy

Scott emphasizes a pragmatic approach: cloud-native is ideal for many use cases, but server-side VRTs are more efficient for complex multi-layer point queries. He advocates for keeping it simple with core open-source technology (GDAL, SQL, QGIS, PostgreSQL/PostGIS, SQLite/Spatialite, STAC, Leaflet, OpenLayers).