---
type: source
title: "SISTEMA API - SCRIPT GROOVY"
created: 2026-01-15
updated: 2026-05-07
tags: [api, groovy, grestlet, legacy, geospatial]
related: [groovy-api-system, legacy-geospatial-api-layer, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["SISTEMA API - SCRIPT GROOVY.md"]
---
# SISTEMA API - SCRIPT GROOVY

## Summary

A brief architectural note describing a Groovy-based dynamic API system that serves geospatial datasets and their items through a hierarchical URL structure. The system uses the Grestlet library and is deployed at `/geoscripts/opendata/api`. It handles content-type negotiation (JSON/HTML) and routes requests based on path variables to serve a landing page, Swagger documentation, dataset listings, and individual item data.

## Key Points

- **Language/Library**: Groovy with the Grestlet library.
- **Deployment Path**: `/geoscripts/opendata/api`.
- **Content-Type Handling**: Supports `application/json` and `text/html` based on the `Content-Type` header.
- **Path Routing Logic**: Reads path variables to determine the resource to serve.
- **Resource Hierarchy**:
  - `pathvar1=null` → Landing page
  - `pathvar1='openapi'` → Swagger documentation
  - `pathvar1='datasets'` → Datasets list
    - `pathvar2={dataset_id}` → Dataset description + metadata
      - `pathvar3='items'` → Items list
        - `pathvar4={item_id}` → Item data

## Context

This API system is part of the legacy geospatial data pipeline. It serves as the **output/consumption layer** for geospatial data processed by the legacy ETL pipeline (Oracle → GDAL → PostgreSQL). The existing wiki documents the ETL pipeline but lacks documentation of this API layer.

## Open Questions

- Is this API system still in production?
- What authentication/authorization mechanisms exist?
- How does pagination work for large item lists?
- What is the performance profile (latency, throughput)?
- Is there a plan to migrate to a modern API framework (FastAPI, etc.)?