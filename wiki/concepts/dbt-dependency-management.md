---
type: concept
title: dbt Dependency Management
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, dag, sql]
related: [dbt, ref-macro]
sources: ["10 Game-Changing dbt Tips I Wish I Knew Before My First Production Model.md"]
---
# dbt Dependency Management

In dbt, dependency management is handled through the use of the `{{ ref() }}` macro. This approach ensures that dbt can build a Directed Acyclic Graph (DAG) of all models.

## The Importance of `ref()`

Using `{{ ref('model_name') }}` instead of hardcoded table names (e.g., `FROM raw_data.sales`) is critical for:
- **DAG Generation**: Allows dbt to understand the order in which models must be run.
- **Environment Agility**: Automatically resolves to the correct database/schema depending on the target environment (dev vs. prod).
- **Lineage Tracking**: Enables the generation of visual lineage in `dbt docs`.

Avoid hardcoding dependencies to prevent broken pipelines and broken lineage.
