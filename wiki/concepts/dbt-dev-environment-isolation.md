---
type: concept
title: dbt Dev Environment Isolation
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, development, terraform, bigquery, isolation]
related: [blablacar, terraform, bigquery, read-from-prod-write-to-dev-pattern, upstream-prod, dev-containers-for-dbt]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# dbt Dev Environment Isolation

dbt Dev Environment Isolation is a pattern for providing each data practitioner with their own isolated development environment in the data warehouse, preventing interference between developers and ensuring safe experimentation.

## BlaBlaCar's Implementation

At [[BlaBlaCar]], dev environment isolation is achieved using [[Terraform]]:

1. A list of users is defined in Terraform.
2. A Terraform module generates a separate BigQuery dataset for each user (using a loop) with appropriate settings and permissions.
3. Each user defines a local environment variable containing their dataset ID.
4. The environment variable is used in the dev dbt profile so that all dbt commands target this dataset by default.

## Combined with Read from Prod / Write to Dev

This isolation pattern is combined with the [[read-from-prod-write-to-dev-pattern]] using the [[upstream-prod]] dbt package. Developers write to their isolated datasets while reading from production tables for upstream dependencies, enabling fast development without running full upstream pipelines.

## Benefits

- **No Interference:** Developers cannot accidentally modify each other's work.
- **Cost Control:** Using `upstream_prod` avoids the cost of running all upstream models in each dev environment.
- **Security:** Permissions are scoped per user and typically limited to the developer's domain.