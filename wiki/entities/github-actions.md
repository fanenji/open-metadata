---
type: entity
title: GitHub Actions
created: 2026-04-22
updated: 2026-05-07
tags: ["ci-cd", "automation", "tool"]
related: ["slim-ci", "dbt-ci-cd-github-actions", "ci-cd-for-data-pipelines", "implementing-cicd-for-dbt-first-steps"]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md", "Implementing CICD for dbt First Steps.md"]
---
# GitHub Actions

**GitHub Actions** is GitHub's built-in CI/CD platform that allows defining automation workflows using YAML syntax. Workflow files are stored in `.github/workflows/` in a repository. It integrates tightly with GitHub for source control and enables triggers on pull requests, pushes, or scheduled cron jobs.

In the context of dbt, GitHub Actions is the most commonly used CI/CD platform—approximately 90% of data engineers use it according to [[Jens Wilms]]—and is often employed to orchestrate "Slim CI" pipelines. These pipelines execute dbt commands, manage cloud storage interactions (such as fetching artifacts from S3), and report build summaries back to Pull Requests.

## Common dbt Workflow Jobs

- **Lint**: Run [[SQLFluff]] to enforce SQL code style and best practices.
- **Test**: Execute `dbt test` to validate data against defined expectations.
- **Build**: Run `dbt build` to materialize models in a staging environment.
- **Impact Analysis**: Use tools like [[PipeRider]] to assess downstream effects of changes.