---
type: entity
title: stac-fastapi
created: 2026-04-29
updated: 2026-04-29
tags: [stac, api, fastapi, python, geospatial]
related: [stac-server-implementation, pgstac, pystac, cloud-optimized-geotiff-cog, raster-cataloging-strategy]
sources: ["ETL RASTER.md"]
---
# stac-fastapi

`stac-fastapi` is a popular Python framework for building STAC (SpatioTemporal Asset Catalog) API servers. It is built on FastAPI and Pydantic, providing a robust, standards-compliant implementation for serving geospatial asset metadata.

## Backend Options

- **`stac-fastapi.pgstac`:** Uses PostgreSQL/PostGIS with the `pgstac` extension as the backend. This is the recommended option for production deployments, offering high performance and scalability for large catalogs.
- **`stac-fastapi.elasticsearch`:** Uses Elasticsearch as the backend, suitable for complex text queries combined with spatial/temporal searches.
- **`stac-fastapi.memory`:** In-memory backend for testing or very small catalogs (non-persistent).
- **Custom Backend:** The framework supports implementing custom backends.

## Deployment

The recommended deployment pattern is as a containerized application on Kubernetes, behind a reverse proxy (Nginx/Traefik), using Gunicorn as the ASGI server for production workloads.
