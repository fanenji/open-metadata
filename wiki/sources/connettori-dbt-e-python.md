---
type: source
title: "Connettori dbt e Python"
created: 2026-02-13
updated: 2026-02-13
tags: [dbt, python, data-engineering]
related: [dbt-python-models-support, dbt-best-practices, orchestration-decompling-patterns]
sources: ["Connettori dbt e Python.md"]
authors: []
year: 2026
url: "https://aistudio.google.com/u/1/prompts/1aBD_VwyvYcrgX7qQgfVebl9Ve-W776U7"
venue: "AI Studio Conversation"
---
# Connettori dbt e Python

A discussion regarding the support for Python models within various dbt adapters. It covers the "Big Three" cloud warehouses with native support, the capabilities of DuckDB, and the deprecation of the `dbt-fal` adapter.

## Key Takeaways

- **Native Support:** Python models (`.py` files) are natively supported in modern cloud warehouses like **Snowflake** (via Snowpark), **Databricks** (via Spark), and **BigQuery** (via Dataproc or BigQuery Studio).
- **DuckDB:** The `dbt-duckdb` adapter allows for in-process Python execution, making it ideal for local development and lightweight pipelines.
- **Deprecation of `dbt-fal`:** The `dbt-fal` project (by fal.ai) is officially **deprecated** as of April 2024. It should not be used for new production pipelines due to lack of maintenance and security risks.
- **Architectural Shift:** For databases without native Python runtimes (e.g., Postgres, Redshift), the recommended approach is moving away from "wrapper" adapters toward **External Orchestration** (using Airflow, Dagster, or Prefect) or using **DuckDB** for local processing.