---
type: concept
title: Dynamic Column Handling for Geospatial SQL
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, sql, duckdb, koop, pattern]
related: [cloud-native-geospatial-proxy-pattern, duckdb, koop-js, bill-dollins]
sources: ["Producing GeoJSON from SQL (DuckDB Geoparquet).md"]
---
# Dynamic Column Handling for Geospatial SQL

Dynamic column handling refers to the ability to write SQL queries that automatically adapt to arbitrary column schemas, rather than hardcoding specific column names. This is a critical requirement for building reusable geospatial data providers.

[[Bill Dollins]] identified this as the next step after demonstrating a proof-of-concept query that converts [[GeoParquet]] to [[GeoJSON]] using [[DuckDB]]. His initial query hardcodes column names like `bf_source`, `boundary_id`, `confidence`, etc. For a production [[Koop]] provider, the query must dynamically discover and handle whatever columns exist in the source dataset.

The challenge is that DuckDB SQL lacks stored procedures or dynamic SQL generation capabilities that would make this straightforward. Solutions may involve:
- Using DuckDB's `DESCRIBE` or `SUMMARIZE` functions to discover schema
- Building dynamic SQL strings in the application layer (e.g., Node.js for Koop)
- Leveraging DuckDB's JSON functions to handle properties generically

This concept is essential for the [[cloud-native-geospatial-proxy-pattern]] to move from proof-of-concept to production-ready implementation.