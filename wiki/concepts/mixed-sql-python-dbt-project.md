---
type: concept
title: Mixed SQL/Python dbt Project
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, architecture, orchestration, python]
related: [dbt-workflow, dbt-project-scaffolding, dbt-osmosis]
sources: ["SCRIPT ESECUZIONE DBT.md"]
---
# Mixed SQL/Python dbt Project

A proposed architectural pattern for dbt projects where a YAML configuration file defines model dependencies and processing flow, and a Python script reads the YAML and executes the pipeline. This introduces an orchestration layer beyond dbt's native capabilities.

## Hypothesis

- A YAML configuration file defines dependencies between models and the processing flow.
- A Python script reads the YAML and executes the pipeline.
- This enables complex orchestration logic that may be difficult to express using dbt's native `ref()` and `source()` functions alone.

## Status

This is a speculative design hypothesis documented in an internal project note. No implementation exists.

## Potential Concerns

- **Conflict with dbt's native DAG**: The proposed YAML-based dependency resolution may conflict with dbt's native `ref()` and `source()` functions, creating a parallel orchestration layer.
- **Complexity**: Introduces additional complexity without clear benefits over dbt's built-in dependency resolution.
- **Maintenance**: Requires maintaining both dbt's native DAG and the YAML configuration, increasing the risk of inconsistencies.

## Related

- [[dbt-workflow]] — the proposed orchestration tool that would implement this pattern
- [[dbt-project-scaffolding]] — project structure patterns that this would extend
- [[dbt-osmosis]] — schema and documentation automation that could complement this pattern