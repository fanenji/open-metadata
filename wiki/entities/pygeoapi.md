---
type: entity
title: pygeoapi
created: 2026-04-12
updated: 2026-04-12
tags: [geospatial, python, api-server, ogc]
related: [ogc-api-standards, geospatial-api-server-comparison, postgis, dremio, duckdb-spatial-extension, geospatial-etl-pipeline-iceberg]
sources: ["pygeoapi - an OGC API to geospatial data - pygeoapi.md"]
---
# pygeoapi

pygeoapi is a Python server implementation of the [[ogc-api-standards|OGC API suite of standards]]. It provides organizations with the capability to deploy a RESTful OGC API endpoint using OpenAPI, GeoJSON, and HTML. The project emerged in 2018 as part of the next generation OGC API efforts.

## OGC Compliance

pygeoapi is certified **OGC Compliant** and is an **OGC Reference Implementation** for multiple OGC API standards:
- OGC API - Features (1.0)
- OGC API - Tiles (1.0)
- OGC API - Environmental Data Retrieval (EDR) (1.0.1)
- OGC API - Processes (1.0)

## Architecture

pygeoapi is built on a robust **plugin framework** that allows:
- Connection to custom data sources (files, services, databases)
- Serving custom output formats
- Implementation of custom processes and workflows
- Deployment via Flask, Django, or any Python web framework

## Deployment

- Installable via pip or git
- Official Docker image available
- UbuntuGIS package support
- Python 3.12 recommended

## Project Status

- Open source (MIT license)
- Hosted on GitHub under the [[geopython]] organization
- [[OSGeo]] Project status
- Featured at FOSS4G conferences

## Connections to Existing Wiki

pygeoapi can serve as the API layer for [[geospatial-etl-pipeline-iceberg]] outputs, connecting to [[postgis]] as a data source. It complements [[dremio]]'s query engine approach by providing a standards-focused API layer for geospatial data serving.