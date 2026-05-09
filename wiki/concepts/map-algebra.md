---
type: concept
title: Map Algebra
created: 2026-04-29
updated: 2026-04-29
tags: [gis, raster, map-algebra, geocomputation]
related: [raster-data-model, python-geospatial-stack, raster-vector-interactions]
sources: ["Geocomputation with Python.md"]
---
# Map Algebra

A systematic framework for raster computation, originally defined by C. Dana Tomlin (1990). Map algebra classifies raster operations into four types based on the spatial extent of input cells used to compute each output cell.

## Operation Types

### Local Operations
Per-cell operations that compute each output cell from the corresponding input cell(s). Examples:
- Arithmetic: `elev + elev`, `elev**2`
- Mathematical: `np.log(elev)`, `elev > 5`
- Reclassification: assigning new values based on value ranges
- Multi-band: NDVI = (NIR - Red) / (NIR + Red)

### Focal Operations
Neighborhood operations that compute each output cell from a window of surrounding input cells. Examples:
- Minimum/maximum filter (3×3 window)
- Mean/median filter
- Mode filter (categorical rasters)
- Terrain metrics (slope, aspect) via GDAL

### Zonal Operations
Operations on irregular zones defined by another raster. Each zone's cells are aggregated using a summary statistic:
- Mean, median, min, max, count per zone
- Unique value counts for categorical zones

### Global Operations
Per-raster operations that compute a single value from all cells:
- Mean, median, standard deviation
- Histogram
- Total sum

## Implementation in Python

```python
# Local
ndvi = (landsat[3] - landsat[2]) / (landsat[3] + landsat[2])

# Focal (using scipy)
elev_mean = scipy.ndimage.uniform_filter(elev, size=3)

# Zonal
z = {i: elev[grain == i].mean() for i in np.unique(grain)}
```

## Relationship to Wiki

Map algebra provides the theoretical framework for raster computation, complementing the wiki's existing coverage of vector-based spatial operations in [[geospatial-analytics-with-dbt]] and [[python-geospatial-stack]].
