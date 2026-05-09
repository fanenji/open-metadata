---
type: entity
title: pgstac
created: 2026-04-29
updated: 2026-04-29
tags: [stac, postgresql, postgis, database, extension]
related: [stac-fastapi, stac-server-implementation, pystac]
sources: ["ETL RASTER.md"]
---
# pgstac

`pgstac` is a PostgreSQL extension that provides the database backend for `stac-fastapi`. It creates the necessary tables and functions for efficiently indexing and querying STAC Items, enabling high-performance spatiotemporal searches on large geospatial catalogs.

## Requirements

- PostgreSQL database with PostGIS extension installed
- The `pgstac` extension installed in the target database

## Role in the Architecture

`pgstac` serves as the persistent storage layer for the STAC catalog, storing all STAC Items and Collections. It is populated by the ingestion process via the `stac-fastapi` API endpoints.
