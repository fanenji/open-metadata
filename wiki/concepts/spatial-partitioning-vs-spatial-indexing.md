type: concept
title: Spatial Partitioning vs Spatial Indexing
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, indexing, partitioning, cloud-native]
related: [geoparquet, geoarrow, geoparquet-vs-iceberg-metadata, cloud-native-geospatial-workflow, flatgeobuf, geopackage]
sources: ["Interview with Kyle Barron on GeoArrow and GeoParquet, and the Future of Geospatial Data Analysis.md"]
---
# Spatial Partitioning vs Spatial Indexing

Spatial partitioning and spatial indexing are two approaches to organizing geospatial data for efficient access. [[geoparquet]] uses spatial partitioning, while formats like [[FlatGeobuf]] and [[GeoPackage]] use spatial indexing.

## Spatial Indexing (Per-Row)

Traditional spatial indexing records the position of every single row of data. This is useful for quickly accessing individual rows but prevents effective compression and scales poorly because the index grows very large with the dataset.

## Spatial Partitioning (Chunk-Based)

Spatial partitioning records the extent of a whole group of rows (a chunk), not individual rows. This provides flexibility and scalability when writing data. The writer can adjust chunk size to choose the tradeoff between index size and indexing efficiency.

**Upside:** Entire groups of data are indexed and compressed as a single unit, enabling better compression and cloud-native filtering.

**Downside:** Accessing a single row requires fetching extra data from the chunk.

## When to Use Each

- **Spatial Partitioning (GeoParquet):** Best for bulk access to data that is co-located in spatial regions. Ideal for cloud-native workflows where column pruning and efficient filtering over large datasets are needed.
- **Spatial Indexing (FlatGeobuf, GeoPackage):** Better suited when access patterns regularly require single rows of data.

This distinction is a key differentiator for [[geoparquet]] and is central to understanding its advantages over traditional geospatial formats in cloud-native environments.