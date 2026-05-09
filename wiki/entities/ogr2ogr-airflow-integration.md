---
type: entity
title: OGR2OGR Airflow Integration
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, ogr2ogr, airflow, gis, etl]
related: [airflow-geospatial-etl-pattern, oracle-to-postgresql-gdal-etl, oracle-thick-client-airflow]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# OGR2OGR Airflow Integration

OGR2OGR Airflow Integration refers to the patterns and best practices for running GDAL/OGR commands from Airflow tasks, specifically for spatial data transfer between Oracle Spatial and PostGIS.

## Execution Methods

### Subprocess (Recommended)
Use `subprocess.run()` with a list of arguments (not shell strings) to avoid shell injection risks:

```python
comando_args = [
    "ogr2ogr",
    "-overwrite",
    "-f", "PostgreSQL",
    f"PG:{pg_conn_str}",
    f"OCI:{oci_conn_str}",
    "-sql", f"SELECT * FROM {tab_geom}",
    "-a_srs", f"EPSG:{epsg_code}",
    "--config", "PG_USE_COPY", "YES",
    "-lco", "FID=ogr_fid",
    "-lco", f"DIM={dim}",
    "-nln", f"{pg_schema}.{pg_tab_geom}"
]
proc = subprocess.run(comando_args, capture_output=True, text=True, timeout=timeout_seconds, check=False)
```

### Custom Operator
For production, consider creating a custom Airflow operator that wraps ogr2ogr with proper logging, retry, and error handling.

## Key Parameters

- **OCI Connection String**: `{stringa_conn}:{tab_geom}` for Oracle Spatial access
- **PG Connection String**: `host={PG_HOST} port={PG_PORT} dbname={PG_DB_NAME} user={PG_USER} password={PG_PWD} active_schema={pg_schema}`
- **Timeout**: Typically 70 minutes (4200 seconds) for large spatial layers
- **Error Handling**: Check for Oracle errors in stderr (e.g., ORA-13208)

## Best Practices

- Use `shell=False` in subprocess to prevent shell injection
- Log the command string with credentials masked for debugging
- Implement timeout handling for long-running spatial transfers
- Capture and log both stdout and stderr for troubleshooting