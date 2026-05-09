---
type: concept
title: Dev Containers for dbt
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, development-environment, dev-containers, vs-code]
related: [blablacar, dbt-power-user, sqlfluff, dbt-osmosis, dbt-dev-environment-isolation]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# Dev Containers for dbt

Dev Containers for dbt is a pattern for providing consistent, pre-configured development environments using VS Code Dev Containers and Docker images. This approach eliminates "works on my machine" problems and simplifies onboarding for data practitioners.

## BlaBlaCar's Implementation

At [[BlaBlaCar]], each developer is provided with a Dev Container containing:

- Python 3.11
- dbt-core & dbt-bigquery v1.9
- dbt Power User extension for VS Code
- SQLFluff for linting
- dbt-osmosis with an abstraction layer (VS Code shortcut) for generating `models.yml` files

## Setup Requirements

Developers install:
1. Rancher (or Docker)
2. VS Code
3. Dev Containers extension in VS Code
4. Google Cloud CLI (gcloud)

A `.devcontainer/devcontainers.json` file defines VS Code extensions and tools (Python, dbt, etc.). When a developer opens the repository in VS Code, a prompt appears to reopen it in the Dev Container.

## Benefits

- **Consistency:** All 45+ practitioners work in identical environments.
- **Simplified Onboarding:** New team members don't need to manually configure their local environment.
- **Local Resource Efficiency:** Docker containers free up local machine resources compared to running tools natively.
- **Version Control:** Dev Container configuration is versioned alongside the code in the mono-repo.