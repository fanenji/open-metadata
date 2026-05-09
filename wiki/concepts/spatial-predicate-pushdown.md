---
type: concept
title: Spatial Predicate Pushdown
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, performance, predicate-pushdown, iceberg, parquet]
related: [iceberg-v3-geo-types, geoparquet-origins, foursquare-geospatial-architecture, iceberg-geospatial-support]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet - Summary.md"]
---
# Spatial Predicate Pushdown

Spatial predicate pushdown is a performance optimization technique that uses spatial statistics to skip irrelevant data before decoding geometry. With Iceberg V3 geo types, this operates at two levels.

## Two-Level Spatial Pruning

**Level 1 — Iceberg file-level statistics:**
Iceberg tracks bounding box statistics per data file. When a spatial query (e.g., "find all points within this polygon") is executed, Iceberg can skip entire files whose bounding boxes don't intersect the query region — without opening the file.

**Level 2 — Parquet row-group-level statistics:**
With native geo types in Parquet (Iceberg V3), bounding box statistics are stored at the row-group level within each Parquet file. This enables finer-grained pruning: skip individual row groups within a file without decoding any geometry.

## Before vs. After

**Before (GeoParquet as binary column):**
- Bounding box statistics stored at the file level only
- Predicate pushdown: either skip the entire file or read the entire file

**After (native geo type in Parquet):**
- Bounding box statistics stored at the row-group level
- Predicate pushdown: skip individual row groups — much finer-grained pruning
- Combined with Iceberg's file-level statistics: two levels of spatial pruning before any geometry is decoded

## Performance Impact

The two-level approach dramatically improves query performance for spatial filters. For workloads like Foursquare's ad measurement by proximity (determining which GPS pings are near a billboard), this can reduce the amount of data scanned from billions of rows to only the relevant spatial regions.
