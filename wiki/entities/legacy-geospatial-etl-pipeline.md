---
type: entity
title: Legacy Geospatial ETL Pipeline
created: 2026-04-29
updated: 2026-04-29
tags: [etl, gis, geospatial, legacy-architecture]
related: [oracle-to-postgresql-gdal-etl, map-service-performance-issues, geospatial-etl-pipeline-iceberg, etl-pattern, elt-pattern]
sources: ["ETL ATTUALE.md"]
---
# Legacy Geospatial ETL Pipeline

The legacy ETL pipeline for geospatial data processing, documented in [[ETL ATTUALE.md]]. It follows a traditional two-phase ETL pattern: data preparation from Oracle to PostgreSQL via GDAL/OGR Groovy scripts, followed by post-processing for map services, application services, and web clients.

## Architecture

1. **Source:** Oracle database (views and tables)
2. **Transformation:** Groovy scripts orchestrating GDAL/OGR (scheduled or on-demand)
3. **Target:** PostgreSQL database (views and tables)
4. **Consumption:** Map services (performance-critical), application services, HTML/JS web clients

## Known Issues
- Performance bottlenecks in the map service layer
- Integration challenges between cartographic and visualization layers

## Relationship to Modern Stack
This legacy pipeline represents the "as-is" architecture that the wiki's modern patterns ([[geospatial-etl-pipeline-iceberg]], [[duckdb]], [[dremio]], [[dbt]]) aim to replace or evolve. It is a concrete example of the [[etl-pattern]] for geospatial data, contrasting with the [[elt-pattern]] and [[data-lakehouse]] approaches documented elsewhere in the wiki.