---
type: concept
title: dbt CI Pipeline Anatomy
created: 2026-05-07
updated: 2026-05-07
tags: [ci, dbt, data-engineering, continuous-integration]
related: [dbt-slim-ci, ci-cd-for-data-pipelines, shift-left-data-quality, dbt-cloud-environments, dbt-cloud]
sources: ["What is CI, and why should you care about it.md"]
---
# dbt CI Pipeline Anatomy

The dbt CI pipeline is a sequence of automated steps that validate code changes before they are deployed to production. The standard pipeline consists of five steps:

1. **dbt compile** — Checks for valid Jinja and SQL syntax, catches missing dependencies and packages.
2. **dbt build in staging** — Executes `dbt run` in a separate staging environment to build data produced by the new code.
3. **dbt test** — Runs foundational tests (uniqueness, null checks, range validation) to catch data quality issues before production deployment.
4. **SQL linter** — Enforces code style and formatting standards (e.g., [[SQLFluff]]) to maintain codebase readability.
5. **Data diff** (bonus) — Compares dev and prod versions of tables to show the impact of code changes on data, including row counts, primary key changes, and downstream model effects.

The pipeline is typically triggered on pull requests and runs against a staging environment that mirrors production. This approach implements [[shift-left-data-quality]] by catching issues before they reach production consumers.

For implementation, [[dbt-cloud]] users configure a CI job with PR triggers and [[dbt-slim-ci]] selectors (`dbt build --select state:modified+`). [[dbt-core]] users set up equivalent workflows via GitHub Actions or similar CI platforms.
