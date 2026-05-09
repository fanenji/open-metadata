---
type: entity
title: dbt-creator
created: 2026-03-27
updated: 2026-03-27
tags: [automation, dbt, bootstrapping]
related: [dbt-workflow]
sources: ["Ambiente sviluppo su Namespace Container.md"]
---
# dbt-creator

`dbt-creator` is a custom Python package used to bootstrap new, compliant dbt projects within the development environment.

## Functionality
It provides an interactive wizard that gathers essential project information, including:
- Project name.
- GitLab group destination.
- GitLab access tokens.

## Output
The tool uses templates to create both a local project structure and a remote repository in GitLab, ensuring that every new project starts with the correct configuration, folder structure, and CI/CD readiness.