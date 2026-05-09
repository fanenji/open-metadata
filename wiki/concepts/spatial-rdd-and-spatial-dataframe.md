---
type: concept
title: Spatial RDD & Spatial DataFrame
created: 2026-05-06
updated: 2026-05-06
tags: [apache-sedena, big-data, architecture]
related: [apache-sedena, spatial-sql]
sources: ["Analyzing Real Esate Data With Apache Sedona-20260506.md"]
---
# Spatial RDD & Spatial DataFrame

[[spatial-rdd-and-spatial-dataframe]] are the core distributed data structures in [[apache-sedena]]. They extend standard Apache Spark RDDs and DataFrames with specialized support for spatial geometries.

### Key Capabilities:
- **Spatial Indexing**: Enables efficient spatial queries (e.g., point-in-polygon) by organizing geometries in a way that minimizes computation.
- **Spatial Partitioning**: Distributes geometric data across a cluster to optimize parallel processing of large-scale datasets.
- **Geometry Support**: Allows for the storage and manipulation of complex types like `POLYGON`, `MULTIPOLYGON`, and `POINT`.
- **SQL Integration**: Enables the use of [[spatial-sql]] to perform complex geometric operations using standard SQL syntax.