---
type: concept
title: Raster Data Model
created: 2026-04-29
updated: 2026-04-29
tags: [gis, raster, geospatial, data-model]
related: [python-geospatial-stack, coordinate-reference-systems, map-algebra, raster-vector-interactions, geospatial-analytics-with-dbt]
sources: ["Geocomputation with Python.md"]
---
# Raster Data Model

A geographic data model where space is divided into a regular grid of cells (pixels), each containing a value representing a measured or classified attribute. Rasters are the standard representation for continuous surfaces such as elevation, temperature, satellite imagery, and land cover.

## Components

A raster dataset consists of two parts:

1. **Metadata**: Transform matrix (origin coordinates, cell resolution), CRS, dimensions (rows, columns, bands), data type, NoData value
2. **Values**: A numpy array (2D for single band, 3D for multiband) containing cell values

## Key Operations

- **Subsetting**: Access individual cells or windows by array index
- **Summarizing**: Mean, median, histogram, unique value counts
- **Map Algebra**: Local, focal, zonal, and global operations (see [[map-algebra]])
- **Reprojection**: Transforming to a different CRS using `rasterio.warp.reproject`
- **Merging**: Combining overlapping rasters with configurable merge methods (first, last, min, max)
- **Resampling**: Changing resolution with methods like nearest, bilinear, cubic, average

## Common Formats

- **GeoTIFF (.tif)**: Open standard, widely supported
- **Cloud Optimized GeoTIFF (COG)**: Enables partial reads via HTTP
- **JPEG2000 (.jp2)**: Compressed, used in satellite imagery

## Relationship to Wiki

The raster data model fills a significant gap in the wiki's geospatial coverage, which previously focused on vector-based approaches ([[geospatial-analytics-with-dbt]], [[geoarrow]]). Raster processing is essential for elevation analysis, satellite imagery, environmental monitoring, and continuous surface modeling.
