---
type: source
title: "Analyzing Real Estate Data With Apache Sedona"
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, spark, tutorial, real-estate]
related: [apache-sedona, wherobots-cloud, geospatial-data-stack]
authors: [Ben Pruden]
year: 2023
url: "https://wherobots.com/blog/analyzing-real-estate-data-sedonadb/?s=09"
venue: "Wherobots Blog"
sources: ["Analyzing Real Estate Data With Apache Sedona.md"]
---
# Analyzing Real Estate Data With Apache Sedona

A tutorial demonstrating how to perform large-scale geospatial analysis using **Apache Sedona** and **Wherobots Cloud**. The workflow involves joining Zillow Home Value Index (ZHVI) CSV data with Natural Earth Shapefile boundaries to visualize changes in median home values across US counties.

Key highlights include:
- Using **Spatial RDDs** and **Spatial DataFrames** for distributed spatial processing.
- Executing **Spatial SQL** joins between attribute data (CSV) and geometry data (Shapefile).
- Generating interactive visualizations using `SedonaPyDeck`.
- Creating publication-quality static choropleth maps using `GeoPandas` and `Matplotlib` with the **Jenks-Caspall** binning method and **Albers Equal Area** projection.