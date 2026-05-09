---
type: concept
title: dbt Workflow SQL + Python Hybrid
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, workflow, sql, python, duckdb, dremio]
related: [dbt-workflow-sql-only, dbt-orchestration-yaml-python, duckdb, dbt-dremio-adapter, dbt]
sources: ["PROCESS.md"]
---
# dbt Workflow SQL + Python Hybrid

The hybrid SQL+Python workflow (Workflow DBT 2) extends the pure SQL pattern by allowing Python models alongside SQL models. In this pattern:

- **SQL models** target Dremio for transformations that are well-suited to SQL.
- **Python models** target DuckDB for transformations that require Python libraries or logic.

## Use Case

This workflow is used when Python transformations are needed alongside SQL. It provides flexibility for complex data processing tasks that cannot be easily expressed in SQL, while still leveraging dbt's transformation framework.

## Open Questions

- How will cross-target dependencies (Dremio → DuckDB or vice versa) be handled?
- What is the specific structure of the YAML config file for orchestration?