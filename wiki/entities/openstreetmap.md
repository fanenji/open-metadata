---
type: entity
title: OpenStreetMap (OSM)
created: 2026-05-06
updated: 2026-05-06
tags: [mapping, road-network, geospatial]
related: [geospatial-data-stack, spatial-pre-processing-pattern]
sources: ["Complex geospatial analytics with dbt - Summary.md"]
---
# OpenStreetMap (OSM)

**OpenStreetMap (OSM)** is an authoritative, open-source source for road network topology. In geospatial data engineering, it is used to provide the structural context (nodes, ways, and relations) that raw GPS data lacks.

### Key Data Entities
- **Node**: A single point in space (latitude/longitude).
- **Way**: An ordered sequence of nodes representing features like roads, rivers, or boundaries.
- **Relation**: A grouping of ways/nodes with shared meaning.

By parsing OSM data, engineers can derive road segments and road lengths, allowing for topological queries (e.g., "how many miles of residential roads are covered?") that are independent of raw GPS traces.
