---
type: source
title: Geocomputation with Python
created: 2026-04-29
updated: 2026-04-29
tags: [python, gis, geocomputation, geopandas, rasterio, reference]
related: [python-geospatial-stack, raster-data-model, coordinate-reference-systems, map-algebra, raster-vector-interactions, static-maps-python, interactive-maps-python, geospatial-analytics-with-dbt, geoarrow]
sources: ["Geocomputation with Python.md"]
authors: [Michael Dorman, Anita Graser, Jakub Nowosad, Robin Lovelace]
year: 2025
url: https://py.geocompx.org/
venue: CRC Press
---
# Geocomputation with Python

*Dorman, M., Graser, A., Nowosad, J., & Lovelace, R. (2025). Geocomputation with Python. CRC Press.*

An introductory textbook on reproducible geographic data analysis with open source Python tools. Published by Chapman & Hall/CRC in their Python Series. The book provides cohesive coverage of both vector and raster geographic data models, emphasizing the [[python-geospatial-stack]] (geopandas, rasterio, shapely, pyproj) and the Free and Open Source Software for Geospatial (FOSS4G) movement.

## Key Topics

- **[[raster-data-model]]** — Grid-based representation of continuous surfaces, with metadata (transform, CRS) and numpy array values.
- **[[coordinate-reference-systems]]** — Geographic vs. projected CRS, EPSG codes, WKT, Proj-strings, and selection criteria.
- **[[map-algebra]]** — Tomlin's four operation types: Local, Focal, Zonal, and Global.
- **[[raster-vector-interactions]]** — Cropping, masking, extraction, rasterization, and vectorization.
- **Reprojection** — Transforming geographic data between CRS for both vector (`.to_crs()`) and raster (`rasterio.warp.reproject`) data.
- **[[static-maps-python]]** — Matplotlib-based mapping with symbology, labels, basemaps, and faceted maps.
- **[[interactive-maps-python]]** — Leaflet-based mapping via geopandas `.explore()`.

## Connections to Existing Wiki

This source provides foundational Python geospatial operations that complement the wiki's existing coverage of [[geospatial-analytics-with-dbt]] (which focuses on dbt/H3/Snowflake) and [[geoarrow]] (columnar in-memory format). It fills significant gaps in raster data processing, CRS theory, and map creation that were previously absent from the wiki.

## Software Stack

- Python 3.11.4
- geopandas 1.0.1, rasterio 1.3.10, shapely 2.0.5
- numpy 2.0.1, pandas 2.2.2, matplotlib 3.9.0
- Additional: contextily, osmnx, cartopy, topojson, folium, rasterstats, scipy
