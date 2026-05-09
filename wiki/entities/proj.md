type: entity
title: PROJ
created: 2026-02-13
updated: 2026-02-13
tags: [c-library, geospatial, coordinate-system]
related: [pyproj, gsb-files, proj4j]
sources: ["Coordinate conversion with GeoPandens and GSB.md"]
---
# PROJ

**PROJ** is a powerful C library for performing cartographic projections and coordinate transformations. It is the industry standard engine used by almost all modern geospatial software, including [[geopandas]] (via [[pyproj]]) and [[apache-sedona]].

## Core Functions
- **Coordinate Transformation**: Converting coordinates between different geographic and projected systems.
- **Grid Shift Support**: Utilizing specialized files (such as [[gsb-files]]) to account for local distortions and datum shifts (e.g., ED50 to WGS84).
- **CRS Management**: Handling various definitions of Coordinate Reference Systems, including EPSG, WKT, and PROJ strings.

## Configuration
For high-precision transformations, PROJ must be able to locate its auxiliary data. This is typically managed via the `PROJ_DATA` environment variable, which points the library to the directory containing necessary transformation grids.
