---
type: concept
title: dbt Project Folder Structure
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, project-structure, naming-conventions, best-practices]
related: [bottom-up-data-modeling, dbt-project-scaffolding, dbt-schema-synchronization]
sources: ["Modern Data Modeling Start with the End?.md"]
---
# dbt Project Folder Structure

A recommended folder structure for dbt projects that organizes models into three sequential layers: `base`, `core`, and `usecases`. The naming is designed to appear in logical alphabetical order in file explorers, IDEs, and warehouse UIs.

## Recommended Structure

```
models/
├── base/
│   ├── _sources.yml
│   ├── mailchimp/
│   │   ├── _mailchimp_models.yml
│   │   └── base_mailchimp__members.sql
│   └── ...
├── core/
│   ├── staging/
│   │   └── ...
│   └── core_orders.sql
└── usecases/
    ├── marketing/
    ├── product/
    ├── sales/
    └── finance/
```

## Naming Conventions

- **Base models**: `base/<source_name>/base_<source_name>__<model_name>.sql`
- **Core models**: Descriptive names at the object grain (e.g., `core_users.sql`)
- **Usecase models**: Organized by stakeholder department

## Schema Mapping

Configure schema names in `dbt_project.yml` to mirror the folder structure:

```yaml
models:
  your_project_name:
    base:
      +schema: "base"
    core:
      +schema: "core"
    usecases:
      +schema: "usecases"
```

## Environment Awareness

Use a custom `generate_schema_name` macro to map dev runs to a single schema and prod/preprod runs to the configured schemas. This pattern is documented in [[dbt-schema-synchronization]].