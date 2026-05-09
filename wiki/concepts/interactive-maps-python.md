---
type: concept
title: Interactive Maps in Python
created: 2026-04-29
updated: 2026-04-29
tags: [python, gis, mapping, visualization, leaflet, folium]
related: [python-geospatial-stack, static-maps-python, raster-data-model]
sources: ["Geocomputation with Python.md"]
---
# Interactive Maps in Python

Creating web-based interactive maps using the Leaflet JavaScript library via geopandas `.explore()` method. Interactive maps are suitable for data exploration, dashboards, and web publishing.

## Key Features

### Minimal Map
```python
nz.explore()
```

### Styling
- Color, opacity, fill opacity
- Marker types: `circle_marker` (radius in px, default), `circle` (radius in m), `marker` (PNG icon)
- `style_kwds`: stroke, color, weight, opacity, fill, fillColor, fillOpacity
- `marker_kwds`: radius for circle markers

### Layers
- Multiple layers with names
- Layer control for toggling visibility
- Combine vector and raster layers

### Symbology
- Column-based coloring with legends
- Categorical and continuous color schemes
- Custom colormaps

### Basemaps
- Built-in tiles: 'OpenStreetMap', 'CartoDB positron', 'CartoDB dark_matter'
- Custom tile URLs

### Export
```python
m.save('output/map.html')
```

## Relationship to Wiki

Interactive maps provide the exploration and dashboard layer for geospatial analyses. They complement [[static-maps-python]] for publication-ready output and serve as the frontend for analyses performed with [[python-geospatial-stack]] and [[geospatial-analytics-with-dbt]].
