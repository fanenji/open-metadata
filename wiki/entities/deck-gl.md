---
type: entity
title: deck.gl
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, visualization, webgl, javascript]
related: [lonboard, geoarrow-layers, geoarrow, geoparquet-vs-iceberg-metadata, kyle-barron, development-seed]
sources: ["GeoParquet and GeoArrow in deck.gl  Kyle Barron  Cloud Engineer at Development Seed.md"]
---
# deck.gl

deck.gl is a WebGL-powered visualization framework for large-scale geospatial data on the web. Developed by Uber and now maintained as an open-source project, it provides a high-level layer API for rendering points, lines, polygons, and 3D objects.

## Binary API

deck.gl exposes a low-level binary API that accepts raw binary buffers (Float32Array, Uint8Array, etc.) for geometry coordinates, colors, radii, and other attributes. This API:

- Eliminates serialization overhead from JavaScript objects
- Copies buffers directly to the GPU without intermediate conversion
- Enables zero-copy data sharing between web workers, WASM, and the main thread

## Role in the High-Performance Pipeline

In the pipeline advocated by [[Kyle Barron]], deck.gl is the rendering endpoint:

1. **[[GeoParquet]]** — compressed, columnar file format for transport
2. **[[GeoArrow]]** — in-memory binary buffer representation
3. **deck.gl binary API** — direct GPU upload for rendering

This stack eliminates text serialization (GeoJSON) at every stage, enabling orders-of-magnitude performance improvements for large geospatial datasets in the browser.

## Related Libraries

- **[[lonboard]]** — Python binding to deck.gl that serializes GeoDataFrames to GeoArrow/GeoParquet and sends them to the browser
- **[[geoarrow-layers]]** — JavaScript library that simplifies using deck.gl's binary API with GeoArrow tables
