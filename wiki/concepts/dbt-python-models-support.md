---
type: concept
title: dbt Python Models Support
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, python, data-engineering]
related: [dbt-best-practices, orchestration-decompling-patterns, duckdb]
sources: ["Connettori dbt e Python.md"]
---
# dbt Python Models Support

A reference for the availability of Python model execution (`.py` files in the `models/` directory) across different dbt adapters.

## Native Support (The "Big Three")
These adapters execute Python code directly within the warehouse's compute infrastructure:
- **dbt-snowflake**: Uses **Snowpark**.
- **dbt-databricks**: Uses **Spark** clusters.
- **dbt-bigquery**: Uses **Dataproc** or **BigQuery Studio**.

## In-Process/Local Support
- **dbt-duckdb**: Executes Python code locally or in-process, making it highly efficient for lightweight or local development pipelines.

## Non-Native/Workaround Approaches
For databases lacking a native Python runtime (e.g., Postgres, Redshift):
- **External Orchestration (Recommended):** Using tools like **Airflow**, **Dagster**, or **Prefect** to manage Python-based tasks that complement dbt SQL models.
- **Community Forks:** Projects like `dbt-postgres-python` exist as temporary solutions but lack official support.
- **Avoid `dbt-fal`:** This method is deprecated and poses security and dependency risks.