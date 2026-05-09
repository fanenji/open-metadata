---
type: concept
title: H3 Geospatial Indexing
created: 2026-05-07
updated: 2026-05-07
tags: [h3, geospatial, indexing, hexagonal-grid, uber]
related: [geospatial-analytics-with-dbt, openstreetmap-data-model, whos-on-first-gazetteer]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# H3 Geospatial Indexing

H3 is Uber's open-source hierarchical hexagonal grid system for the Earth's surface. It is the core enabler of Nexar's geospatial analytics approach, converting expensive spatial operations into fast integer equality checks.

## Why Hexagons?

Point-in-polygon queries are computationally expensive in any data warehouse. H3 solves this by replacing every geographic point or polygon with an **integer** (the hexagon ID). Equality checks on integers are orders of magnitude faster than spatial operations, especially in columnar storage systems like Snowflake.

## Grid Structure

- The Earth is divided into hexagons at multiple resolutions (levels 0–15)
- Each hexagon has 7 sub-hexagons at the next finer resolution
- Every location maps to exactly one hexagon at any resolution
- Parent hexagons can be computed from child hexagons using **bit-shift operations** (no lookup required)

## Resolutions and Use Cases

| Resolution | Approx. Edge Length | Use Case |
|---|---|---|
| 8 | ~460m | US States |
| 10 | ~65m | Cities |
| 12 | ~9–20m | Individual GPS samples / road segments |

## Polyfill

Converting a geographic polygon to a set of H3 hexagons at a chosen resolution. Instead of a point-in-polygon query, you perform a set membership check:

```sql
-- Instead of: ST_CONTAINS(california_polygon, point)
-- Do: h3_index IN (SELECT h3_index FROM california_hexagons)
```

## H3 UDFs in dbt

Traversing between resolutions is done via bitwise operations, implemented as SQL UDFs managed in dbt:

```sql
CREATE FUNCTION h3_to_parent_8(h3_index BIGINT)
RETURNS BIGINT AS
$$
  (h3_index >> N) << N
$$;
```