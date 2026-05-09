---
type: concept
title: dbt Seeds
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, static-data, csv]
related: [dbt-core, dbt-project-scaffolding]
sources: ["How to get started with dbt.md"]
---
# dbt Seeds

Seeds in [[dbt Core]] are CSV files placed in the `seeds/` directory of a dbt project. They provide a way to quickly ingest static or reference data (e.g., country codes, lookup tables, configuration mappings) into the data warehouse. Seeds are loaded using the `dbt seed` command and are materialized as tables. They are intended for small, static datasets that change infrequently, not for large or dynamic data.