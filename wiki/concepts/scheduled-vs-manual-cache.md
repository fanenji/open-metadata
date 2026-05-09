---
type: concept
title: Scheduled vs Manual Cache
created: 2026-04-29
updated: 2026-04-29
tags: [gis, etl, oracle, postgis, caching]
related: [airflow-geospatial-etl-pattern, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# Scheduled vs Manual Cache

Scheduled vs Manual Cache defines two execution modes for the Oracle-to-PostGIS spatial data caching pipeline. This distinction drives the DAG parameterization strategy and determines which Oracle tables are queried for layer configuration.

## Scheduled Mode

- **Trigger**: Automated via Airflow scheduler
- **Instance Types**: Production (P) or Test (T)
- **Configuration Source**: Reads from `GS_LAYERS` table where `CACHE_SCHEDULATA` matches the instance pattern
- **Filter**: Only layers with `POSTGIS_CACHE = 'S'` are processed
- **Use Case**: Regular, automated cache refreshes for all configured layers

## Manual Mode

- **Trigger**: Manual trigger via Airflow UI or API
- **Identifier Types**: Map ID (numeric) or Layer ID (prefixed with 'L')
- **Configuration Source**: Reads from `PG_CACHE_LAYERS` table filtered by the provided IDs
- **Optional Flag**: `--update-flag` sets `POSTGIS_CACHE = 'S'` in `sit_catalogo` after successful import (map IDs only)
- **Use Case**: On-demand cache refresh for specific maps or layers

## DAG Parameterization

In the Airflow DAG, these modes are implemented via DAG `params`:

```python
params = {
    "schedule_type": Param("P", enum=["P", "T", None], description="Scheduled instance type"),
    "identifier": Param("", description="Map ID(s) or Layer ID(s) for manual run"),
    "update_flag": Param(False, description="Set POSTGIS_CACHE flag after import")
}
```