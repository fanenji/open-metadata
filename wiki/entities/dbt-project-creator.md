---
type: entity
title: dbt-project-creator
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, scaffolding, tooling, cli]
related: [cookiecutter-dbt-template, dbt-project-scaffolding, dbt]
sources: ["DBT CREATOR.md"]
---
# dbt-project-creator

An interactive CLI tool for scaffolding new dbt projects. Developed internally for the Regione Liguria data platform, it uses a [[cookiecutter-dbt-template]] to generate a standardized project structure.

## Purpose

- Enforce consistent project conventions across teams.
- Reduce manual setup errors and time.
- Provide a repeatable initialization workflow.

## Installation

Installed via pip from the internal GitLab instance:

```
GIT_SSL_NO_VERIFY=true pip install git+https://10.11.9.20/data-platform/dbt/models/dbt-project-creator.git
```

## Execution

Activate the virtual environment and run:

```
source dbt-project-creator/.venv/bin/activate
dbt-creator
```

## Known Limitations (TODO)

- Default values need modification.
- Slug separator should change from `-` to `_`.
- Instructions for project initialization need to be added.

## Repository

Hosted at `https://gitlab-test.dataliguria.it/data-platform/dbt/models/dbt-project-creator` (internal).