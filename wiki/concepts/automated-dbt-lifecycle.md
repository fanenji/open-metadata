---
type: concept
title: Automated dbt Lifecycle
created: 2026-03-27
updated: 2026-03-27
tags: [automation, data-engineering, governance]
related: [dbt-workflow, dbt-creator, dbt-osmosis, software-defined-assets]
sources: ["Ambiente sviluppo su Container.md"]
---
# Automated dbt Lifecycle

The **Automated dbt Lifecycle** is a standardized, end-to-end workflow that automates the transition of a dbt project from initial creation to production-ready deployment. This lifecycle is a core feature of the platform's data governance strategy.

## Stages of the Lifecycle
1. **Bootstrapping**: Using [[dbt-creator]] to generate a new project from a standardized template.
2. **Development**: Active coding and modeling within the containerized IDE.
3. **Validation & Refactoring**: Using [[dbt-osmosis]] for YAML synthesis and `pre-commit` for sanity checks.
4. **Execution**: Running transformations via `dbt build`.
5. **Documentation & Metadata**: Generating dbt documentation and automatically injecting metadata into [[openmetadata]].
6. **Deployment**: Finalizing the cycle by pushing the updated, validated code back to GitLab.

## Benefits
- **Enforced Governance**: Metadata injection and quality checks are not optional; they are baked into the standard development loop.
- **Reduced Manual Error**: Automation of repetitive tasks like YAML refactoring and metadata synchronization.

- **Scalability**: Enables a consistent process that can be scaled across multiple teams and projects.