---
type: entity
title: Italian Datum Transformations
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, coordinate-transformation, proj, gsb, italy]
related: [gdal-docker-image, geoscript-migration-plan, oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline]
sources: ["ETL CARTO 2.md"]
---
# Italian Datum Transformations

The specific coordinate transformation parameters and PROJ grid files used for converting geospatial data between Italian datums in the Regione Liguria ETL pipeline.

## Primary Transformation

**From:** Italian datum GB (Gauss-Boaga)  
**To:** ETRK2K (EPSG:7791)

The transformation uses a PROJ string with a GSB grid file for precise datum shift:

```
-s_srs "+proj=tmerc +lat_0=0 +lon_0=9.000000000 +k=0.999600 +x_0=1500000 +y_0=0 +ellps=intl +nadgrids=@43340719_44471019_R40_F00.gsb,null +units=m +no_defs" -t_srs EPSG:7791
```

## Key Parameters

- **Projection:** Transverse Mercator (`tmerc`)
- **Central Meridian:** 9° E (`lon_0=9.000000000`)
- **Scale Factor:** 0.999600 (`k=0.999600`)
- **False Easting:** 1,500,000 m (`x_0=1500000`)
- **Ellipsoid:** International 1924 (`ellps=intl`)
- **Grid File:** `43340719_44471019_R40_F00.gsb` (with `null` fallback)
- **Units:** meters

## Infrastructure

GSB grid files must be mounted at `/usr/share/proj` in the [[gdal-docker-image]] container. The `@` prefix in the `nadgrids` parameter indicates the grid file is mandatory — if missing, the transformation will fail rather than silently produce incorrect results.