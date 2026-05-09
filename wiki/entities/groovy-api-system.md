---
type: entity
title: Groovy API System
created: 2026-05-07
updated: 2026-05-07
tags: [api, groovy, grestlet, legacy, geospatial]
related: [legacy-geospatial-api-layer, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, groovy, grestlet]
sources: ["SISTEMA API - SCRIPT GROOVY.md"]
---
# Groovy API System

A dynamic API system built with the Groovy programming language and the Grestlet library. It is deployed at `/geoscripts/opendata/api` and serves geospatial datasets and their items through a hierarchical URL structure.

## Architecture

The system uses path variable routing to determine which resource to serve. It handles content-type negotiation, supporting both `application/json` and `text/html` responses.

### Resource Hierarchy

1. **Landing Page** — Served when no path variable is provided.
2. **Swagger Documentation** — Served when `pathvar1='openapi'`.
3. **Datasets List** — Served when `pathvar1='datasets'`.
   - **Dataset Detail** — Served when `pathvar2={dataset_id}`.
     - **Items List** — Served when `pathvar3='items'`.
       - **Item Data** — Served when `pathvar4={item_id}`.

## Role in Legacy Pipeline

This API system is the **output/consumption layer** for the legacy geospatial data pipeline. It provides programmatic access to the geospatial datasets stored in PostgreSQL after they have been processed by the [[oracle-to-postgresql-gdal-etl]] workflow.

## Related Pages

- [[legacy-geospatial-api-layer]] — The full API consumption layer of the legacy pipeline.
- [[legacy-geospatial-etl-pipeline]] — The ETL pipeline that feeds data into this API.
- [[oracle-to-postgresql-gdal-etl]] — The specific ETL workflow pattern.