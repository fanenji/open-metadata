---
type: concept
title: dbt Workflow SQL Only
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, workflow, sql, dremio]
related: [dbt-workflow-sql-python-hybrid, dbt-orchestration-yaml-python, dbt-dremio-adapter, dbt]
sources: ["PROCESS.md"]
---
# dbt Workflow SQL Only

The pure SQL workflow (Workflow DBT 1) is a core process definition for the data platform. In this pattern, all data transformation — both ingestion and transformation — is performed using SQL models in dbt, with Dremio as the target query engine.

## Constraints

- All data sources must be configured on Dremio (relational databases, files on S3).
- All transformations are written as SQL queries in dbt models.
- No Python models are used.

## Use Case

This workflow is suitable when all required transformations can be expressed in SQL and the data sources are accessible through Dremio. It is the simpler and more performant of the two defined workflows.