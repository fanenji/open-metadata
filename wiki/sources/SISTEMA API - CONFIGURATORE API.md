---
type: source
title: "SISTEMA API - CONFIGURATORE API"
created: 2026-01-15
updated: 2026-01-15
tags: [api, geospatial, metadata-driven, ogc]
related: [ogc-api-features, metadata-driven-api-configuration, api-configurator-system, legacy-geospatial-etl-pipeline, data-download-service]
sources: ["SISTEMA API - CONFIGURATORE API.md"]
---
# SISTEMA API - CONFIGURATORE API

## Description

A system for configuring read-only APIs from metadata stored in databases or JSON files. The document describes the API structure following the OGC API - Features standard, with a landing page, SwaggerUI, conformance endpoint, dataset listing, and item access endpoints.

## Key Points

- Read-only API system configured from metadata (database or JSON)
- Follows OGC API - Features standard structure
- Reference implementation uses GeoServer
- Endpoints: Landing Page, SwaggerUI, Conformance, Datasets, Items
- Metadata endpoints: `/conformance`, `/datasets`, `/datasets/{datasetId}`
- Data endpoints: `/datasets/{datasetId}/items`, `/datasets/{datasetId}/items/{itemId}`

## Reference URLs

- Landing Page: `http://localhost:8080/geoservices/apps/ogc-api/LandingPage.html`
- SwaggerUI: `http://geoservizi.datasiel.net:8083/geoserver/ogc/features/openapi?f=text%2Fhtml`
- API Definition: `http://geoservizi.datasiel.net:8083/geoserver/M1237/ogc/features/openapi?f=application%2Fvnd.oai.openapi%2Bjson%3Bversion%3D3.0`

## Open Questions

- What is the exact metadata schema (database tables or JSON structure)?
- Is this intended to replace or complement the [[data-download-service]]?
- What query engine or storage layer backs the API?
- Is the API for internal, partner, or public consumption?
- How does authentication/authorization work?