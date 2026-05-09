---
type: source
title: ETL RASTER
created: 2026-01-15
updated: 2026-01-15
tags: [etl, raster, mapping, ingestion-dati-geo, gis]
related: [cloud-optimized-geotiff-cog, stac-server-implementation, raster-data-ingestion-pipeline, minio, raster-cataloging-strategy, stac-fastapi, pgstac, pystac, geospatial-etl-pipeline-iceberg, datahub, openmetadata, dremio-geospatial-limitations, legacy-geospatial-etl-pipeline]
sources: ["ETL RASTER.md"]
---
# ETL RASTER

This document analyzes the raster data ingestion pipeline for the Data Platform, focusing on the evolved Geoscript/Python+GDAL workflow for generating Cloud Optimized GeoTIFFs (COGs) and the critical need for a robust cataloging strategy.

## Key Findings

- **COG generation is valid and recommended.** The existing approach using Python/GDAL (`gdalwarp`, `gdal_translate`) to reproject to EPSG:7791 and write COGs to MinIO is the correct technical choice.
- **Cataloging is the critical gap.** Making COG files discoverable and usable through the Data Platform is the highest priority.
- **Two-tier cataloging is recommended:** A general Data Catalog (DataHub/OpenMetadata) for enterprise-wide discovery and governance, plus a specialized STAC server for geospatial-specific search and interoperability.
- **Dataset-level cataloging is preferred** over file-level for orthophoto mosaics, to avoid catalog bloat while maintaining discoverability.
- **Dremio is not suitable for COG access.** Direct S3 access via the Data Catalog path is the correct consumption pattern.
- **STAC server implementation is feasible** using `stac-fastapi` with `pgstac` backend, deployed on Kubernetes, populated by the ingestion process using `pystac`.

## Proposed Architecture

The document proposes a complementary cataloging architecture where:
1. The raster ingestion process creates COGs on MinIO
2. STAC metadata is generated using `pystac` and pushed to a STAC API server (`stac-fastapi` with `pgstac` backend)
3. General metadata (including the STAC endpoint) is pushed to the Data Catalog (DataHub/OpenMetadata)
4. Users discover raster data through either the Data Catalog (enterprise view) or the STAC API (specialized geospatial search)

## Open Questions

- Orchestration: Should raster ingestion be scheduled via the Data Platform orchestrator (Kestra/Airflow) or remain under Geoscript's cron?
- Error handling: What is the robust error handling strategy for GDAL commands?
- Update strategy: How should existing COG files be updated/overwritten?
- Catalog population mechanism: Should Geoscript push metadata to the catalog via API, or should the catalog scan S3 buckets?
- STAC server deployment: Should the STAC server be deployed on Kubernetes as part of the Data Platform infrastructure?
- Metadata redundancy: If raster metadata is stored in both the Data Catalog and STAC, how is consistency maintained?
