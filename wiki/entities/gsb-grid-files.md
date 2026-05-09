---
type: entity
title: GSB Grid Files
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, coordinate-transformation, proj, gsb]
related: [gdal-ogr-container-pipeline, spark-sedona-geospatial-etl, legacy-geospatial-etl-pipeline]
sources: ["Ingestione Dati Geospaziali_ Analisi e Opzioni_ .md"]
---
# GSB Grid Files

GSB (Grid Shift Binary) files are binary grid files used by the PROJ library for high-accuracy coordinate transformations between datums. They are essential for precise transformations in regions with local datum shifts (e.g., Italian national grids).

## Technical Details

- **Format:** Binary grid files containing shift values (latitude, longitude, height) at regular grid intervals.
- **Usage:** PROJ uses GSB files for datum transformations that cannot be accurately modeled by simple mathematical formulas (e.g., Molodensky, Helmert).
- **Common Files:** `IT_00.gsb` (Italian national grid), `nzgd2000.gsb` (New Zealand), `ntv2_0.gsb` (Canada).
- **Configuration:** GSB files must be accessible to PROJ via the `PROJ_LIB` environment variable or the `proj-data` package.

## Critical Requirement

The ingestion pipeline requires GSB file support for coordinate transformations. This is a hard constraint for any alternative approach:

- **GDAL:** Native support via PROJ. GSB files are included in the GDAL Docker image or mounted as volumes.
- **Apache Sedona:** Support for GSB files is **unverified**. This is the critical blocker for adopting Spark+Sedona as the primary alternative.
- **GeoPandas/Dask:** Support depends on the underlying PROJ installation; generally works if PROJ is configured correctly.

## Verification Needed

Before adopting any alternative, GSB support must be verified through:
1. A test transformation using a known GSB file.
2. Comparison of results with GDAL's output for the same transformation.
3. Documentation of the configuration steps required.