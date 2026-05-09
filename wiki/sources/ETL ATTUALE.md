---
type: source
title: "ETL ATTUALE: Current Geospatial ETL Pipeline Architecture"
created: 2026-01-15
updated: 2026-04-29
tags: [etl, gis, geospatial, legacy-architecture]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, map-service-performance-issues, geospatial-etl-pipeline-iceberg, etl-pattern]
sources: ["ETL ATTUALE.md"]
---
# ETL ATTUALE: Current Geospatial ETL Pipeline Architecture

This document outlines the current (as-is) ETL pipeline for geospatial data processing. It describes a two-phase architecture: data preparation from Oracle to PostgreSQL via GDAL/OGR Groovy scripts, followed by post-processing for map services, application services, and web clients.

## Structure

The pipeline consists of two main phases:

### 1. Preparazione Dati (Data Preparation)
- **Source:** Oracle database views and tables
- **Transformation:** Groovy scripts using GDAL/OGR (scheduled or on-demand)
- **Target:** PostgreSQL database views and tables
- **Optimizations:** Caching and other performance improvements
- **Monitoring:** Notifications and logging

### 2. Post Processing
- **Map Services:** Performance-critical layer with known issues
- **Application Services:** Downstream application consumption
- **Web Clients:** HTML/JS frontend with cartographic and visualization integration concerns

## Known Issues
- **Performance Criticality (CRITICITÀ PRESTAZIONI):** The map service layer experiences performance bottlenecks.
- **Integration Challenges (INTEGRAZIONE CARTO / VIZ):** Integration between cartographic and visualization layers is a concern.

## Context
This document represents the legacy architecture that the wiki's modern patterns (Iceberg, DuckDB, Dremio, dbt) aim to replace or evolve. It provides a baseline "as-is" architecture for comparison with modern alternatives.