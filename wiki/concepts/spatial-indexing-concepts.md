---
type: concept
title: Spatial Indexing Concepts
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, indexing, performance, spatial]
related: [duckdb-spatial-extension, geospatial-performance-patterns, duckdb]
sources: ["Mastering Geospatial Analysis with DuckDB Spatial and MotherDuck.md"]
---
# Spatial Indexing Concepts

Spatial indexing is a specialized data structure technique that enables fast geometric operations (proximity, intersection, containment) by organizing spatial data using multi-dimensional index structures rather than traditional B-tree indexes.

## The Problem

Traditional SQL joins compare values column-by-column. For geospatial data, this approach is catastrophically inefficient. With 1 million points and 100,000 polygons, a naive SQL join would require 100 billion comparisons (1M × 100K), each requiring complex geometric calculations.

## How Spatial Indexes Work

### Minimum Bounding Rectangles (MBRs)

Each geometry is approximated by a simple rectangular bounding box defined by minimum and maximum x/y coordinates. This simplification allows fast overlap/intersection checks without examining the full geometry.

### R-tree Structure

The R-tree (R for Rectangle) organizes space hierarchically:
1. Nearby geometries are grouped into progressively larger bounding boxes
2. The tree structure divides space into nested rectangles
3. Queries traverse the tree, quickly eliminating large areas of non-matching geometries

### GIST Indexes

Generalized Search Tree (GIST) indexes in PostGIS and other databases provide a flexible framework for implementing R-tree-like structures for geometric data types.

## Performance Impact

With a spatial index:
- **Without index:** 100 billion comparisons (1M points × 100K polygons)
- **With index:** ~10 million comparisons (1M grid cell lookups × ~10 nearby polygons)
- **Improvement:** 10,000x faster

## Two-Step Spatial Filtering

A common performance optimization pattern:
1. **Coarse filter:** Use bounding box coordinates (e.g., `longitude BETWEEN x1 AND x2 AND latitude BETWEEN y1 AND y2`) to quickly eliminate non-matching rows
2. **Precise filter:** Apply the exact spatial function (e.g., `ST_Distance_Spheroid`, `ST_DWithin`) only on the filtered subset

## Connections

- [[duckdb-spatial-extension]] — DuckDB's implementation of spatial indexing
- [[geospatial-performance-patterns]] — Practical patterns for optimizing spatial queries
- [[duckdb]] — DuckDB's spatial capabilities