---
type: concept
title: dbt Dispatch Pattern
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, jinja, macros, dispatch, adapter-override]
related: [dbt-nessie-branch-workaround, dbt-testing-patterns]
sources: ["DBT - NOTE.md"]
---
# dbt Dispatch Pattern

The dbt dispatch pattern is a Jinja function dispatch mechanism that allows projects to override adapter macros with custom implementations. It is configured in `dbt_project.yml` and enables projects to extend or modify adapter behavior without forking the adapter package.

## Configuration

```yaml
dispatch:
  - macro_namespace: dbt_dremio
    search_order: ['my_project', 'dbt_dremio']
```

The `search_order` list defines the priority: dbt searches for macro implementations in the listed namespaces in order, falling back to the adapter's default implementation if no custom macro is found.

## Use Case: Nessie Branch Support

The dispatch pattern is used to override the `create_table_as` and `relation` macros in the dbt-dremio adapter to inject Nessie branch syntax. This is a generalizable technique for any adapter limitation that can be addressed at the SQL generation level.

## Benefits

- No need to fork or modify the adapter package
- Changes are scoped to the dbt project
- Falls back to adapter defaults for unmodified macros
- Compatible with dbt's standard upgrade path