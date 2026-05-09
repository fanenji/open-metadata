---
type: source
title: Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM
created: 2026-04-08
updated: 2026-04-08
tags: [geoparquet, duckdb, wasm, overture-maps, browser-based-analytics]
related: [duckdb-wasm, overture-maps, browser-based-geospatial-analytics, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, duckdb-spatial-extension]
sources: ["Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM.md"]
authors: [Florent Gravin]
year: 2025
url: "https://dev.to/camptocamp-geo/querying-overture-maps-geoparquet-directly-in-the-browser-with-duckdb-wasm-4jn4"
venue: "dev.to"
---
# Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM

A practical tutorial demonstrating how to query large geospatial datasets (Overture Maps GeoParquet) entirely in the browser using DuckDB-WASM, with no server-side processing. The article walks through loading DuckDB-WASM, fetching GeoParquet files, running spatial SQL queries (including ST_Contains spatial joins), and visualizing results on a MapLibre GL JS map.

**Key limitation**: DuckDB-WASM does not support the HTTPFS extension, so direct querying of official Overture Maps S3 releases is not possible. Users must extract subsets and host them in their web application.

**Demo**: [https://fgravin.github.io/overture-duckdb-wasm/](https://fgravin.github.io/overture-duckdb-wasm/)  
**Code**: [https://github.com/fgravin/overture-duckdb-wasm](https://github.com/fgravin/overture-duckdb-wasm)