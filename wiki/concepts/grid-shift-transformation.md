type: concept
title: Grid Shift Transformation
created: 2026-02-13
updated: 2026-02-13
tags: [gis, geospatial, accuracy, datum]
related: [gsb-files, proj, pyproj]
sources: ["Coordinate conversion with GeoPandens and GSB.md"]
---
# Grid Shift Transformation

**Grid Shift Transformation** is a high-precision technique used in geospatial analysis to account for local distortions when converting between different coordinate reference systems (CRS).

## Mechanism
Unlike standard mathematical transformations that apply a uniform formula across a whole projection, a grid shift transformation uses a lookup table (often stored in [[gsb-files]]) to apply localized corrections. This is particularly critical when dealing with legacy datums or regional coordinate systems where the Earth's ellipsoid model varies significantly.

## Technical Requirements
To implement these transformations in a Python-based stack (e.g., using [[geopandas]]):
- The **PROJ** library must be configured to access the necessary grid files.
- The `PROJ_DATA` environment variable must be correctly pointed to the directory containing the `.gsb` files.
- Complex transformations may require defining a `pyproj.Transformer` pipeline that explicitly includes the `hgridshift` step.
