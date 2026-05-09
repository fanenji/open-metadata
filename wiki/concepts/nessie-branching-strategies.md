---
type: concept
title: Nessie Branching Strategies
created: 2026-04-22
updated: 2026-04-22
tags: [nessie, branching, versioning, data-lakehouse, git-workflow]
related: [nessie-catalog-versioning, nessie-commit-best-practices, nessie-operational-practices, data-lakehouse-versioning-strategies]
sources: ["nessie-branching-best-practices.md"]
---
# Nessie Branching Strategies

Nessie supports Git-like branching workflows adapted for data lakehouse management. The choice of strategy depends on team size, release cadence, and complexity of data transformations.

## Feature Branches

Create a dedicated branch for each new data pipeline, experiment, or schema change. All modifications (ingestion, transformation, quality checks) occur within this branch. The branch is merged to `main` only after validation passes.

**When to use**: Most common pattern; suitable for teams practicing continuous integration.

## Main/Develop Branches (GitFlow-like)

A structure with a `main` branch containing production-ready data and a `develop` branch for ongoing, integrated development. Feature branches are merged into `develop` first, then `develop` is merged into `main` for releases.

**When to use**: Larger teams or projects requiring a staging/integration step before production.

## Short-Lived Branches

For agile data operations, branches should ideally be short-lived — created for a specific task, validated, and merged quickly. This minimizes divergence and merge complexity.

**When to use**: Teams with fast iteration cycles and automated validation pipelines.

## Recommendation

Simple workflows (GitHub Flow with just `main` and feature branches) are often sufficient for data workflows. The GitFlow pattern adds complexity that may not be justified unless there is a clear need for a separate integration branch.