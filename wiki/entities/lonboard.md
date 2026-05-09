---
type: entity
title: lonboard
created: 2026-04-29
updated: 2026-05-07
tags: [geospatial, python, visualization, deck-gl, geoarrow, tool]
related: [deck-gl, geoarrow-layers, geoarrow, geoparquet-vs-iceberg-metadata, kyle-barron, development-seed, geoparquet, hybrid-geospatial-systems]
sources:
  - "GeoParquet and GeoArrow in deck.gl  Kyle Barron  Cloud Engineer at Development Seed.md"
  - "Interview with Kyle Barron on GeoArrow and GeoParquet, and the Future of Geospatial Data Analysis.md"
---
# lonboard

lonboard is a Python geospatial visualization library developed by [[kyle-barron]] at [[Development Seed]] that creates interactive [[deck.gl]] maps from GeoDataFrames (GeoPandas) or Shapely geometry arrays. It bridges Python spatial analysis with browser-based rendering using [[GeoArrow]] and [[GeoParquet]] serialization. By leveraging GeoParquet's compression, lonboard efficiently moves data from Python to JavaScript, minimizing network data transfer even in non-cloud-native use cases. It is a key component of Kyle Barron's vision for [[hybrid-geospatial-systems]].

## How It Works

1. A GeoDataFrame is serialized to GeoArrow and then to a GeoParquet binary buffer. GeoParquet's compression reduces the data size for transfer.
2. The buffer is sent from the Python kernel to the browser via a Jupyter notebook websocket.
3. On the JavaScript side, the GeoParquet buffer is parsed into a GeoArrow table.
4. The GeoArrow table is passed to deck.gl's binary API for direct GPU rendering.

## Performance

- 3M points rendered in <3 seconds (local machine).
- Color updates for 3M points in <1 second (only the color buffer is re-sent).
- 50x+ faster than alternatives like ipy-leaflet (3.5 min, crashed) and folium (2.5 min, crashed).

## Caveats

- First released as 0.1 in December 2023.
- Benchmarks are local-machine only; remote environments (Colab, Binder) require network transfer of the GeoParquet file.
- Tooltips and multi-layer support were still in development at launch.