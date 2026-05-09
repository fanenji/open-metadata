---
type: concept
title: Shift-Left Data Quality
created: 2026-04-29
updated: 2026-04-29
tags: [data-quality, devops, testing, validation]
related: [data-quality-dimensions, engineering-led-data-quality, data-quality-score, early-binding-vs-late-binding, dbt-preflight-validation, environmental-data-quality-hierarchy]
sources: ["Defining Data Quality The Foundation of Modern Data Architecture.md"]
---
# Shift-Left Data Quality

A strategy for Data Quality (DQ) enforcement borrowed from DevOps, where validation is moved as close to the data source as possible. The principle is that errors caught earlier are cheaper and faster to fix.

## Application Points

- **At the Source**: Validate before ingestion. This is the cheapest point to catch and fix errors.
- **During Ingestion**: Apply checks within pipelines to catch bad data early in the flow.
- **Post-Ingestion**: Reconciliation and monitoring for consistency and freshness as a final safety net.

## Layered Validation

Best practice is to build redundant validation layers at every system handoff:

- **Source Systems**: First line of defense — cheapest to fix errors.
- **Data Lake/Warehouse**: Final defense — monitor quality at scale.

## Relationship to Existing Wiki Concepts

The shift-left approach aligns with [[early-binding-vs-late-binding]] (prescribed context at source vs discovered context downstream) and [[dbt-preflight-validation]] (pre-run checks in dbt). It also complements the [[environmental-data-quality-hierarchy]]'s tiered validation pattern (VAL → VAL_COR → CERT), where earlier tiers catch issues before they propagate.

## Testing, Monitoring, and Cleaning

- **Unit Testing**: Ensures known data assumptions hold during development.
- **Data Cleaning/Transformation**: Fixes known quality issues.
- **Data Quality Monitoring**: Detects unexpected issues as data evolves — the "dynamic safety net."