---
type: concept
title: dbt Project Scaffolding
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, scaffolding, automation, project-initialization]
related: [dbt-project-creator, cookiecutter-dbt-template, dbt, dbt-cloud, dbt-mesh, dbt-testing-patterns, dbt-data-contract-implementation]
sources: ["DBT CREATOR.md"]
---
# dbt Project Scaffolding

The practice of using automated tools to generate standardized dbt project structures. Within the Regione Liguria data platform, this is implemented through a combination of an interactive CLI tool ([[dbt-project-creator]]) and a [[cookiecutter-dbt-template]].

## Benefits

- **Consistency:** Enforces a canonical project layout across all teams and projects.
- **Efficiency:** Reduces time spent on manual project setup.
- **Error reduction:** Minimizes configuration mistakes by automating boilerplate.
- **Onboarding:** Lowers the barrier for new team members to start contributing.

## Implementation

The scaffolding workflow consists of:

1. Installing the [[dbt-project-creator]] CLI tool via pip.
2. Running `dbt-creator` to interactively configure a new project.
3. The tool generates a project from the [[cookiecutter-dbt-template]], applying user-provided settings.
4. Running `dbt deps` to install dependencies (e.g., [[dbt-utils]]).

## Relationship to Other Concepts

- [[dbt-cloud]] and [[dbt-mesh]] — Scaffolding ensures projects are structured in a way compatible with dbt Cloud and dbt Mesh deployment.
- [[dbt-testing-patterns]] — A standardized project structure makes it easier to enforce testing conventions.
- [[dbt-data-contract-implementation]] — Scaffolding can include default contract configurations, promoting data contract adoption from project inception.