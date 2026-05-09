---
type: source
title: "Complex Geospatial Analytics with dbt — Summary"
created: 2026-05-07
updated: 2026-05-07
tags: [geospatial, dbt, h3, snowflake, openstreetmap, whos-on-first, map-matching]
related: [h3-geospatial-indexing, geospatial-analytics-with-dbt, openstreetmap-data-model, whos-on-first-gazetteer, snowflake-zero-copy-clone, dbt-insert-by-period, snowflake-manual-clustering]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
authors: [Assaf Lavi]
year: 2022
url: "https://www.youtube.com/watch?v=UCEFHXUBqr0"
venue: "Big Things Conference"
---
# Complex Geospatial Analytics with dbt — Summary

A summary of Assaf Lavi's (Principal Engineer @ Nexar) talk at Big Things Conference 2022, describing how Nexar uses dbt, Snowflake, H3, OpenStreetMap, and Who's on First to perform scalable geospatial analytics on GPS data from ~500,000 dashcams.

## Key Techniques

- **H3 hexagonal indexing** — converting all geographic data to integer indexes, replacing expensive spatial joins with fast integer equality checks
- **HEX_EGG table** — a central join table combining H3 hexagons, OSM road segments, and Who's on First geography, enabling simple downstream queries
- **Zero-copy cloning** — Snowflake feature used for fast dev environment setup
- **Insert by period** — advanced dbt incremental strategy for large backfills
- **Manual clustering keys** — Snowflake optimization for predictable query patterns

## Core Insight

By converting GPS samples, road segments, and place boundaries into H3 integer indexes, every spatial join becomes an integer equality check, enabling columnar data warehouses to perform geospatial analytics at scale.