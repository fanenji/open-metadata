---
type: concept
title: dbt Macros
created: 2026-04-29
updated: 2026-05-07
tags: [dbt, jinja, code-reuse, sql, reusability]
related: [dbt-core, jinja-templating, dbt-project-scaffolding, dbt-dispatch-pattern, dynamic-sql-generation, incremental-models, dbt-testing-patterns, dbt-jinja-variables]
sources: ["How to get started with dbt.md", "Leveraging DBT Macros for Enhanced Data Engineering Practices.md"]
---
# dbt Macros

Macros in [[dbt Core]] are reusable Jinja functions that either perform an action or return SQL (or partial SQL) code. They enable code reuse across a dbt project, reducing duplication and enforcing consistent patterns across models, tests, and other dbt resources. Macros are defined in `.sql` files within the `macros/` directory of a dbt project and can also be imported from other dbt packages (e.g., [[dbt-expectations]], dbt_utils). They can accept parameters, contain control flow logic, and call other macros.

The `ref` and `source` macros are the most commonly used built-in macros, defining relationships between models and sources to build the dbt DAG.

This page serves as a foundational reference for the macro concept. More advanced patterns — such as adapter-specific overrides via [[dbt-dispatch-pattern]], custom tests via [[dbt-testing-patterns]], and automated schema generation with [[dbt-osmosis]] — are covered in their respective pages.

## Key Benefits

- **Code Reusability**: Write logic once and reuse across multiple models and projects.
- **Dynamic SQL Generation**: Create SQL that adapts to different inputs, schemas, or conditions.
- **Maintainability**: Centralize complex logic in macros, reducing duplication and simplifying updates.

## Common Use Cases

- Date formatting and manipulation
- Dynamic filtering and date dimension generation
- Housekeeping metadata (e.g., adding timestamps to incremental models)
- Adapter-specific SQL overrides via [[dbt-dispatch-pattern]]
- Custom test definitions in [[dbt-testing-patterns]]

## Best Practices

- Keep macros simple and focused on a single task.
- Document macros clearly with descriptions and parameter definitions.
- Test macros across various scenarios to ensure reliability.
- Use descriptive naming conventions for easy discovery.