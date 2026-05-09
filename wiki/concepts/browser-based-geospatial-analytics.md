---
type: concept
title: Browser-Based Geospatial Analytics
created: 2026-04-08
updated: 2026-04-08
tags: [geospatial, analytics, browser, wasm, zero-infrastructure]
related: [duckdb-wasm, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, overture-maps, geoparquet]
sources: ["Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM.md"]
---
# Browser-Based Geospatial Analytics

The pattern of running spatial SQL queries and geospatial analytics entirely in the browser using DuckDB-WASM, with no server-side processing or backend infrastructure. This extends the [[cloud-native-geospatial-workflow]] pattern from server-side to fully client-side execution.

## Architecture

1. **Data Preparation**: GeoParquet subsets are extracted from large datasets (e.g., Overture Maps) and hosted as static files on a web server or CDN.
2. **Browser Engine**: DuckDB-WASM is initialized in the browser with the Spatial extension loaded.
3. **Data Loading**: GeoParquet files are fetched via JavaScript `fetch()` and loaded into DuckDB-WASM.
4. **Spatial SQL**: Queries using spatial functions (ST_Contains, ST_AsGeoJSON, etc.) are executed in-browser.
5. **Visualization**: Results are converted to GeoJSON and rendered with libraries like MapLibre GL JS.

## Key Advantages

- **Zero infrastructure**: No backend servers, databases, or API endpoints needed
- **Privacy**: Data never leaves the client
- **Scalability**: Leverages client-side resources
- **Simplicity**: Static hosting only

## Key Limitations

- **No HTTPFS in WASM**: Cannot directly query remote S3/HTTP filesystems
- **Memory constraints**: Limited by browser memory
- **Dataset size**: Practical limits on how much data can be processed in-browser
- **No filesystem access**: All data must be loaded programmatically

## Related

- [[cloud-native-geospatial-workflow]] — Server-side variant
- [[duckdb-wasm]] — The enabling technology
- [[duckdb-geoparquet-limitations]] — Known limitations
- [[overture-maps]] — Common data source for this pattern