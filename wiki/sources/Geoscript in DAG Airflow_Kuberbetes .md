---
type: source
title: "Geoscript in DAG Airflow_Kuberbetes "
created: 2026-02-13
updated: 2026-02-13
tags: [airflow, kubernetes, gis, gemini, mapping, oracle, postgis, gdal]
related: [oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline, kubernetes-etl-deployment-strategies, dbt-dag-generator, airflow-geospatial-etl-pattern, oracle-thick-client-airflow, ogr2ogr-airflow-integration]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# Geoscript in DAG Airflow_Kuberbetes

This source is a conversation (from Google Gemini) that transforms a monolithic Python script for Oracle-to-PostGIS geospatial data caching into an Airflow DAG. The original script uses GDAL/OGR (ogr2ogr) to transfer spatial data from Oracle Spatial to a PostGIS cache, with features including scheduled vs. manual execution, geometry validation, index creation, vacuum/analyze, and email notifications.

## Key Design Decisions

- **Parameterization**: Replaces `argparse` CLI arguments with Airflow DAG `params` for flexible execution (scheduled instance P/T or manual map/layer ID).
- **Notifications**: Uses Airflow callbacks (`on_success_callback`, `on_failure_callback`) for email notifications instead of inline SMTP.
- **Task Structure**: Keeps core logic in a single `PythonOperator` rather than splitting into multiple tasks.
- **Configuration**: Maintains `.env` file loading but recommends migration to Airflow Connections/Variables for production.

## Architecture

The DAG orchestrates a pipeline that:
1. Connects to both Oracle and PostgreSQL databases
2. Reads configuration from Oracle tables (PG_CACHE_LAYERS, GS_LAYERS, SIT_DB_ISTANZE)
3. Executes ogr2ogr for each spatial layer
4. Validates geometries (ST_MakeValid for invalid polygons)
5. Creates indexes and runs VACUUM ANALYZE
6. Recreates materialized views (post-update)
7. Logs execution metrics to Oracle (LOG_CACHE_PG)
8. Sends email notifications on success/failure

## Limitations & Tensions

- **Single vs. Multi-Task**: Keeping all logic in one `PythonOperator` reduces observability and retry granularity. Airflow best practice would split into multiple tasks.
- **Global State**: The script uses global variables for database connections, which Airflow discourages.
- **Logging Duality**: The script maintains its own file-based logging alongside Airflow's native logging.
- **Error Handling**: Original `sys.exit(1)` replaced with exceptions, but Airflow retry semantics not fully addressed.

## Connections to Existing Wiki

- Directly extends [[oracle-to-postgresql-gdal-etl]] by proposing Airflow orchestration
- The script being transformed IS the [[legacy-geospatial-etl-pipeline]]
- Related to [[kubernetes-etl-deployment-strategies]] for Airflow on Kubernetes deployment
- Related to [[dbt-dag-generator]] as an alternative DAG generation approach (for dbt, not GDAL)