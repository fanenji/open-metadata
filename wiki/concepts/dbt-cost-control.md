---
type: concept
title: dbt Cost Control
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, cost-management, warehouse-optimization]
related: [dbt-query-tagging, dbt-slim-ci, dbt-job-design-by-layer, dbt-minimum-model-standards, dbt-observability-implementation, abhishek-2025-running-dbt-real-world]
sources: ["Running dbt in the Real World Cost Control, Governance, and Team Practices at Scale.md"]
---
# dbt Cost Control

A framework for managing warehouse spend driven by dbt jobs. Since most dbt compute cost lives in the warehouse (not dbt itself), cost control focuses on aligning dbt's job design with the warehouse's cost model.

## Practical Levers

1. **Incremental Models**: Prefer incremental models and sliding windows for large fact tables to avoid full-refresh costs.
2. **Slim CI**: Use `state:modified` selectors in CI to avoid rebuilding everything on every PR (see [[dbt-slim-ci]]).
3. **Job Grouping by Layer**: Separate staging (high frequency, smaller warehouse), core/marts (daily, larger warehouse), and heavy aggregates/backfills (off-hours) into distinct jobs (see [[dbt-job-design-by-layer]]).
4. **Off-Peak Scheduling**: Schedule heavy jobs during low-cost warehouse periods.
5. **Query Tagging**: Attribute cost to projects, jobs, environments, and domains via warehouse query tags (see [[dbt-query-tagging]]).

## Cost Dashboards

Build dashboards using warehouse usage views and query tags to show:
- Cost by dbt job, environment, and domain/team.
- Trends over weeks/months.
- Outliers where cost spikes for specific jobs or models.

This supports conversations like "Why did marketing's daily job cost 3x last week?" and identifies models to optimize or convert to incrementals.

## Relationship to Existing Wiki

This concept extends [[dbt-slim-ci]] by adding cost-control motivation and provides the cost dimension to [[dbt-observability-implementation]].