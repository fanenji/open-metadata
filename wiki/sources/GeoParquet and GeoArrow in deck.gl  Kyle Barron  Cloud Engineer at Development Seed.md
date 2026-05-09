---
type: source
title: "GeoParquet and GeoArrow in deck.gl | Kyle Barron | Cloud Engineer at Development Seed"
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, web, performance, deck-gl, geoparquet, geoarrow]
related: [deck-gl, lonboard, geoarrow-layers, geoarrow, geoparquet-vs-iceberg-metadata, cloud-native-geospatial-workflow, kyle-barron, development-seed]
sources: ["GeoParquet and GeoArrow in deck.gl  Kyle Barron  Cloud Engineer at Development Seed.md"]
authors: [Kyle Barron]
year: 2023
url: "https://www.youtube.com/watch?v=PFWjMHXdRdY"
venue: "Spatial App Development Summit (CARTO)"
---
# GeoParquet and GeoArrow in deck.gl — Kyle Barron (Development Seed)

A talk by [[Kyle Barron]], Cloud Engineer at [[Development Seed]], presented at the CARTO Spatial App Development Summit (December 2023). The talk advocates for a high-performance web geospatial rendering pipeline using [[GeoParquet]] for data transport, [[GeoArrow]] for in-memory representation, and [[deck.gl]]'s binary API for GPU rendering.

## Key Arguments

- **GeoJSON is the bottleneck** for web-based geospatial visualization due to large file sizes, slow parsing, high memory overhead from JavaScript objects, expensive structured clone for web workers, and indirect GPU upload paths.
- **GeoParquet + GeoArrow + deck.gl binary API** forms a complete high-performance pipeline where each stage eliminates serialization overhead.
- **Same analytical format for backend and frontend** eliminates data duplication and synchronization issues between analysis and visualization copies.

## Performance Claims

- 1M buildings (7M coordinates) parsed in 1.3 seconds via WASM (orders of magnitude faster than GeoJSON)
- 3.2M points rendered in deck.gl via the pipeline
- Python-to-browser pipeline ([[lonboard]]): 3M points in <3 seconds vs. 3.5 minutes (ipy-leaflet) and 2.5 minutes (folium) — both crashed

## Libraries Introduced

- **[[lonboard]]** — Python package creating deck.gl maps from GeoDataFrames via GeoArrow/GeoParquet serialization
- **[[geoarrow-layers]]** — JavaScript library simplifying deck.gl binary API usage with GeoArrow

## Caveats

- Libraries were at 0.1 release at time of talk (December 2023)
- Benchmarks are local-machine only; remote/server scenarios have network transfer overhead
- GeoParquet 1.0 uses WKB encoding requiring JavaScript-side parsing; GeoArrow encoding expected in 1.1
- Spatial partitioning not yet in GeoParquet 1.0
