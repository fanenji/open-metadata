---
type: concept
title: API Configurator System
created: 2026-05-07
updated: 2026-05-07
tags: [api, configuration, metadata, geospatial, data-platform]
related: [metadata-driven-api-configuration, ogc-api-features, data-download-service, legacy-geospatial-etl-pipeline, geoserver]
sources: ["SISTEMA API - CONFIGURATORE API.md"]
---
# API Configurator System

The API Configurator System is a component of the Data Platform that generates read-only APIs from metadata stored in databases or JSON files. It follows the [[ogc-api-features]] standard and provides a structured way to expose geospatial datasets.

## Endpoint Structure

### Metadata Endpoints
- `/conformance` — Lists supported standards
- `/datasets` — Lists available datasets
- `/datasets/{datasetId}` — Description and metadata for a specific dataset

### Data Endpoints
- `/datasets/{datasetId}/items` — List of features in a dataset
- `/datasets/{datasetId}/items/{itemId}` — Single feature data

### Documentation
- Landing Page — Entry point with title, description, links
- SwaggerUI — Interactive API documentation (HTML and JSON)

## Relationship to Other Systems

- **[[data-download-service]]**: Complementary serving subsystem — this provides API access, the download service provides file-based access
- **[[legacy-geospatial-etl-pipeline]]**: The API system serves data produced by these pipelines
- **[[geoserver]]**: Reference implementation used in the example configuration

## Open Questions

- What is the exact metadata schema (database tables or JSON structure)?
- Is this intended to replace or complement the [[data-download-service]]?
- What query engine or storage layer backs the API (Dremio, DuckDB, PostgreSQL, Iceberg)?
- Is the API intended for internal consumption, external partners, or public access?
- How does authentication/authorization work?