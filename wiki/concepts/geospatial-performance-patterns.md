---
type: concept
title: Geospatial Performance Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, performance, optimization, spatial]
related: [spatial-indexing-concepts, duckdb-spatial-functions-reference, duckdb-spatial-extension]
sources: ["Mastering Geospatial Analysis with DuckDB Spatial and MotherDuck.md"]
---
# Geospatial Performance Patterns

Optimization patterns for efficient geospatial queries, as demonstrated in the DuckDB Spatial analysis of the Foursquare OS Places dataset.

## Two-Step Spatial Filtering

The most important performance pattern for geospatial queries. It separates the filtering process into two stages:

### Step 1: Coarse Bounding Box Filter
Use simple numeric comparisons on latitude/longitude columns to quickly eliminate non-matching rows. This leverages standard B-tree indexes and avoids expensive geometric calculations.

```sql
AND longitude BETWEEN 7.0 AND 7.5
AND latitude BETWEEN 46.9 AND 47.3
```

### Step 2: Precise Spatial Filter
Apply the computationally expensive spatial function only on the pre-filtered subset.

```sql
AND ST_Distance_Spheroid(
    ST_Point(longitude, latitude), 
    center
) <= 2000
```

## Metadata Pre-filtering

Filter on non-spatial metadata columns before applying spatial operations to reduce the dataset size:

```sql
AND country = 'CH'  -- Filter by country first
AND date_closed IS NULL  -- Filter by status
```

## Spatial Index Utilization

Ensure spatial indexes are available and used. DuckDB Spatial automatically uses spatial indexes when available, dramatically reducing the number of geometric comparisons.

## Self-Join Optimization

When finding pairs of nearby points, use `a.fsq_place_id < b.fsq_place_id` to ensure each pair is counted only once, and use `ST_DWithin` instead of `ST_Distance` for proximity checks:

```sql
JOIN nearby_stores b 
  ON a.fsq_place_id < b.fsq_place_id
  AND ST_DWithin(a.location, b.location, 2)
```

## Connections

- [[spatial-indexing-concepts]] — The theoretical foundation for these patterns
- [[duckdb-spatial-functions-reference]] — Functions used in these patterns
- [[duckdb-spatial-extension]] — DuckDB's implementation