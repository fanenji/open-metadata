---
type: concept
title: PipeRider Impact Analysis for dbt
created: 2026-04-29
updated: 2026-04-29
tags: [piperider, impact-analysis, dbt, data-quality, ci-cd]
related: [dbt-ci-cd-github-actions, piperider, dbt-slim-ci, implementing-cicd-for-dbt-first-steps]
sources: ["Implementing CICD for dbt First Steps.md"]
---
# PipeRider Impact Analysis for dbt

The practice of using [[PipeRider]] to automatically analyze the downstream impact of proposed [[dbt]] model changes. PipeRider leverages dbt's lineage to produce a lineage diff that summarizes how a model change affects metrics, columns, dependencies, and other downstream models.

## Purpose

- Discover downstream changes that might otherwise go unnoticed.
- See how a change affects important business metrics.
- Prevent manual checking of all downstream models in the staging environment.
- Provide automated PR comments with impact summaries.

## Integration

PipeRider is integrated into [[GitHub Actions]] workflows using the `InfuseAI/piperider-compare-action`:

```yaml
jobs:
  piperider-compare:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
      - uses: actions/checkout@v3
      - name: PipeRider Compare
        uses: InfuseAI/piperider-compare-action@v1
        with:
          cloud_api_token: ${{ secrets.PIPERIDER_CLOUD_TOKEN_ID }}
          cloud_project: ${{ secrets.PIPERIDER_API_PROJECT }}
          upload: true
          share: true
```

## Relationship to dbt Slim CI

PipeRider's impact analysis complements [[dbt-slim-ci]] by providing a visual and automated way to understand the consequences of changes, while Slim CI focuses on running only the affected models and tests.