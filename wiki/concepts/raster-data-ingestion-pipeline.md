---
type: concept
title: Raster Data Ingestion Pipeline
created: 2026-04-29
updated: 2026-04-29
tags: [etl, raster, gdal, cog, minio, ingestion]
related: [cloud-optimized-geotiff-cog, minio, stac-server-implementation, raster-cataloging-strategy, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg]
sources: ["ETL RASTER.md"]
---
# Raster Data Ingestion Pipeline

The raster data ingestion pipeline is the evolved version of the legacy geospatial ETL pipeline, specifically for raster data. It replaces the Oracle/GDAL/PostgreSQL flow with a Python/GDAL/MinIO/COG architecture.

## Pipeline Flow

1. **Source Reading:** Python scripts using GDAL (`gdalwarp`, `gdal_translate`) read source raster files
2. **Reprojection:** Rasters are reprojected to EPSG:7791 (the target coordinate reference system)
3. **COG Conversion:** Rasters are converted to Cloud Optimized GeoTIFF (COG) format
4. **Storage:** COG files are written directly to MinIO (S3-compatible object storage)
5. **Cataloging:** Metadata is generated and pushed to both the Data Catalog (DataHub/OpenMetadata) and optionally a STAC server

## Key Differences from Vector Pipeline

- **No Iceberg/Nessie:** Unlike vector data, raster COGs are not managed by Iceberg or Nessie
- **Direct S3 Access:** COGs are accessed directly via their S3 path, not through a query engine
- **Separate Cataloging:** Raster data requires specialized cataloging (STAC) in addition to the general Data Catalog

## Critical Considerations

- **Computational Resources:** Raster transformation is CPU, I/O, and RAM intensive; the Geoscript server must be adequately sized
- **Error Handling:** Robust error handling for GDAL commands is essential
- **Orchestration:** The pipeline needs scheduling and monitoring (cron or Data Platform orchestrator)
- **Cataloging:** Making COGs discoverable is the highest priority
- **Updates:** A strategy for updating/overwriting existing COG files must be defined
