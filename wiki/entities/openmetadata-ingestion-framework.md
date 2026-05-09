---
type: entity
title: OpenMetadata Ingestion Framework
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, ingestion, connectors, metadata]
related: [openmetadata, openmetadata-architecture, openmetadata-python-sdk, custom-connector-openmetadata, dbt, airflow, snowflake]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Ingestion Framework

The Ingestion Framework is a Python-based system for pulling metadata from 90+ connectors into the OpenMetadata server. It runs as standalone scripts, Airflow DAGs, or scheduled jobs.

## How Ingestion Works

1. Define a **Service** (e.g., a Snowflake connection).
2. Configure an **Ingestion Pipeline** (what to extract: schema, profiling, lineage, usage).
3. OpenMetadata connects and pulls metadata on a schedule.

## Connector Categories

- **Databases** — Snowflake, BigQuery, Redshift, Postgres, MySQL, etc.
- **Data Lakes** — S3, GCS, ADLS, Delta Lake, Iceberg
- **Data Warehouses** — Snowflake, BigQuery, Redshift
- **BI Tools** — Tableau, Looker, Power BI, Metabase
- **Pipelines** — Airflow, dbt, Fivetran, Stitch
- **ML Platforms** — MLflow, SageMaker
- **Messaging** — Kafka, Kinesis

## Example: Snowflake Ingestion via YAML

```yaml
source:
  type: snowflake
  serviceName: prod-snowflake
  serviceConnection:
    config:
      type: Snowflake
      username: "${SNOWFLAKE_USER}"
      password: "${SNOWFLAKE_PASSWORD}"
      account: "${SNOWFLAKE_ACCOUNT}"
      warehouse: COMPUTE_WH
      database: ANALYTICS
      role: ANALYST
  sourceConfig:
    config:
      type: DatabaseMetadata
      markDeletedTables: true
      includeTables: true
      includeViews: true
      schemaFilterPattern:
        includes:
          - "PUBLIC"
          - "ANALYTICS.*"
sink:
  type: metadata-rest
  config: {}
workflowConfig:
  openMetadataServerConfig:
    hostPort: http://localhost:8585/api
    authProvider: openmetadata
    securityConfig:
      jwtToken: "${OM_JWT_TOKEN}"
```

Run with: `metadata ingest -c snowflake-ingestion.yaml`