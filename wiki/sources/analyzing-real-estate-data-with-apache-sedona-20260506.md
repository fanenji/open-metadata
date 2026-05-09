---
type: source
title: Analyzing Real Estate Data With Apache Sedona
created: 2026-05-06
updated: 2026-05-06
authors: [Ben Pruden]
year: 2023
url: "https://wheroborts.com/blog/analyzing-real-estate-data-sedonadb/?s=09"
venue: "Wherobots Blog"
tags: [geospatial, apache-sedona, real-estate, tutorial]
sources: ["Analyzing Real Estate Data With Apache Sedona-20260506.md"]
---
# Analyzing Real Estate Data With Apache Sedona

A tutorial demonstrating how to analyze real estate data using [[apache-sedona]] and [[wherobots-cloud]]. The workflow involves ingesting Zillow Home Value Index (ZHVI) CSV data and Natural Earth Shapefiles to calculate and visualize property value changes across US counties using [[geospatial-analysis-techniques]] like choropleth mapping.

Key components include:
- Using [[spatial-join-patterns]] to link attribute data with geometries.
- Utilizing [[geopandas]] and [[matplotlib]] for static visualization.
- Leveraging [[sedonapydeck]] for interactive maps.

Note: There is a technical discrepancy in the source where the text recommends an equal-area projection, but the code implements Web Mercator (EPSG:3857).