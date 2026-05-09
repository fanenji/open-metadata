---
type: entity
title: DuckDB-WASM
created: 2026-04-08
updated: 2026-04-08
tags: [duckdb, wasm, browser, analytics]
related: [duckdb, browser-based-geospatial-analytics, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, duckdb-spatial-extension]
sources: ["Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM.md"]
---
# DuckDB-WASM

DuckDB compiled to WebAssembly, enabling in-browser execution of analytical SQL queries without any server-side processing or backend setup. DuckDB-WASM is a full DuckDB engine that runs entirely in the browser's JavaScript environment.

## Capabilities

- Full SQL query execution including spatial operations (via the Spatial extension)
- Support for reading Parquet and GeoParquet files fetched from URLs
- Support for community extensions like H3
- Can be initialized with async API from JavaScript

## Key Limitations

- **No HTTPFS extension support**: DuckDB-WASM cannot directly query remote filesystems (S3, HTTP) using the HTTPFS extension. Files must be fetched via JavaScript `fetch()` and loaded into the database.
- **No filesystem access**: Cannot read local files; all data must be loaded programmatically.
- **Memory constraints**: Limited by browser memory and WASM heap size.

## Use Cases

- Client-side geospatial analytics and visualization
- Interactive data exploration dashboards
- Zero-infrastructure demos and prototypes
- Educational tools for geospatial SQL

## Related

- [[duckdb]] — The parent project
- [[browser-based-geospatial-analytics]] — The broader pattern
- [[cloud-native-geospatial-workflow]] — Server-side variant of the pattern