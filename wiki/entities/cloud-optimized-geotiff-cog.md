---
type: entity
title: Cloud Optimized GeoTIFF (COG)
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, raster, format, cloud]
related: [gdal-ogr-container-pipeline, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline]
sources: ["Ingestione Dati Geospaziali_ Analisi e Opzioni_ .md"]
---
# Cloud Optimized GeoTIFF (COG)

Cloud Optimized GeoTIFF (COG) is a raster format optimized for cloud access via HTTP range requests. It is the standard output format for raster data in the geospatial ingestion pipeline, produced by `gdal_translate`.

## Key Characteristics

- **HTTP Range Requests:** Enables efficient access to specific portions of a raster file without downloading the entire file.
- **Internal Tiling:** Data is organized in tiles, allowing partial reads for zoom-level or region-specific queries.
- **Multi-Resolution Overviews:** Built-in overviews (pyramids) enable fast rendering at different zoom levels.
- **GDAL Integration:** `gdal_translate` with appropriate options (e.g., `-co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW`) produces COG-compliant output.

## Role in the Architecture

In the current pipeline, raster data from sources (Oracle, PostGIS, filesystem) is converted to COG format and written to MinIO object storage. COG files are then accessible via Dremio or other query engines for analysis and visualization.

## Integration with Iceberg

COG files can be stored as Iceberg table data files, but Iceberg does not natively understand COG's internal structure. The two-phase ingestion problem applies: GDAL writes COG files, then a separate process must register them in Iceberg.

## Alternatives

- **GeoParquet for raster:** Emerging but not yet mature for raster data.
- **Zarr:** Cloud-optimized array format, suitable for multi-dimensional raster data.
- **Iceberg with native raster types:** Not yet supported in Iceberg specification.