---
type: concept
title: on-run-end Hook
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, configuration, hooks, macros]
related: [dbt-observability-implementation, dbt-artifacts, dbt-jinja-variables]
sources: ["dbt observability 101 How to monitor dbt run and test results.md"]
---
# on-run-end Hook

A dbt configuration mechanism that executes a specified macro after every dbt command (run, test, seed, snapshot, etc.). It is defined in `dbt_project.yml` and is the only context where the `results` Jinja variable is available.

## Usage in dbt Observability

The `on-run-end` hook is central to the [[dbt-observability-implementation]] pattern because the `results` Jinja variable — which contains metadata about command execution (status, execution time, rows affected, node details) — is only accessible within this hook. The pattern uses the hook to:

1. Receive the `results` variable as input
2. Flatten the nested result objects using a parsing macro
3. Insert the flattened data into a warehouse table

## Configuration

```yaml
# dbt_project.yml
on-run-end:
  - "{{ my_observability_macro(results) }}"
```

## Limitations

- The hook runs after the entire command completes, so results cannot be streamed incrementally during execution.
- Only the `results` variable is available; other Jinja variables like `graph` are accessible elsewhere but not in this context.
- Performance impact depends on the complexity of the macro and the number of nodes executed.

## Related

- [[dbt-observability-implementation]] — The primary use case documented in this wiki.
- [[dbt-artifacts]] — An alternative approach that processes JSON files outside of hooks.
- [[dbt-jinja-variables]] — The broader set of Jinja variables available in dbt.