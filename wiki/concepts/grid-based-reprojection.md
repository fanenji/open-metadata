---
type: concept
title: Grid-Based Reprojection
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, coordinate-transformation, proj, gsb, datum-shift]
related: [italian-datum-transformations, gdal-docker-image, oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline]
sources: ["ETL CARTO 2.md"]
---
# Grid-Based Reprojection

A technique for precise coordinate transformations between datums using GSB (Grid Shift Binary) files. Unlike simple mathematical transformations (e.g., Helmert transforms), grid-based reprojection uses a raster of displacement vectors to correct for local variations in the Earth's shape.

## Application in Regione Liguria

The primary use case is transforming geospatial data from the Italian Gauss-Boaga (GB) datum to the modern ETRK2K (EPSG:7791) reference system. This is required because the legacy Oracle database stores data in the older GB datum, while the target PostgreSQL/PostGIS system uses ETRK2K.

## PROJ Configuration

Grid files are specified in the PROJ string using the `nadgrids` parameter with a `@` prefix to make the grid mandatory:

```
+nadgrids=@43340719_44471019_R40_F00.gsb,null
```

The `@` prefix ensures the transformation fails explicitly if the grid file is missing, preventing silent datum errors.

## Infrastructure Requirements

- Grid files must be accessible to GDAL/PROJ at runtime
- In the [[gdal-docker-image]], grid files are mounted at `/usr/share/proj`
- The `gdalwarp` tool is used for raster reprojection with grid support