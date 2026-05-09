---
type: entity
title: cookiecutter-dbt-template
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, scaffolding, template, cookiecutter]
related: [dbt-project-creator, dbt-project-scaffolding, dbt, dbt-utils]
sources: ["DBT CREATOR.md"]
---
# cookiecutter-dbt-template

A [[cookiecutter]] template that defines the canonical directory structure and configuration files for new dbt projects within the Regione Liguria data platform. Used by the [[dbt-project-creator]] CLI tool.

## Template Structure Modifications (TODO)

- Place model directories directly under `models/`.
- Modify `profiles.yaml`.
- Remove `space_` prefix from names.
- Add `.ipynb_checkpoints` to `.gitignore`/`.dbtignore`.
- Modify `source.yml`.
- Modify `create_pdf` to reference source.
- Add `packages.yml` with `dbt_utils` dependency.

## Repository

Hosted at `https://gitlab-test.dataliguria.it/data-platform/dbt/models/cookiecutter-dbt-template` (internal).