---
type: concept
title: Geospatial Analytics with dbt
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, geospatial, h3, snowflake, openstreetmap, whos-on-first]
related: [h3-geospatial-indexing, openstreetmap-data-model, whos-on-first-gazetteer, snowflake-zero-copy-clone, dbt-insert-by-period, snowflake-manual-clustering, nexar]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# Geospatial Analytics with dbt

An architectural pattern for scalable geospatial analytics using dbt, Snowflake, H3, OpenStreetMap, and Who's on First, as demonstrated by [[nexar]].

## Core Insight

By converting all geographic data — GPS samples, road segments, and place boundaries — into H3 integer indexes, every spatial join becomes an integer equality check. Columnar data warehouses (Snowflake, BigQuery, Databricks) are optimized for integer operations, not for polygon geometry.

## Architecture

The geographic dimension layer in dbt follows this dependency graph:

```
Who's on First (raw)         OSM (raw)
       │                         │
  WoF H3 hexagons           OSM nodes + road segments
  (by resolution:            (enriched with H3)
   localities, regions,           │
   counties, countries)           │
       └──────────┬───────────────┘
                  │
           HEX_EGG table
       (road segment × hexagon)
       + locality + region + county
                  │
         Daily rollup models
       (GPS samples / rides / users
        by road segment, per geography)
```

## The HEX_EGG Table

The central join table combining:
- **H3 hexagon** at resolution 12 (precise location on a road)
- **OSM road segment** (road type, direction, length)
- **Who's on First locality, county, region** (human geography)

This is a cartesian product of hexagons × road segments, pre-enriched with all geographic dimensions. It is expensive to build once but makes all downstream queries trivially simple.

## Result

A non-technical analyst can query "how many unique users drove on residential roads in San Francisco last month?" with a simple GROUP BY query — with no knowledge of H3, OSM, or geospatial computation required.