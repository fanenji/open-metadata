---
type: concept
title: dbt Environment Management
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, devops, infrastructure]
related: [dbt-best-practices, infrastructure-architecture]
sources: ["Best Practices for Workflows A Guide to Effective dbt Use-20260506.md"]
---
# dbt Environment Management

A strategy for separating development and production workloads within dbt to ensure data integrity and developer productivity.

## Key Components
- **Target Profiles:** Using `profiles.yml` to define distinct `dev` and `pro` targets.
- **Conditional Logic:** Utilizing `target.name` in Jinja to apply environment-specific logic, such as:
    - **Data Sampling:** Limiting row counts in `dev` to speed up testing (`LIMIT 1000`).
    - **Permission Management:** Using `post-hooks` to apply `GRANT` statements specifically in production.

## Benefits
- Prevents accidental modification of production datasets.
- Optimizes development speed by reducing the volume of data processed during local runs.