---
type: concept
title: STAC (SpatioTemporal Asset Catalog)
created: 2026-04-29
updated: 2026-04-29
tags: [standard, metadata, catalog, geospatial, STAC]
related: [cloud-optimized-geotiff-cog, serverless-geospatial-architecture, radiant-earth, formati-e-standard]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# STAC (SpatioTemporal Asset Catalog)

A metadata standard for cataloging geospatial assets, particularly [[cloud-optimized-geotiff-cog]] (COG) collections. STAC enables querying COG collections by bounding box, making it an essential companion to COG for managing many rasters.

## Key Properties

- **Catalog structure**: Organizes COGs into collections with searchable metadata.
- **Bounding-box queries**: Allows efficient discovery of assets that intersect a given spatial extent.
- **Widely adopted**: Accepted by both private and government organizations.

## STAC-COG Marriage

[[scott-parks]] emphasizes that the topic of cloud-native data is incomplete without discussing STAC. When working with many high-resolution COGs, STAC allows easy identification of relevant rasters from a collection. [[radiant-earth]]'s GitHub page is recommended as an excellent starting point for learning about STAC.

## Relationship to Existing Wiki

STAC is mentioned in [[Formati e Standard]] as a geospatial standard. This page provides a more detailed treatment of its role in cloud-native geospatial architecture.