---
type: source
title: "Producing GeoJSON from SQL, Part 2 (DuckDB/Geoparquet Edition)"
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, duckdb, geoparquet, geojson, sql]
related: [bill-dollins, duckdb, geoparquet, koop-js, source-cooperative, geoservices-rest-specification, cloud-native-geospatial-workflow, duckdb-spatial-extension, duckdb-geoparquet-limitations]
sources: ["Producing GeoJSON from SQL (DuckDB Geoparquet).md"]
authors: [Bill Dollins]
year: 2024
url: "https://blog.geomusings.com/2024/10/10/producing-geojson-from-sql-part-2-duckdb-geoparquet-edition/"
venue: "GeoMusings Blog"
---
# Producing GeoJSON from SQL, Part 2 (DuckDB/Geoparquet Edition)

This blog post by [[Bill Dollins]] demonstrates how to use [[DuckDB]] as a proxy layer to convert [[GeoParquet]] data into [[GeoJSON]] using pure SQL. It follows a previous post that used [[PostGIS]] for the same purpose.

The author uses a combined dataset of Google, Microsoft, and OSM building footprints for Ireland (downloaded from [[Source Cooperative]]) in GeoParquet 1.1.0 format. The core SQL query uses DuckDB's `read_parquet()` function to access the external file, then constructs a GeoJSON FeatureCollection using DuckDB's built-in spatial and JSON extensions (`ST_AsGeoJSON`, `json_object`, `array_agg`).

The work is positioned as the first step toward a [[Koop]] provider that would serve GeoParquet data through the [[GeoServices REST Specification]]. The author notes that DuckDB is surprisingly fast even on full datasets (3M+ rows) and plans to push column selections and WHERE clauses down to DuckDB from a pass-through Koop provider. The query is currently hardcoded to specific columns and must be "genericized" for production use.

Key technical points:
- DuckDB's spatial functions are similar to PostGIS; JSON functions required more translation work
- The approach bridges the "clear boundary between cloud and not-cloud" in geospatial workflows
- DuckDB's speed on full datasets suggests it can serve as an efficient proxy layer
- Dynamic column handling is the next challenge for building a reusable Koop provider