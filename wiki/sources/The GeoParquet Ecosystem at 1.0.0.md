---
type: source
title: The GeoParquet Ecosystem at 1.0.0
created: 2026-05-07
updated: 2026-05-07
tags: [geoparquet, geospatial, cloud-native, ecosystem]
related: [geoarrow, geoparquet-ecosystem, source-cooperative, gpq, gdal-ogr-geoparquet, geoparquet-data-providers, cloud-native-geospatial-workflow, formati-e-standard, geoparquet-vs-iceberg-metadata]
sources: ["The GeoParquet Ecosystem at 1.0.0.md"]
authors: [Chris Holmes]
year: 2023
url: https://cloudnativegeo.org/blog/2023/10/the-geoparquet-ecosystem-at-1.0.0
venue: Cloud Native Geo Blog
---
# The GeoParquet Ecosystem at 1.0.0

A comprehensive survey of the GeoParquet ecosystem at the time of the 1.0.0 specification release, cataloging libraries, tools, data providers, and community resources. Written by Chris Holmes, Radiant Earth Technical Fellow and co-author of the GeoParquet spec.

## Key Points

- **Multi-language library support**: GeoPandas (Python), GDAL/OGR (C++), GPQ (Go), loaders.gl (JavaScript), GeoParquet.jl (Julia), DotNet library, Fiona (Python), and R libraries (GeoArrow, sfarrow).
- **Tool ecosystem**: Command-line tools (OGR/GDAL, GPQ), desktop GIS (QGIS, FME), web-based tools (Scribble Maps, CARTO), converters (BigQuery converter, stac-geoparquet), and frameworks (Apache Sedona, ArcGIS GeoAnalytics Engine, Seer AI, DuckDB).
- **Data providers**: Microsoft, Planet, Maxar, Ordnance Survey, VIDA, Streambatch, Pacific Spatial Solutions, CARTO Data Observatory.
- **Hosting platform**: Source Cooperative (Radiant Earth initiative) emerging as central repository for cloud-native geospatial data.
- **Gaps**: No native Java library yet; DuckDB lacks direct GeoParquet support; QGIS Mac installer requires conda workaround.
- **Future direction**: OGC ecosystem enhancement grants; goal of ubiquitous GeoParquet support across all geospatial software.

## Relevance to Project

This source provides the definitive catalog of the GeoParquet ecosystem, directly supporting the project's evaluation of GeoParquet as a standard format for geospatial data exchange. It complements existing wiki content on [[geoarrow]], [[cloud-native-geospatial-workflow]], and [[formati-e-standard]].