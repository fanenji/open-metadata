---
type: concept
title: Jinja Templating in dbt
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, jinja, templating, sql]
related: [dbt-core, dbt-macros]
sources: ["How to get started with dbt.md"]
---
# Jinja Templating in dbt

Jinja is a templating engine originally from Python that [[dbt Core]] uses to render SQL templates into executable SQL queries. In dbt, SQL files are treated as templates containing Jinja syntax — recognized by double curly brackets (`{{ }}`) and curly percent signs (`{% %}`). When dbt compiles a project, it processes these templates, replacing Jinja expressions with their evaluated results, producing final SQL that is executed against the data warehouse.

Jinja enables:
- Dynamic SQL generation with variables and control flow
- Reusable code through [[dbt-macros|macros]]
- Conditional logic (e.g., incremental model logic)
- Reference resolution via `ref` and `source` macros

Jinja is the core mechanism that makes dbt a framework rather than a simple SQL runner.