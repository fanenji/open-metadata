---
type: entity
title: Who's on First Gazetteer
created: 2026-05-07
updated: 2026-05-07
tags: [gazetteer, geospatial, place-identifiers, open-data]
related: [geospatial-analytics-with-dbt, openstreetmap-data-model, h3-geospatial-indexing]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# Who's on First Gazetteer

Who's on First is an open-source gazetteer of places, providing stable integer IDs and precise GeoJSON shapes for geographic entities. Nexar uses it instead of relying on city/country names, which are ambiguous.

## Key Features

| Feature | Value |
|---|---|
| **Stable integer IDs** | Unique, unambiguous foreign keys — no name collisions |
| **Precise GeoJSON shapes** | Full polygon boundaries (not just bounding boxes) |
| **Administrative hierarchy** | Countries → Regions → Counties → Localities (cities/towns) |
| **Population metadata** | Filter by population threshold |
| **Git-based distribution** | Clone a repo per country/region; each place is a GeoJSON file |

## Importance

Using stable IDs as foreign keys between tables is far more reliable than using names. The hierarchy allows grouping at any administrative level, enabling queries like "data in the 5 NYC boroughs" or "all cities in California."