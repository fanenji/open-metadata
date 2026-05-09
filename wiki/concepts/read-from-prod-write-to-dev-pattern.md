---
type: concept
title: Read from Prod / Write to Dev Pattern
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, development, bigquery, cost-optimization]
related: [upstream-prod, dbt-dev-environment-isolation, blablacar, bigquery, dbt-project-scaffolding]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# Read from Prod / Write to Dev Pattern

The "Read from Prod / Write to Dev" pattern is a dbt development strategy that enables data practitioners to run intermediate and downstream models in an isolated development environment without first running all upstream models. This is achieved using the [[upstream-prod]] dbt package.

## How It Works

- The `upstream_prod` package overrides dbt's `ref()` and `source()` functions to point to production tables when the corresponding objects don't exist in the development dataset.
- Developers write to their isolated dev datasets while reading from production tables for upstream dependencies.
- This avoids the cost and time of running full upstream pipelines in development.

## Benefits

- **Cost Savings:** Particularly important for BigQuery on-demand pricing, where running all upstream models would incur significant costs.
- **Development Speed:** Developers can iterate quickly on downstream models without waiting for upstream pipelines to complete.
- **Isolation:** Developers work in their own datasets without interfering with each other or production.

## Implementation at BlaBlaCar

At [[BlaBlaCar]], this pattern is combined with [[dbt-dev-environment-isolation]] (Terraform-provisioned per-user BigQuery datasets). Each developer has a local environment variable containing their dataset ID, which is used in the dev dbt profile. The `upstream_prod` package then handles the "read from prod" aspect automatically.

## Limitations

- Requires appropriate permissions for reading production tables, typically limited to the developer's domain.
- Not suitable for development that requires modifying upstream models.
- May mask issues where upstream model changes would break downstream models.