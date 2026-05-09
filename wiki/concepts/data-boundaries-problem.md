type: concept
title: Data Boundaries Problem
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, architecture, cloud-native, data-movement]
related: [hybrid-geospatial-systems, kyle-barron, geoarrow, geoparquet, cloud-native-geospatial-workflow]
sources: ["Interview with Kyle Barron on GeoArrow and GeoParquet, and the Future of Geospatial Data Analysis.md"]
---
# Data Boundaries Problem

The data boundaries problem refers to the fundamental challenge of moving data between local and cloud domains in geospatial data analysis. Both local devices and cloud compute are powerful, but moving data between these two domains is very slow due to network bandwidth constraints.

## Key Questions

- When do you need to move data across boundaries?
- How can you minimize what data you need to move?
- How can you make the movement most efficient when you actually do need to move it?

## Relevance

This problem is central to the design of [[hybrid-geospatial-systems]]. [[kyle-barron]] identifies it as a fascinating architectural challenge that drives the adoption of cloud-native formats like [[geoparquet]] and in-memory formats like [[geoarrow]], which enable efficient data movement and selective data fetching.