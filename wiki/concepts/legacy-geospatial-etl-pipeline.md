---
type: concept
title: Legacy Geospatial ETL Pipeline Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [etl, gis, geospatial, legacy-architecture, architectural-pattern]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, map-service-performance-issues, geospatial-etl-pipeline-iceberg, etl-pattern, elt-pattern, push-vs-pull-ingestion]
sources: ["ETL ATTUALE.md"]
---
# Legacy Geospatial ETL Pipeline Architecture

A traditional two-phase ETL pattern for geospatial data processing, documented in [[ETL ATTUALE.md]]. This architecture represents the "as-is" state that the wiki's modern stack aims to replace.

## Phase 1: Data Preparation
- Extract from Oracle (source views/tables)
- Transform via GDAL/OGR orchestrated by Groovy scripts
- Load into PostgreSQL (target views/tables)
- Apply optimizations (caching)
- Monitor via notifications and logging

## Phase 2: Post Processing
- Serve data through map services (performance-critical)
- Support application services
- Deliver to HTML/JS web clients

## Known Weaknesses
- Performance bottlenecks in map service layer
- Integration challenges between cartographic and visualization layers
- Traditional ETL pattern (not ELT), limiting flexibility and scalability

## Contrast with Modern Patterns
This legacy pattern contrasts with the wiki's modern approaches:
- [[etl-pattern]] vs [[elt-pattern]]: Legacy uses ETL; modern stack favors ELT
- [[push-vs-pull-ingestion]]: Legacy uses scheduled/on-demand scripts
- [[geospatial-etl-pipeline-iceberg]]: Modern alternative using Iceberg, Spark, and GeoParquet
- [[data-lakehouse]]: Legacy uses traditional RDBMS; modern uses lakehouse architecture