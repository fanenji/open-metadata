---
type: concept
title: Raster-Vector Interactions
created: 2026-04-29
updated: 2026-04-29
tags: [gis, raster, vector, geospatial, data-model]
related: [raster-data-model, coordinate-reference-systems, python-geospatial-stack, map-algebra]
sources: ["Geocomputation with Python.md"]
---
# Raster-Vector Interactions

Techniques for combining raster and vector data models, bridging the two fundamental representations of geographic information. These operations are essential for real-world analysis where continuous surfaces (raster) need to be queried by discrete features (vector) and vice versa.

## Main Techniques

### Raster Cropping and Masking
Using vector polygons to limit raster analysis to areas of interest:
- **Cropping**: Reduces raster extent to the bounding box of the vector
- **Masking**: Sets pixels outside vector boundaries to NoData
- Requires matching projections and valid NoData values

### Raster Extraction
Retrieving raster values at vector locations:
- **Points**: Nearest neighbor or bilinear interpolation
- **Lines**: Elevation profiles via equally-spaced point sampling
- **Polygons**: Zonal statistics (mean, min, max, count, median)

### Rasterization
Converting vector features to raster format:
- Presence/absence binary rasters
- Value-weighted rasters (e.g., population density)
- Configurable: all_touched (all intersecting cells) vs. centroid-based

### Vectorization
Converting raster data to vector format:
- **Raster to Polygons**: Each contiguous cell group becomes a polygon
- **Raster to Points**: Each cell becomes a point at its centroid
- **Raster to Contours**: Isolines at specified intervals (via GDAL)

## Implementation in Python

```python
# Masking
out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)

# Extraction to polygons
rasterstats.zonal_stats(polygons, raster_path, stats=['mean', 'min', 'max'])

# Rasterization
out = rasterio.features.rasterize(
    [(geom, 1) for geom in geometries],
    out_shape=template.shape, transform=template.transform
)

# Vectorization
shapes = list(rasterio.features.shapes(raster_array, transform=src.transform))
```

## Relationship to Wiki

This concept fills a gap in the wiki's geospatial coverage by documenting how raster and vector data models interact. It complements the [[geospatial-analytics-with-dbt]] pattern (which focuses on vector-based H3 analytics) and the [[python-geospatial-stack]] (which provides the implementation tools).
