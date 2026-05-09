---
type: concept
title: FlatGeobuf (FGB)
created: 2026-04-29
updated: 2026-04-29
tags: [format, vector, cloud-native, geospatial, FGB]
related: [cloud-optimized-geotiff-cog, serverless-geospatial-architecture, cloud-native-geospatial-workflow, formati-e-standard]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# FlatGeobuf (FGB)

An indexed vector data format that uses the same underlying HTTP range-request streaming mechanism as [[cloud-optimized-geotiff-cog]] (COG). Created by [[bjorn-harrtell]], FGB enables direct client-to-cloud-storage access for vector data without an intermediate tile server.

## Key Properties

- **HTTP range requests**: Clients request only the needed portions of the file, enabling efficient streaming of large vector datasets.
- **Indexed**: Spatial indexing allows fast bounding-box queries without scanning the entire file.
- **GDAL support**: FGB is fully supported by GDAL, meeting [[scott-parks]]'s technology maturity criterion.

## Usage in Postholer

[[scott-parks]] uses FGB for all vector layers in his [[postholer]] maps. He chose FGB over alternatives like PMTiles for simplicity, noting he may revisit that decision if his needs change.

## Limitations

- **Zoom-level management required**: If the extent of a 10GB FGB file is contained within the map viewport at a low zoom level, the API will attempt to download and display the entire file. Scott addresses this by creating low-resolution vector datasets for low zoom levels and using the complete dataset at high zoom levels.
- **Not suitable for all vector use cases**: For complex multi-layer point queries, a server-side approach may be more efficient.

## Comparison to PMTiles

FGB is one of several cloud-native vector formats. [[scott-parks]] chose FGB for its simplicity and GDAL support, but acknowledges that PMTiles may be a better fit for some use cases.