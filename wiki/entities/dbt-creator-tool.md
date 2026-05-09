---
type: entity
title: dbt-creator Tool
created: 2026-05-22
updated: 2026-05-22
tags: [automation, dbt, bootstrap]
related: [containerized-development-empty, kestra]
sources: ["CI-CD GIT FLOW v2.0.md"]
---
# dbt-creator Tool

The **dbt-creator** is a custom automation script (likely based on a cookie-cutter template) used to bootstrap new dbt projects within the Data Platform.

## Functionality
The tool automates the creation of a standardized project structure, ensuring all new projects adhere to the established CI/CD and folder conventions. Its primary responsibilities include:

- **dbt Project Initialization**: Configures the dbt project with a "dev" profile and initializes the Git "dev" branch.
- **Kestra Pipeline Configuration**: Creates the initial Kestra flow YAML file within the `/flows/` directory of the project.
- **Kestra Instance Synchronization**: Automatically sends the initial flow definition to the Kestra `dev` namespace to enable immediate orchestration.
- **CI/CD Pipeline Setup**: Generates the `.gitlab-ci.yml` file, pre-configured with the logic required for environment promotion (Dev $\rightarrow$ Test $\rightarrow$ Stage $\rightarrow$ Prod).

## Project Structure Created
The tool ensures the following directory structure:
- `models/`: dbt transformation logic.
- `flows/`: Kestra pipeline definitions (YAML).
- `.gitlab-ci.yml`: Automation logic for deployment and promotion.
- Python scripts: For managing dbt execution, documentation, and Git versioning.