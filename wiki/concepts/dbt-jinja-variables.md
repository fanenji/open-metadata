---
type: concept
title: dbt Jinja Variables
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, jinja, macros, metadata]
related: [dbt-observability-implementation, on-run-end-hook, dbt-artifacts]
sources: ["dbt observability 101 How to monitor dbt run and test results.md"]
---
# dbt Jinja Variables

Jinja variables exposed by dbt that provide access to project metadata and command execution results within macros. Three variables are particularly relevant to dbt observability:

- **`results`:** Available only during an `on-run-end` hook. Contains metadata about command execution results (status, execution time, rows affected, node details).
- **`graph`:** Provides metadata about project resources (models, tests, sources, etc.) and their relationships.
- **`invocation_id`:** A unique identifier for each dbt command execution, used to create unique `result_id` values.

## Role in dbt Observability

The [[dbt-observability-implementation]] pattern relies on these variables to avoid processing [[dbt-artifacts]] JSON files. The `results` variable provides execution metadata, `graph` provides project structure metadata, and `invocation_id` enables unique identification of each result record.

## Limitations

- `results` is only available during `on-run-end` hooks, limiting when data can be collected.
- The Jinja variables expose less comprehensive metadata than the full artifact JSON files (e.g., model descriptions, test configurations are not included).
- The structure of these variables may change between dbt versions, though less frequently than artifact schemas.

## Related

- [[dbt-observability-implementation]] — The primary use case documented in this wiki.
- [[on-run-end-hook]] — The context where `results` is available.
- [[dbt-artifacts]] — The alternative approach that provides richer metadata.