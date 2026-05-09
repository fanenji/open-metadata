---
type: concept
title: dbt Adapters
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, configuration, data-warehouse]
related: [dbt-core, dbt-profiles-yml]
sources: ["How to get started with dbt.md"]
---
# dbt Adapters

dbt adapters are plugins that enable [[dbt Core]] to connect to specific data warehouse platforms. Each adapter handles the translation of dbt's SQL compilation and execution logic to the dialect and capabilities of the target warehouse. Common adapters exist for Snowflake, BigQuery, Redshift, Postgres, Databricks, and many others.

To use a warehouse with dbt, the corresponding adapter must be installed as a Python package. The adapter is then referenced in the [[dbt-profiles-yml|profiles.yml]] configuration file to establish the connection.