---
type: entity
title: Airflow Geospatial ETL Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [airflow, gis, etl, oracle, postgis, gdal]
related: [oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline, ogr2ogr-airflow-integration, oracle-thick-client-airflow, kubernetes-etl-deployment-strategies]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# Airflow Geospatial ETL Pattern

The Airflow Geospatial ETL Pattern is a DAG design for orchestrating Oracle-to-PostGIS spatial data transfers using GDAL/OGR. It transforms a monolithic Python script into a parameterized, scheduled, and monitored Airflow workflow.

## Key Characteristics

- **Parameterized Execution**: Uses Airflow DAG `params` for flexible execution modes (scheduled instance P/T or manual map/layer ID).
- **Callback-Based Notifications**: Replaces inline SMTP with Airflow `on_success_callback` and `on_failure_callback`.
- **Single-Task Core**: Keeps the core ogr2ogr logic in one `PythonOperator` for simplicity, though multi-task splitting is recommended for production.
- **Configuration via Airflow**: Recommends migration from `.env` files to Airflow Connections/Variables for production environments.

## Pipeline Steps

1. Connect to Oracle and PostgreSQL databases
2. Read layer configuration from Oracle tables (PG_CACHE_LAYERS, GS_LAYERS)
3. Execute ogr2ogr for each spatial layer with OCI driver
4. Validate geometries using ST_MakeValid
5. Create indexes and run VACUUM ANALYZE
6. Recreate materialized views (post-update)
7. Log execution metrics to Oracle (LOG_CACHE_PG)
8. Send email notifications

## Production Considerations

- **Multi-Task Splitting**: Split into separate tasks for connect, import each table, post-update, and notify for better observability and retry granularity.
- **Connection Management**: Use Airflow Hooks instead of global variables for database connections.
- **Retry Strategy**: Implement retry logic for transient Oracle errors (e.g., ORA-13208).
- **Parallelism**: Consider per-table parallel tasks vs. sequential batch processing.