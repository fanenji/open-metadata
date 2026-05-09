---
type: concept
title: HEX_EGG Table Pattern
created: 2026-05-08
updated: 2026-05-08
tags: [geospatial, dbt, h3, data-model, spatial-aggregation, pattern]
related: [hex-egg-table, h3-geospatial-indexing, geospatial-analytics-with-dbt, spatial-bucketing, dbt-insert-by-period, dbt-expectations]
sources: ["research-hexegg-table-2026-05-08.md"]
---
# HEX_EGG Table Pattern

The **HEX_EGG Table Pattern** is a reusable architectural pattern for large-scale geospatial analytics that converts continuous GPS coordinates into discrete [[h3-geospatial-indexing]] hexagonal cells for efficient aggregation and analysis. The pattern bridges raw streaming events and analytical aggregates through a materialized intermediate table.

## Core Principles

1. **Spatial Bucketing**: Convert continuous GPS coordinates into discrete H3 cell IDs, enabling fast equality joins and GROUP BY operations.
2. **Multi-Resolution Materialization**: Store data at multiple H3 resolutions simultaneously to support analysis at different geographic scales.
3. **Incremental Processing**: Use [[dbt]] incremental models (timestamp-based or [[dbt-insert-by-period]]) to handle continuous data streams.
4. **Metadata Enrichment**: Push dbt documentation and test results to the warehouse for surfacing in analytics tools.

## Relationship to Other Concepts

- [[h3-geospatial-indexing]] provides the underlying grid system; the HEX_EGG pattern is a concrete materialization strategy.
- [[geospatial-analytics-with-dbt]] is the broader architectural pattern; HEX_EGG is a canonical implementation example.
- [[spatial-bucketing]] is the general technique; HEX_EGG applies it specifically to H3 hexagons.

## Known Limitations

- The "EGG" acronym lacks a canonical definition — see [[hex-egg-table]] for discussion.
- H3 cells do not align with administrative boundaries, which can misrepresent data.
- High-resolution cells at scale require careful partitioning and clustering.