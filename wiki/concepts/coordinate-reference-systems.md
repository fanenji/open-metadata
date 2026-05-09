---
type: concept
title: Coordinate Reference Systems
created: 2026-04-29
updated: 2026-04-29
tags: [gis, crs, projection, geospatial]
related: [raster-data-model, python-geospatial-stack, raster-vector-interactions, geospatial-analytics-with-dbt]
sources: ["Geocomputation with Python.md"]
---
# Coordinate Reference Systems

A Coordinate Reference System (CRS) defines how geographic coordinates map to locations on Earth. Understanding CRS is fundamental to all geospatial work — incorrect CRS leads to meaningless area calculations, distance measurements, and spatial operations.

## Types

### Geographic CRS
Uses longitude and latitude to identify locations on Earth's 3D surface. References an ellipsoidal surface adjusted by a datum (e.g., WGS84). Units are angular degrees.

### Projected CRS
Converts Earth's 3D surface to 2D Cartesian coordinates (Easting/Northing), typically in meters. All projections introduce distortions, preserving different properties:

- **Conformal**: Preserves local shape (e.g., UTM, Mercator)
- **Equal-area**: Preserves area (e.g., Mollweide, LAEA)
- **Equidistant**: Preserves distance from a point (e.g., Azimuthal Equidistant)
- **Azimuthal**: Preserves direction from a point

## CRS Representations

| Format | Example | Notes |
|---|---|---|
| Authority:Code | `EPSG:4326` | Recommended; unambiguous |
| WKT | Full specification | Unambiguous; "shall prevail" over identifiers |
| Proj-string | `+proj=longlat +ellps=WGS84 +datum=WGS84` | Outdated; ambiguous |

## Key Operations

- **Querying**: `gdf.crs`, `src.crs`, `.crs.is_geographic`
- **Setting metadata**: `.set_crs(4326)` — does **not** transform coordinates
- **Reprojection**: `.to_crs(27700)` for vector, `rasterio.warp.reproject` for raster

## Selection Guidance

- **WGS84 (EPSG:4326)**: Standard for web mapping and GPS
- **UTM zones**: Conformal; restrict to 6° from central meridian
- **LAEA**: Equal-area preservation for continental regions
- **AEQD**: Accurate straight-line distances from center point
- **LCC**: Regions spanning thousands of km
- **STERE**: Polar regions

## Importance

Geometric calculations (area, length, distance) require a projected CRS with meters as units. Geographic CRS coordinates in degrees produce meaningless numeric results for these operations.
