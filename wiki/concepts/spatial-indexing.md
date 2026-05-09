---
type: concept
title: Spatial Indexing
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, indexing, performance, query-optimization]
related: [spatial-partitioning-strategies-for-iceberg, iceberg-geoparquet-integration-patterns, h3-geospatial-indexing]
sources: ["Iceberg e GeoParquet - Strumenti per Integrazione.md"]
---
# Spatial Indexing

Spatial indexing refers to techniques used to accelerate spatial queries on geospatial data. In the context of Iceberg and GeoParquet, spatial indexing (e.g., from Apache Sedona) can be applied to GeoParquet data stored in Iceberg tables to speed up spatial joins, range queries, and nearest-neighbor searches. The interaction between spatial indexing and Iceberg's manifest-level statistics is an area of ongoing interest for query optimization.