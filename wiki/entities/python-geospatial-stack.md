---
type: entity
title: Python Geospatial Stack
created: 2026-04-29
updated: 2026-04-29
tags: [python, gis, geopandas, rasterio, shapely, pyproj]
related: [raster-data-model, coordinate-reference-systems, map-algebra, raster-vector-interactions, static-maps-python, interactive-maps-python, geospatial-analytics-with-dbt, geoarrow]
sources: ["Geocomputation with Python.md"]
---
# Python Geospatial Stack

The core set of open-source Python packages for geographic data analysis, as documented in [[Geocomputation with Python]]. The stack provides comprehensive support for both vector and raster data models, coordinate reference system management, and map creation.

## Core Packages

| Package | Purpose |
|---|---|
| **geopandas** | Vector layer operations (GeoDataFrame, GeoSeries), spatial joins, aggregation, I/O |
| **rasterio** | Raster data I/O, metadata access, reprojection, windowed reading |
| **shapely** | Individual geometry operations (points, lines, polygons), topological relations |
| **pyproj** | CRS management, reprojection, EPSG code resolution |
| **numpy** | Array operations for raster data values |
| **matplotlib** | Static map rendering, symbology, faceted maps |

## Supporting Packages

| Package | Purpose |
|---|---|
| **contextily** | Basemap tiles for static maps |
| **osmnx** | OpenStreetMap data access (street networks, POIs) |
| **cartopy** | Map projections and Natural Earth data access |
| **topojson** | Topology-aware geometry simplification |
| **folium** | Interactive map backend (Leaflet) |
| **rasterstats** | Raster extraction to points, lines, polygons |
| **scipy** | Focal operations (filters), statistical functions |

## Relationship to Other Wiki Content

The Python Geospatial Stack provides a complementary approach to the [[geospatial-analytics-with-dbt]] pattern documented elsewhere in the wiki. While the dbt/H3/Snowflake approach is optimized for production-scale geospatial analytics in a data warehouse, the Python stack is better suited for ad-hoc analysis, raster processing, and custom map creation. The [[geoarrow]] format bridges these approaches by providing a columnar in-memory format compatible with both ecosystems.
