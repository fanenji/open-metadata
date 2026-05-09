---
type: source
title: Script Esecuzione DBT
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, ci-cd, orchestration, documentation]
related: [dbt-workflow, dbt-checkpoint, dbt-ci-documentation-gate, mixed-sql-python-dbt-project, dbt-osmosis, dbt-pre-commit-patterns, ci-cd-for-data-pipelines]
sources: ["SCRIPT ESECUZIONE DBT.md"]
---
# Script Esecuzione DBT

Internal design note proposing a custom Python orchestration tool (`dbt-workflow`) for dbt execution, and documenting the workflow constraints and CI/CD documentation gate pattern.

## Key Points

- **Proposed `dbt-workflow` tool**: A Python package using the `questionary` library for a terminal user interface (TUI), supporting reduced (non-full) workflows for faster development iteration.
- **dbt execution flow**: `dbt build` → `dbt-osmosis yaml refactor` → `dbt docs generate` → (optional) `dbt docs serve` → `pre-commit` (non-blocking checks).
- **dbt-osmosis constraint**: Requires prior `dbt build` execution, so documentation quality cannot be enforced during development.
- **CI/CD documentation gate**: `dbt-checkpoint` is used in CI/CD pipelines as a blocking pre-commit hook. If it fails, the merge request is blocked, preventing deployment to staging/production environments.
- **Mixed SQL/Python project hypothesis**: A proposed architecture where a YAML configuration file defines model dependencies and processing flow, and a Python script reads the YAML and executes the pipeline.

## Workflow Diagram

The note references a diagram (Pasted image 20260309115452.png) illustrating the commit/push Git workflow.

## Connections

- [[dbt-osmosis]] — confirms the tool's requirement for prior `dbt build` execution
- [[dbt-pre-commit-patterns]] — introduces dbt-checkpoint as a specific CI/CD enforcement tool
- [[CI-CD-for-data-pipelines]] — the documentation gate pattern aligns with this concept
- [[dbt-project-scaffolding]] — the proposed `dbt-workflow` tool could complement project scaffolding