---
type: concept
title: dbt Orchestration via YAML + Python
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, orchestration, yaml, python, workflow]
related: [dbt-workflow-sql-only, dbt-workflow-sql-python-hybrid, dbt]
sources: ["PROCESS.md"]
---
# dbt Orchestration via YAML + Python

This concept describes a proposed lightweight orchestration pattern for dbt workflows. Instead of using a full orchestration tool like Airflow or Kestra, the pattern uses:

1. A **YAML configuration file** that defines model dependencies and the execution flow.
2. A **Python script** that reads the YAML file and executes the pipeline.

## Status

This is a proposed pattern, not yet implemented. The specific structure of the YAML config file is not defined in the source document.

## Open Questions

- Is this intended to replace or complement existing orchestration tools (Kestra, Airflow)?
- What is the specific structure of the YAML config file?
- How will error handling, retries, and monitoring be implemented?