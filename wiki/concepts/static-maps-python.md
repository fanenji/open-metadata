---
type: concept
title: Static Maps in Python
created: 2026-04-29
updated: 2026-04-29
tags: [python, gis, mapping, visualization, matplotlib]
related: [python-geospatial-stack, interactive-maps-python, raster-data-model]
sources: ["Geocomputation with Python.md"]
---
# Static Maps in Python

Creating publication-quality static maps using matplotlib-based plotting in geopandas and rasterio. Static maps are suitable for reports, papers, and presentations where interactivity is not required.

## Key Features

### Minimal Maps
```python
nz.plot()                      # Vector
rasterio.plot.show(nz_elev)    # Raster
```

### Styling and Symbology
- Color, edge color, marker size
- Column-based coloring with legends (categorical or continuous)
- Colormaps: 'Reds', 'Set1', 'plasma', 'viridis', 'BrBG' (append `_r` to reverse)
- Raster colorbars

### Labels
- Annotate features with text labels at centroid coordinates
- Custom font properties and positioning

### Layers
- Overlay multiple vector and raster layers
- Control draw order with `zorder`
- Combine raster basemaps with vector overlays

### Basemaps (contextily)
```python
import contextily as cx
cx.add_basemap(ax, source=cx.providers.OpenStreetMap.Mapnik)
cx.add_basemap(ax, source=cx.providers.CartoDB.Positron)
```

### Faceted Maps
- Multiple subplots showing different attributes
- Shared or independent legends
- Consistent styling across panels

### Export
- Formats: .jpg, .png, .svg, .pdf
- Configurable DPI (e.g., `dpi=300`)

## Relationship to Wiki

Static maps complement the wiki's existing geospatial coverage by providing the visualization layer. They are the output medium for analyses performed with [[python-geospatial-stack]] and [[geospatial-analytics-with-dbt]].
