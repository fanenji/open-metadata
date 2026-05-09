---
type: concept
title: Ref Macro
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, sql, macro]
related: [dbt-dependency-management, dbt]
sources: ["10 Game-Changing dbt Tips I Wish I Knew Before My First Production Model.md"]
---
# Ref Macro

The `{{ ref() }}` macro is the fundamental building block of dbt development. It is used to reference other models within the dbt project.

## Functionality
Instead of using static SQL references like `FROM my_database.my_schema.my_table`, developers use `FROM {{ ref('my_table') }}`.

## Benefits
- **DAG Construction**: It allows dbt to calculate the execution order of models.
- **Environment Switching**: It dynamically resolves the table name to the correct schema based on the active dbt target (e.g., switching from `dev` to `prod`).
- **Lineage**: It is the mechanism that enables the creation of the lineage graph in `dbt docs`.
