---
type: concept
title: OGC API Standards
created: 2026-04-12
updated: 2026-04-12
tags: [geospatial, standards, ogc, api]
related: [pygeoapi, geospatial-api-server-comparison, formati-e-standard, geospatial-etl-pipeline-iceberg]
sources: ["pygeoapi - an OGC API to geospatial data - pygeoapi.md"]
---
# OGC API Standards

The OGC API suite of standards is the next generation of RESTful geospatial web service standards from the Open Geospatial Consortium (OGC). These standards replace the older OGC Web Service (OWS) standards (WMS, WFS, WCS) with modern web API patterns using OpenAPI, GeoJSON, and HTML.

## Key Standards

- **OGC API - Features**: Access to geospatial feature data (replaces WFS)
- **OGC API - Tiles**: Access to tiled geospatial data (replaces WMTS)
- **OGC API - Environmental Data Retrieval (EDR)**: Access to environmental data along spatial/temporal trajectories
- **OGC API - Processes**: Execution of geospatial processing workflows (replaces WPS)
- **OGC API - Records**: Catalog and discovery of geospatial resources (replaces CSW)

## Relevance to Data Platforms

OGC API standards provide a standardized way to serve geospatial data from modern data lakehouses and analytical platforms. They complement technologies like [[iceberg-geospatial-support]] and [[geoarrow]] by providing the API layer for data consumption.

## OGC Reference Implementation

An OGC Reference Implementation is an official certification that a software implementation correctly implements one or more OGC standards. [[pygeoapi]] holds this certification for multiple OGC API standards, validating its compliance and interoperability.