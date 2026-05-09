---
type: entity
title: PipeRider
created: 2026-04-29
updated: 2026-04-29
tags: [tool, impact-analysis, dbt, data-quality]
related: [piperider-dbt-impact-analysis, dbt-ci-cd-github-actions, dbt-slim-ci, implementing-cicd-for-dbt-first-steps]
sources: ["Implementing CICD for dbt First Steps.md"]
---
# PipeRider

An open-source tool that automatically analyzes the downstream data impact of proposed [[dbt]] model changes. It leverages dbt's lineage feature to produce a lineage diff, summarizing how a model change affects metrics, columns, dependencies, and other downstream models. PipeRider can be integrated into [[GitHub Actions]] workflows to provide automated impact analysis on pull requests, helping reviewers understand the consequences of changes without manually checking all downstream models.

## Key Features

- Lineage diff visualization showing affected models and columns.
- Metric impact analysis to see how changes affect key business metrics.
- Integration with GitHub Actions for automated PR comments.
- Cloud-based reporting and sharing capabilities.