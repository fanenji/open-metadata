---
type: source
title: Apache Sedona Coordinate Transform
created: 2026-02-13
updated: 2026-02-13
tags: [sedona, coordinate, mapping, gis]
sources: ["Apache Sedona Coordinate Transform.md"]
authors: [ChatGPT]
year: 2026
url: "https://chatgpt.com/c/6808d8b6-ed20-8008-bf31-154247508cc4"
venue: "AI Conversation"
---
# Apache Sedona Coordinate Transform

Technical discussion regarding the limitations of coordinate transformations in Apache Sedona due to its reliance on the Proj4j library.

Key points:
- Apache Sedona uses **Proj4j** for CRS transformations.
- It does **not** support `.gsb` grid files (e.g., NADCON, NTv2) for high-precision transformations.
- High-precision requirements may necessitate a **pre-processing pattern** using tools like **GDAL/OGR** or **GeoPandas/Pyproj** before data ingestion into the Spark/Sedona pipeline.