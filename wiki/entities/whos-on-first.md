---
type: entity
title: Who's on First
created: 2026-05-06
updated: 2026-05-06
tags: ["gazetteer", "geography", "spatial-id", "geospatial", "dataset"]
related: ["h3-spatial-indexing", "geospatial-data-stack", "geospatial-data-intelligance-layer"]
sources: ["Complex geospatial analytics with and dbt - Summary.md", "Complex geospatial analytics with dbt - Video Transcript.md"]
---
# Who's on First

**Who's on First (WOF)** is a gazetteer and a collection of geographic identifiers. It provides stable, hierarchical metadata for places (countries, regions, cities, etc.) using GeoJSON shapes.

### Key Benefits
* **Stable Identifiers**: Replaces ambiguous place names with unique, persistent IDs, preventing errors caused by duplicate names (e.g., multiple "Detroits").
* **Hierarchical Context**: Allows for easy grouping and rollups (e.g., aggregating data by city, then by state, then by country).
* **Semantic Enrichment**: Provides additional metadata such as population, which can be used to filter or weight geospatial queries.
