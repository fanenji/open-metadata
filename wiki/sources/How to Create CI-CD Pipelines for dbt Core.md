---
type: source
title: How to Create CI/CD Pipelines for dbt Core
created: 2026-04-04
updated: 2026-04-29
tags: [dbt, ci-cd, slim-ci, dbt-core]
related: [dbt-slim-ci, dbt-state-aware-selectors, dbt-artifacts, dbt-ci-testing-strategy, dbt-core-slim-ci-implementation, dbt-checkpoint, sqlfluff-dbt-integration, data-diff-dbt, paul-fry]
sources: ["How to Create CI-CD Pipelines for dbt Core.md"]
authors: [Paul Fry]
year: 2023
url: "https://paul-fry.medium.com/v0-4-pre-chatgpt-how-to-create-ci-cd-pipelines-for-dbt-core-88e68ab506dd"
venue: Medium
---
# How to Create CI/CD Pipelines for dbt Core

A practical guide by [[Paul Fry]] on replicating dbt Cloud's "Slim CI" job pattern in dbt Core using state processing. The article provides a step-by-step process for generating and comparing dbt manifest files to run only modified models in CI/CD pipelines, along with enhancement candidates including SQLFluff, dbt-checkpoint, and data-diff.

## Key Points

- The dbt Cloud Slim CI pattern can be fully replicated in dbt Core using `state:modified` and `defer` flags.
- Two versions of `manifest.json` are required: one from the main branch and one from the feature branch.
- The 4-step process: compile main branch manifest, push to Git, compile feature branch, apply state processing.
- Enhancement candidates in order of complexity: SQLFluff, Git standards enforcement, dbt-checkpoint (high-value), data-diff.

## Known Limitations

- The `--defer` flag is not available for `dbt ls` command, contradicting the code example in the article.
- Pushing manifest.json to the main branch requires rebasing feature branches, creating operational overhead.
- SQLFluff will flag legacy code issues if not already in use, potentially blocking CI/CD adoption.

## Connections

- Strengthens [[dbt-slim-ci]] with concrete dbt Core implementation steps.
- Extends [[dbt-ci-testing-strategy]] with enhancement candidates.
- Provides practical usage of [[dbt-state-aware-selectors]] and [[dbt-artifacts]].
- Contributes to [[CI-CD-for-data-pipelines]] with dbt-specific implementation.