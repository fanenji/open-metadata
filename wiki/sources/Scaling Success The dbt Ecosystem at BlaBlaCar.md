---
type: source
title: "Scaling Success: The dbt Ecosystem at BlaBlaCar"
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, blablacar, data-mesh, airflow, dev-containers, ci-cd]
related: [blablacar, antoine-lefebvre, dbt-dag-generator, dbt-osmosis, dev-containers-for-dbt, read-from-prod-write-to-dev-pattern, dbt-dev-environment-isolation, dbt-power-user, sqlfluff, terraform, upstream-prod, dbt-dry-run, bigquery, airflow, data-mesh, dbt-project-scaffolding, ci-cd-for-data-pipelines]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# Scaling Success: The dbt Ecosystem at BlaBlaCar

**Author:** Antoine Lefebvre  
**Published:** 2025-09-17  
**Source:** Medium (BlaBlaCar publication)

## Summary

This article describes the internal dbt ecosystem developed at BlaBlaCar to manage over 4,000 tables and 300 reports across 45+ data practitioners organized in a data mesh architecture. The ecosystem includes a custom dbtDagGenerator framework for Airflow orchestration, Dev Containers for standardized environments, Terraform-provisioned isolated dev datasets, CI/CD checks, and dbt-osmosis for documentation generation. The article details the trade-offs between building custom tooling (dbtDagGenerator) versus adopting existing solutions (Cosmos), and presents the "read from prod/write to dev" pattern using the upstream_prod package.

## Key Insights

- BlaBlaCar chose dbt Core + Airflow over dbt Cloud, building a custom dbtDagGenerator framework that maps dbt models/tests to Airflow tasks and sources to sensors.
- Dev Containers with pre-configured Docker images (Python 3.11, dbt-core 1.9, dbt-power-user, SQLFluff, dbt-osmosis) ensure consistent environments across 45+ practitioners.
- Per-user BigQuery datasets provisioned via Terraform, combined with the upstream_prod package, enable isolated development without running full upstream pipelines.
- CI/CD pipeline includes dbt-dry-run, linting, tag checks, and DAG load validation to prevent broken code from reaching production.
- dbt projects are organized in a mono-repo with domain-aligned projects following a Staging → Intermediate → Model → Reporting layer structure.

## Relevance

This source provides a concrete, real-world implementation of a dbt ecosystem at scale within a data mesh architecture. It validates several patterns already documented in the wiki (dbt-osmosis usage, dbt project organization, CI/CD for data pipelines) and introduces new patterns (dbtDagGenerator, read-from-prod/write-to-dev, Dev Containers for dbt) that extend the wiki's coverage of dbt best practices.