type: concept
title: GSB Files
created: 2026-02-13
updated: 2026-02-13
tags: [gis, geospatial, data-format, precision]
related: [proj, pyproj, geopandas]
sources: ["Coordinate conversion with GeoPandens and GSB.md"]
---
# GSB Files

**GSB (Grid Shift Binary)** files are specialized data formats used by the **PROJ** library to perform high-accuracy coordinate transformations.

## Purpose
Standard mathematical formulas for transforming between different datums (e.g., from an older European datum like ED50 to the modern WGS84) often lack the precision required for regional mapping. GSB files provide "grid shifts" that account for local, non-linear distortions in the Earth's surface model, significantly increasing transformation accuracy.

## Implementation in Python
GeoPandas does not manage these files directly. Instead, the workflow relies on:
1. **PROJ Engine**: The underlying engine that reads the `.gsb` files.
2. **Environment Configuration**: The `PROJ_DATA` environment variable must be set to a path containing these files so that [[pyproj]] and [[proj]] can locate them.
3. **Transformation Pipeline**: Using `pyproj.Transformer` to explicitly define a pipeline that includes the `+proj=hgridshift` step.
