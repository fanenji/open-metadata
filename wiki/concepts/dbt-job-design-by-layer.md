---
type: concept
title: dbt Job Design by Layer
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, job-design, cost-control, environments]
related: [dbt-cost-control, dbt-query-tagging, dbt-cloud-environments, write-audit-publish-pattern, abhishek-2025-running-dbt-real-world]
sources: ["Running dbt in the Real World Cost Control, Governance, and Team Practices at Scale.md"]
---
# dbt Job Design by Layer

A pattern for separating dbt jobs by data layer and criticality to control cost, risk, and rollout. Teams at scale typically define three job categories:

## Job Categories

### Job 1 — Staging (High Frequency, Smaller Warehouse)
- Runs multiple times per day/hour.
- Pulls and cleans raw sources.
- Uses a smaller warehouse to keep costs low.

### Job 2 — Core / Marts (Lower Frequency, Larger Warehouse)
- Runs daily or intraday.
- Builds fact/dim tables and mart models.
- Uses a larger warehouse for complex transformations.

### Job 3 — Heavy Aggregates / Backfills / Maintenance (Off-Hours)
- Runs off-hours or weekly.
- Handles heavy backfills, re-clustering, or historical rebuilds.
- Scheduled during low-cost warehouse periods.

## Environment Separation

Each job targets separate environments:
- `dev` for feature development and manual testing.
- `staging` for integrated testing on prod-like data.
- `prod` for business-critical outputs.

## Promotion Strategy

Use the [[write-audit-publish-pattern]] (WAP):
- Write new versions to a shadow schema.
- Run tests/validation.
- Swap or re-point views to the new schema once checks pass.

## Relationship to Existing Wiki

This concept provides the job design framework that complements [[dbt-cloud-environments]] and operationalizes [[dbt-cost-control]] through scheduling and warehouse sizing decisions.