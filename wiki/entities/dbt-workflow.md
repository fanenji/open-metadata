---
type: entity
title: dbt-workflow
created: 2026-03-27
updated: 2026-05-07
tags: [automation, dbt, pipeline, orchestration, python, tui]
related: [dbt-creator, dbt-osmosis, kestra, dbt-checkpoint, dbt-ci-documentation-gate, mixed-sql-python-dbt-project, dbt-project-scaffolding]
sources: ["Ambiente sviluppo su Container.md", "SCRIPT ESECUZIONE DBT.md"]
---
# dbt-workflow

**dbt-workflow** is a custom automation pipeline designed to manage the end-to-end lifecycle of a dbt project within a containerized development environment. It was originally proposed as a Python orchestration tool with a terminal user interface (TUI) using `questionary`, and has since been implemented as a comprehensive pipeline that enforces governance standards and automates critical stages of the data engineering workflow.

## Design

The tool was designed with developer productivity in mind, offering:

- **Interactive TUI** built with the `questionary` library for streamlined execution.
- **Reduced workflows** – supports a subset of the full dbt pipeline, skipping non‑essential steps during development for faster iteration.
- **Proposed workflow** – the initial design specified the following steps: `dbt build`, `dbt-osmosis yaml refactor`, `dbt docs generate` (optional `dbt docs serve`), and `pre-commit` (as non‑blocking checks).
- **Full automation** – when run in complete mode, the pipeline encompasses all steps described below.

## Pipeline Steps

The `dbt-workflow` pipeline automates the following stages:

1. **Environment Setup** – loads necessary environment variables (e.g., Dremio credentials, OpenMetadata tokens).
2. **Dependency Management** – executes `dbt deps` to ensure all packages are present.
3. **Execution** – runs `dbt build` to execute models and tests.
4. **Refactoring** – integrates `dbt-osmosis` for YAML synthesis and refactoring (`dbt-osmosis yaml refactor`).
5. **Documentation** – automates `dbt docs generate` (and optionally `dbt docs serve` for local preview).
6. **Quality Assurance** – runs `pre-commit` hooks and `dbt-checkpoint` sanity checks. In reduced mode these can be non‑blocking.
7. **Metadata Governance** – injects processed metadata into [[openmetadata]].
8. **Version Control** – automates the `git commit` and `push` process to GitLab.

Each step can be selectively enabled or disabled, allowing developers to run the full pipeline or a shortened version appropriate for their task.

## Role in Governance

By embedding these steps into a single automated command, `dbt-workflow` ensures that all developers adhere to the platform’s governance standards. Metadata injection and quality checks become a mandatory part of the development loop, promoting consistency and compliance across the team.

## Status

The tool originated as a design proposal documented in an internal project note (without implementation details or repository references at the time). It has since been implemented and is used as the standard workflow for dbt projects within the containerized environment. The interactive TUI and reduced‑workflow capabilities remain available for development scenarios.

## Related

- [[dbt-creator]] – project scaffolding and initialization.
- [[dbt-osmosis]] – schema and documentation automation.
- [[kestra]] – orchestration platform (complementary to `dbt-workflow`).
- [[dbt-checkpoint]] – CI/CD enforcement tool for documentation quality.
- [[dbt-ci-documentation-gate]] – pattern for enforcing documentation at CI/CD boundary.
- [[mixed-sql-python-dbt-project]] – proposed architecture pattern with YAML config + Python orchestration.
- [[dbt-project-scaffolding]] – template scaffolding for dbt projects.