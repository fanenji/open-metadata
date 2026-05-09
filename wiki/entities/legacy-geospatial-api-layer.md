---
type: entity
title: Legacy Geospatial API Layer
created: 2026-05-07
updated: 2026-05-07
tags: [api, legacy, geospatial, consumption-layer]
related: [groovy-api-system, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["SISTEMA API - SCRIPT GROOVY.md"]
---
# Legacy Geospatial API Layer

The API consumption layer of the legacy geospatial data pipeline. It provides programmatic access to geospatial datasets and their items, serving as the output interface for data processed by the [[oracle-to-postgresql-gdal-etl]] workflow.

## Components

- **[[groovy-api-system]]** — The primary API implementation, built with Groovy and Grestlet, deployed at `/geoscripts/opendata/api`.

## Resource Hierarchy

The API exposes a four-level navigation structure:

1. Landing page
2. Swagger/OpenAPI documentation
3. Datasets list → individual dataset detail
4. Items list → individual item data

## Related Pages

- [[legacy-geospatial-etl-pipeline]] — The ETL pipeline that feeds data into this API layer.
- [[groovy-api-system]] — The specific API implementation.