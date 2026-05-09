---
type: entity
title: GeoServer
created: 2026-05-07
updated: 2026-05-07
tags: [geospatial, server, ogc, api]
related: [ogc-api-features, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, api-configurator-system]
sources: ["SISTEMA API - CONFIGURATORE API.md"]
---
# GeoServer

GeoServer is an open-source server for sharing geospatial data. It implements OGC standards including WMS, WFS, WCS, and OGC API - Features. In the context of this wiki, GeoServer serves as the reference implementation for the [[api-configurator-system]] and is part of the [[legacy-geospatial-etl-pipeline]] serving layer.

## Role in the Data Platform

- Serves as the reference implementation for OGC API - Features
- Hosted at Datasiel for the example configuration
- Provides the landing page, SwaggerUI, and dataset/item endpoints
- Part of the legacy geospatial data serving infrastructure