---
type: concept
title: Hybrid Raster/Vector Strategy for Web Mapping
created: 2026-04-29
updated: 2026-04-29
tags: [pattern, performance, geospatial, web-mapping]
related: [cloud-optimized-geotiff-cog, flatgeobuf-fgb, serverless-geospatial-architecture, femafhz-com]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Hybrid Raster/Vector Strategy for Web Mapping

A performance optimization pattern for web maps that uses low-resolution raster data for low zoom levels and high-resolution vector data for high zoom levels. This balances visual clarity with data transfer efficiency.

## Motivation

Displaying vector footprints at zoom level 12 is impractical because no detail is visible. Conversely, raster data at high zoom levels lacks the interactivity and precision of vectors.

## Implementation

[[scott-parks]] uses this technique at femaFHZ.com to display FEMA flood hazard data and building footprints. He creates two versions of the data:
- A low-resolution raster for zoom levels 1-13
- High-resolution vectors for zoom levels 14-20

## Related Pattern: Zoom-Level Management for FGB

A similar approach is used for [[flatgeobuf-fgb]] data: a low-resolution vector dataset is created for low zoom levels, and the complete dataset is used at high zoom levels. This prevents the FGB API from downloading 10GB of data at zoom level 4.