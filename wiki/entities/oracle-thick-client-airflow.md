---
type: entity
title: Oracle Thick Client Airflow
created: 2026-04-29
updated: 2026-04-29
tags: [oracle, airflow, kubernetes, docker, gis]
related: [airflow-geospatial-etl-pattern, ogr2ogr-airflow-integration, kubernetes-etl-deployment-strategies]
sources: ["Geoscript in DAG Airflow_Kuberbetes .md"]
---
# Oracle Thick Client Airflow

Oracle Thick Client Airflow refers to the configuration and deployment of Oracle Instant Client libraries for Airflow workers, enabling the `oracledb` Python library in thick mode for direct Oracle database access from Airflow tasks.

## Key Requirements

- **Oracle Instant Client**: Must be installed on all Airflow worker nodes (or in the Docker image for Kubernetes deployments).
- **Environment Variable**: `ORACLE_CLIENT_LIB_DIR` must point to the Instant Client library directory (e.g., `/opt/oracle/instantclient`).
- **Initialization**: `oracledb.init_oracle_client(lib_dir=...)` must be called before any Oracle connections.

## Kubernetes Deployment

For Airflow on Kubernetes, the Oracle Instant Client libraries must be included in the worker container image. This can be achieved by:

1. Building a custom Docker image with Oracle Instant Client installed
2. Setting the `ORACLE_CLIENT_LIB_DIR` environment variable in the Airflow worker deployment
3. Ensuring the thick client initialization runs at task startup

## Best Practices

- Use Airflow Connections for Oracle credentials instead of `.env` files
- Test the thick client initialization in the container build process
- Consider using Oracle's thin mode (default in oracledb) if thick mode dependencies are problematic