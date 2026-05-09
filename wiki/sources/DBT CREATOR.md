---
type: source
title: DBT CREATOR
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, scaffolding, tooling, data-platform]
related: [dbt-project-scaffolding, cookiecutter-dbt-template, dbt, dbt-utils]
sources: ["DBT CREATOR.md"]
---
# DBT CREATOR

Internal project note documenting the development of an interactive CLI tool (`dbt-project-creator`) and a Cookiecutter template (`cookiecutter-dbt-template`) for standardizing the creation of new dbt projects within the Regione Liguria data platform.

## Key Points

- **Purpose:** Provide a repeatable, standardized way to initialize new dbt projects, enforcing conventions and reducing manual setup errors.
- **Components:**
  - `dbt-project-creator` — Interactive CLI tool that scaffolds a new dbt project.
  - `cookiecutter-dbt-template` — Cookiecutter template defining the canonical project structure.
- **Status:** In development. A TODO list identifies pending modifications.

## TODO Items

### Script (dbt-project-creator)
- Modify default values.
- Change slug separator from `-` to `_`.

### Template (cookiecutter-dbt-template)
- Place model directories directly under `models/`.
- Modify `profiles.yaml`.
- Remove `space_` prefix.
- Add `.ipynb_checkpoints` to `.gitignore`/`.dbtignore`.
- Modify `source.yml`.
- Modify `create_pdf` to reference source.
- Add `packages.yml` with `dbt_utils` dependency.

## Installation & Execution

Installation is done via pip from the internal GitLab instance, with SSL verification disabled. Execution requires activating the virtual environment and running the `dbt-creator` command.

## Repository URLs (Internal)
- Script: `https://gitlab-test.dataliguria.it/data-platform/dbt/models/dbt-project-creator`
- Template: `https://gitlab-test.dataliguria.it/data-platform/dbt/models/cookiecutter-dbt-template`