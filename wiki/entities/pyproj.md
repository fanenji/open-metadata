type: entity
title: Pyproj
created: 2026-02-13
updated: 2026-02-13
tags: [python, geospatial, library]
related: [geopandas, proj, gsb-files]
sources: ["Coordinate conversion with GeoPandens and GSB.md"]
---
# Pyproj

**Pyproj** is the Python interface to the **PROJ** library. It serves as the critical bridge between high-level Python geospatial libraries like [[geopandas]] and the underlying C-based coordinate transformation engine.

## Role in the Geospatial Stack
While libraries like [[geopandas]] provide the data structures (GeoDataFrames) and high-level API for transformations (via `.to_crs()`), they delegate the actual mathematical computation and datum transformations to [[pyproj]], which in turn calls [[proj]].

## Key Capabilities
- **Coordinate Transformations**: Handles complex transformations between different Coordinate Reference Systems (CRS).
- **Pipeline Support**: Allows for the definition of explicit transformation pipelines using WKT or PROJ strings, including the use of grid shifts.
- **Integration**: Essential for any Python-based geospatial workflow requiring high precision.
