---
type: entity
title: pystac
created: 2026-04-29
updated: 2026-04-29
tags: [stac, python, library, metadata]
related: [stac-server-implementation, stac-fastapi, cloud-optimized-geotiff-cog, raster-data-ingestion-pipeline]
sources: ["ETL RASTER.md"]
---
# pystac

`pystac` is the standard Python library for generating, parsing, and validating STAC (SpatioTemporal Asset Catalog) metadata. It provides a programmatic way to create STAC Items and Collections with proper JSON structure.

## Usage in the Data Platform

The `pystac` library is used by the raster ingestion process (Geoscript/Python+GDAL) to generate STAC metadata for each COG file. The workflow involves:

1. Opening the COG file with `rasterio` to extract spatial metadata (bounding box, CRS, etc.)
2. Creating a `pystac.Item` with the extracted geometry, bbox, datetime, and properties
3. Adding the COG file as a `pystac.Asset` with the S3 path as the `href`
4. Adding STAC extensions (e.g., EO, Projection) as needed
5. Validating the item with `item.validate()`
6. Converting to a dictionary with `item.to_dict()` for API submission
