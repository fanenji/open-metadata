---
type: entity
title: geoarrow-layers
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, javascript, visualization, deck-gl, geoarrow]
related: [deck-gl, lonboard, geoarrow, geoparquet-vs-iceberg-metadata, kyle-barron, development-seed]
sources: ["GeoParquet and GeoArrow in deck.gl  Kyle Barron  Cloud Engineer at Development Seed.md"]
---
# geoarrow-layers

geoarrow-layers is a JavaScript library that simplifies using [[deck.gl]]'s binary API with [[GeoArrow]] memory format. It provides GeoArrow-aware layer classes (scatter plot, path, solid polygon) that accept GeoArrow tables directly.

## Features

- Accepts a GeoArrow table (from parsed GeoParquet or a GeoArrow file) and a geometry column name
- Manages internal chunking of Arrow arrays
- Handles validation of geometry and attribute data
- Supports per-object colors and radii from Arrow columns (not just constants)

## Usage

Instead of manually constructing deck.gl's low-level binary data objects, users pass a GeoArrow table and column name:

```javascript
import { GeoArrowScatterplotLayer } from 'geoarrow-layers';

const layer = new GeoArrowScatterplotLayer({
  id: 'points',
  getPosition: 'geometry',
  getFillColor: 'color_column',
  getRadius: 'radius_column'
});
```

## Status

First released as 0.1 in December 2023, alongside [[lonboard]]. Part of the GeoArrow organization's JavaScript ecosystem.
