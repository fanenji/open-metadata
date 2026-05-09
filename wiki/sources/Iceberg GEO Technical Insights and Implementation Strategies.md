---
type: source
title: "Source: Iceberg GEO Technical Insights and Implementation Strategies.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["Iceberg GEO Technical Insights and Implementation Strategies.md"]
tags: []
related: []
---

# Source: Iceberg GEO Technical Insights and Implementation Strategies.md

# Analysis: Iceberg GEO Technical Insights and Implementation Strategies

## Key Entities

### Central Entities
- **Apache Iceberg** — Open table format; central subject. Likely exists in wiki (see `[[iceberg-geospatial-support]]`, `[[iceberg-table-versioning]]`).
- **GeoParquet** — Precursor project (2022) that standardized spatial data exchange. Exists in wiki (`[[geoparquet-vs-iceberg-metadata]]`).
- **Wherobots** — Company driving Iceberg GEO development, provides compute engine. New entity.
- **Ben Pruden** — Author, Wherobots employee. New entity.
- **Havasu** — Wherobots' production-ready Iceberg extension for spatial data (2023). New entity.
- **Apache Sedona** — Spatial compute engine mentioned for upcoming demo. Likely new to wiki.

### Peripheral Entities
- **CARTO, Planet, Apple, Databricks, Snowflake** — Community collaborators on Iceberg GEO proposal. Some may exist in wiki.
- **GeoLake** — Early design exploration project. New entity.
- **Apache Polaris, AWS Glue, Hive Metastore** — Catalog systems needing adaptation. Some may exist in wiki.

## Key Concepts

- **Iceberg GEO** — Native spatial data types (geometry, geography) integrated into Apache Iceberg. **New concept** that extends existing `[[iceberg-geospatial-support]]`.
- **Geometry vs. Geography Types** — Planar (flat surface) vs. ellipsoidal (Earth's curvature) spatial representations. **New detail** for wiki.
- **Edge Interpolation Algorithms** — Six methods (Planar, Spherical, Vincenty, Thomas, Andoyer, Karney) for defining edges between points. **New concept**.
- **WKB Encoding** — ISO Well-Known Binary format for spatial objects, following OGC Simple Feature Access v1.2.1. **New detail**.
- **Antimeridian Bounding** — Special handling for objects crossing ±180° longitude, where lower bound > upper bound. **New concept**.
- **Z-Ordering for Spatial Data** — Using H3/S2 indices for spatial clustering. Extends existing `[[h3-geospatial-indexing]]`.
- **Havasu-to-Native Migration** — Transition path from Wherobots' extension to native Iceberg GEO. **New concept**.

## Main Arguments & Findings

1. **Native Iceberg GEO is superior to extensions** — Integrating spatial types directly into Iceberg (vs. Havasu extension) ensures broader ecosystem compatibility without modifications.
2. **Two-type distinction is necessary** — Geometry (planar) vs. Geography (ellipsoidal) addresses varying engine capabilities and use cases.
3. **WKB encoding with longitude-latitude order** — Aligns with GeoPandas, Apache Sedona, Google Maps standards.
4. **CRS flexibility** — Supports both SRID and PROJJSON, with geography restricted to geographic CRS only.
5. **Bounds optimization for antimeridian** — Correctly handles Fiji-like cases where naive min/max fails.

**Evidence strength**: Strong — based on community consensus (multiple companies), merged PR in Apache Iceberg, and reference implementations (Havasu, GeoLake).

## Connections to Existing Wiki

### Strengthens/Extends:
- `[[iceberg-ge
