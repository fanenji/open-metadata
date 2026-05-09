---
type: entity
title: Oracle to PostgreSQL GDAL ETL
created: 2026-04-29
updated: 2026-04-29
tags: [etl, gis, geospatial, gdal, oracle, postgresql]
related: [legacy-geospatial-etl-pipeline, map-service-performance-issues, geospatial-etl-pipeline-iceberg, etl-pattern]
sources: ["ETL ATTUALE.md"]
---
# Oracle to PostgreSQL GDAL ETL

A specific ETL workflow pattern documented in [[ETL ATTUALE.md]] that uses Groovy scripts with GDAL/OGR to transform geospatial data from Oracle source tables/views into PostgreSQL target tables/views.

## Components
- **Source:** Oracle database (ORA)
- **Transformation Engine:** GDAL/OGR orchestrated via Groovy scripts
- **Target:** PostgreSQL database (PG)
- **Scheduling:** Scheduled or on-demand execution
- **Optimizations:** Caching and performance improvements
- **Monitoring:** Notifications and logging

## Context
This pattern is part of the [[legacy-geospatial-etl-pipeline]] and represents the traditional ETL approach that the wiki's modern stack ([[geospatial-etl-pipeline-iceberg]], [[duckdb]], [[dremio]]) aims to modernize.