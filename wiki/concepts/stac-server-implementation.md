---
type: concept
title: STAC Server Implementation
created: 2026-04-29
updated: 2026-04-29
tags: [stac, api, geospatial, catalog, raster]
related: [stac-fastapi, pgstac, pystac, cloud-optimized-geotiff-cog, raster-cataloging-strategy, raster-data-ingestion-pipeline, datahub, openmetadata]
sources: ["ETL RASTER.md"]
---
# STAC Server Implementation

A STAC (SpatioTemporal Asset Catalog) server is a standards-compliant API for describing, discovering, and accessing geospatial assets. It provides specialized spatiotemporal search capabilities optimized for raster and imagery data.

## Why STAC?

- **Standardization:** Enables generic clients (STAC browsers, QGIS plugins, Python libraries like `pystac-client`) to search and discover raster data uniformly
- **Interoperability:** Facilitates data sharing and integration with other platforms that understand STAC
- **Spatiotemporal Search:** Designed specifically for queries based on area of interest (AOI) and time range
- **Rich Metadata:** Defines standard fields for common metadata (EO, SAR, etc.) and is extensible

## Recommended Implementation Stack

The recommended implementation uses `stac-fastapi` with the `pgstac` backend:

1. **Backend:** PostgreSQL/PostGIS with `pgstac` extension for high-performance indexing
2. **API Framework:** `stac-fastapi` (FastAPI + Pydantic) for the REST API
3. **Metadata Generation:** `pystac` library for generating STAC JSON from COG files
4. **Deployment:** Containerized application on Kubernetes behind a reverse proxy

## Population Workflow

1. The raster ingestion process creates COG files on MinIO
2. Using `pystac`, the process generates STAC Item JSON for each COG (or Collection for datasets)
3. The STAC Item is submitted to the STAC API via HTTP POST to `/collections/{collection_id}/items`
4. `stac-fastapi` validates the JSON and indexes it in the `pgstac` backend

## Relationship to Data Catalog

The STAC server is complementary to the general Data Catalog (DataHub/OpenMetadata), not a replacement. The Data Catalog provides an enterprise-wide view of all data assets, while the STAC server provides specialized geospatial search. The recommended approach is to register raster datasets in both systems, with the Data Catalog entry including a link to the STAC endpoint.
