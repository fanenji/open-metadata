---
type: concept
title: dbt Query Tagging
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, cost-attribution, governance, warehouse]
related: [dbt-cost-control, dbt-job-design-by-layer, data-domain-governance, abhishek-2025-running-dbt-real-world]
sources: ["Running dbt in the Real World Cost Control, Governance, and Team Practices at Scale.md"]
---
# dbt Query Tagging

A pattern for setting warehouse query tags from dbt configuration to attribute query cost to specific projects, jobs, environments, and domains. Supported by warehouses like Snowflake and BigQuery.

## Pattern

Set a query tag from dbt that includes project, job, environment, and/or domain:

```yaml
# dbt_project.yml
vars:
  query_tag: "project=my_dbt_project,env=prod,job=nightly_core"

models:
  +query_tag: "{{ var('query_tag') }}"
```

## Benefits

Warehouse usage views can then answer questions like:
- "How much does the nightly core job cost?"
- "Which team's dbt models are most expensive?"

This supports cost-back to domains and pushes teams toward cost-aware development.

## Limitations

This pattern assumes the warehouse supports query tagging (e.g., Snowflake, BigQuery). It may not apply to all warehouses (e.g., DuckDB, Dremio). The cost of maintaining tag infrastructure and dashboards should be considered.

## Relationship to Existing Wiki

Query tagging is a foundational practice for [[dbt-cost-control]] and enables the cost attribution dimension of [[data-domain-governance]].