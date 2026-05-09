---
type: concept
title: Automated Geometry Validation
created: 2024-05-22
updated: 2024-05-22
tags: [data-quality, spatial, postgis]
related: [postgis]
sources: ["CONVERSIONI GROOVY -> PYTHON.md"]
---
# Automated Geometry Validation

A data quality pattern where the ETL process uses PostGIS functions (such as `ST_IsValid` and `ST_GeometryType`) to automatically repair or flag invalid geometries (e.g., self-intersecting polygons) during the ingestion process.