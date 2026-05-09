---
type: entity
title: upstream_prod
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, package, development, bigquery]
related: [read-from-prod-write-to-dev-pattern, dbt-dev-environment-isolation, blablacar, bigquery]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# upstream_prod

`upstream_prod` is a dbt package available on the dbt Hub that enables the "read from prod/write to dev" pattern. It overrides dbt's `ref()` and `source()` functions to point to production tables when the corresponding objects don't exist in the development dataset.

## Usage

The package is used in development environments to avoid running all upstream models. Developers can run intermediate and downstream models directly, with the package automatically resolving upstream dependencies from production.

## At BlaBlaCar

At [[BlaBlaCar]], `upstream_prod` is a key component of the [[dbt-dev-environment-isolation]] strategy. Combined with Terraform-provisioned per-user BigQuery datasets, it enables 45+ data practitioners to develop independently without incurring the cost of running full upstream pipelines (critical for BigQuery on-demand pricing).