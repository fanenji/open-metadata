---
type: entity
title: dbt (data build tool)
created: 2026-04-22
updated: 2026-04-22
tags: [transformation, sql, data-engineering]
related: [slim-ci, data-observability, data-governance]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md"]
---
# dbt (data build tool)

**dbt** is a central transformation tool in the Modern Data Stack used to transform data within a warehouse using SQL. It allows data engineers to apply software engineering best practices—such as version control, testing, and documentation—to the data transformation layer.

Key features relevant to CI/CD include:
- **State-aware selection**: Ability to run models based on changes relative to a previous state.
- **Deferral**: Ability to reference existing production relations during development or CI.
- **Model Contracts**: Enforcing schema constraints to ensure downstream stability.
- **Testing**: Built-in support for generic schema tests (e.g., `unique`, `not_null`).