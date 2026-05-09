---
type: concept
title: Cloud-Native Geospatial Proxy Pattern
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, duckdb, geoparquet, proxy, pattern]
related: [cloud-native-geospatial-workflow, duckdb, geoparquet, koop-js, geoservices-rest-specification, bill-dollins, duckdb-spatial-extension]
sources: ["Producing GeoJSON from SQL (DuckDB Geoparquet).md"]
---
# Cloud-Native Geospatial Proxy Pattern

The cloud-native geospatial proxy pattern uses [[DuckDB]] as an intermediary to convert cloud-native formats (like [[GeoParquet]]) into non-cloud formats (like [[GeoJSON]]). This bridges the "clear boundary between cloud and not-cloud" in geospatial workflows.

[[Bill Dollins]] demonstrated this pattern by using DuckDB's `read_parquet()` function to access a GeoParquet file, then constructing a GeoJSON FeatureCollection using DuckDB's built-in spatial and JSON extensions (`ST_AsGeoJSON`, `json_object`, `array_agg`).

The pattern is particularly relevant for:
- Serving cloud-native geospatial data to legacy systems that require feature services
- Building [[Koop]] providers that act as pass-through layers
- Enabling gradual migration from traditional geospatial pipelines (e.g., [[PostGIS]]) to modern cloud-native stacks

Key design considerations include:
- Pushing column selections and WHERE clauses down to DuckDB for performance
- Dynamically handling arbitrary columns rather than hardcoding them
- DuckDB's speed on full datasets (3M+ rows) makes it suitable as a proxy layer

This pattern extends the [[cloud-native-geospatial-workflow]] concept with a concrete SQL implementation example.