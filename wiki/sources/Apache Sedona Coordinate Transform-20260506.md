---
type: source
title: Apache Sedona Coordinate Transform
created: 2026-05-06
updated: 2026-05-06
tags: [sedona, coordinate, mapping, gis]
related: [apache-sedona, proj4j, spatial-pre-processing-pattern, geopandas]
sources: ["Apache Sedona Coordinate Transform-20260506.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Apache Sedona Coordinate Transform

Technical discussion regarding the limitations of Coordinate Reference System (CRS) transformations within Apache Sedona, specifically focusing on the dependency on Proj4j and the inability to process `.gsb` grid files for high-precision transformations.

The source highlights that while `ST_Transform` is available via `Proj4j`, advanced transformations requiring grid files (like NADCON or NTv2) must be handled via external pre-processing using tools like GDAL or GeoPandas.