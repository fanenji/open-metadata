---
type: entity
title: OpenStreetMap Data Model
created: 2026-05-07
updated: 2026-05-07
tags: [openstreetmap, geospatial, road-network, osm]
related: [geospatial-analytics-with-dbt, h3-geospatial-indexing, whos-on-first-gazetteer]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# OpenStreetMap Data Model

OpenStreetMap (OSM) is an open-source, collaborative mapping project that provides a free geographic database of the world. Nexar uses OSM as the authoritative road network definition for their geospatial analytics pipeline.

## OSM Entity Model

| Entity | Description |
|---|---|
| **Node** | A single point in space (lat/lon) |
| **Way** | An ordered sequence of nodes (can be a road, river, building boundary) |
| **Relation** | A grouping of ways/nodes with shared meaning |

## Highway Tags

All OSM entities carry key-value tags. The most important for roads is the `highway` tag on Way entities, whose value indicates road type:
- `motorway`, `trunk`, `primary`, `secondary`, `residential`, `service`, etc.

## Road Segments

Road segments are derived as source→destination node pairs from Ways. Road length is computed as the sum of Haversine distances between consecutive nodes. This allows answering map-topology questions like road type distribution by county, independent of GPS data.