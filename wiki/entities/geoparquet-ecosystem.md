---
type: entity
title: GeoParquet Ecosystem
created: 2026-05-07
updated: 2026-05-07
tags: [geoparquet, geospatial, ecosystem, cloud-native]
related: [geoarrow, source-cooperative, gpq, gdal-ogr-geoparquet, geoparquet-data-providers, chris-holmes, cloud-native-geospatial-workflow, formati-e-standard, geoparquet-vs-iceberg-metadata]
sources: ["The GeoParquet Ecosystem at 1.0.0.md"]
---
# GeoParquet Ecosystem

The GeoParquet Ecosystem encompasses the libraries, tools, data providers, and community infrastructure that support the GeoParquet 1.0.0 specification. As of October 2023, the ecosystem includes multi-language library support, command-line and desktop tools, web-based platforms, and a growing number of data providers.

## Libraries

- **Python**: [[GeoPandas]] (first library to support GeoParquet), [[Fiona]] (row-based support)
- **R**: GeoArrow R library, sfarrow
- **C++**: [[GDAL/OGR]] (GeoParquet and GeoArrow drivers with column-oriented read API)
- **Go**: [[GPQ]] (conversion, validation, description; WASM web app)
- **JavaScript**: loaders.gl (pure JavaScript support)
- **Julia**: GeoParquet.jl
- **.NET**: DotNet GeoParquet library
- **Rust/WASM**: Kyle Barron's browser-based tooling

## Tools

- **Command-line**: OGR/GDAL (ogr2ogr), GPQ CLI
- **Desktop**: [[QGIS]] (via GDAL/OGR), [[FME]] (Safe Software, v2023.1+)
- **Web-based**: Scribble Maps, CARTO, geoparquet.org converter
- **Converters**: BigQuery converter, stac-geoparquet
- **Frameworks**: [[Apache Sedona]], ArcGIS GeoAnalytics Engine (Esri), Seer AI, [[DuckDB]] (indirect support)

## Data Providers

See [[geoparquet-data-providers]] for the full list.

## Hosting

[[Source Cooperative]] (Radiant Earth initiative) serves as the primary hosting platform for GeoParquet datasets.

## Community

- Slack: #geoparquet channel on Cloud Native Geospatial Foundation
- Community meetings: Bi-weekly, 17:00 UTC
- OGC ecosystem enhancement grants available

## Gaps

- No native Java library (GeoTools/GeoServer community)
- DuckDB lacks direct GeoParquet support
- QGIS Mac installer requires conda workaround