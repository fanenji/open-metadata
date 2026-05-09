---
type: concept
title: Hex-Road Segment Join
created: 2026-05-06
updated: 2026-05-06
tags: [geospatial, dbt, optimization]
related: [h3-spatial-indexing, spatial-to-integer-conversion, geospatial-data-stack]
sources: ["Complex geospatial analytics with dbt - Video Transcript.md"]
---
# Hex-Road Segment Join

The **Hex-Road Segment Join** is a specialized geospatial engineering pattern used to combine high-resolution spatial indexing (like H3) with topological road network data (like OpenStreetMap).

### The Pattern
The pattern involves creating a "bridge" table (often called a `hex_road_hex` table) that represents the Cartesian product of H3 hexagons and road segments.

1. **H3 Layer**: Provides a granular, integer-based spatial index for efficient point-in-polygon queries.
2. **Road Segment Layer**: Provides topological information (road type, directionality, length) from OSM.
3. **The Join**: By mapping each road segment to the H3 hexagons it intersects, queries can be performed using simple integer joins.

### Benefits
* **Performance**: Replaces expensive `ST_Intersects` or `ST_Contains` operations with high-performance integer equality checks.
* **Multi-Granularity**: Enables analysts to query road data at different spatial resolutions (e.g., looking at traffic at a street level vs. a city level) using the same underlying structure.
