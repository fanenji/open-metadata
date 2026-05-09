---
type: entity
title: Minerva
created: 2026-05-06
updated: 2026-05-06
tags: [airbnb, semantic-layer, metrics-platform]
related: [semantic-layer-architecture, metrics-as-code, data-quality-score, data-contract-platform]
sources: ["Semantic Layer in Big Tech.md"]
---
# Minerva

Airbnb's semantic layer system that manages metrics, dimensions, and KPI computation at company scale. Minerva ingests fact and dimension tables, denormalizes data, and serves it to downstream applications through APIs.

## Scale

- More than 12,000 metrics
- More than 4,000 dimensions
- More than 200 data producers across company functions

## Key Principles

- **Define once, use everywhere**: Single source of truth for metric definitions
- **Metrics as code**: Definitions stored in a centralized GitHub repository with code review, static validation, and test runs
- **Mandatory metadata**: Quality checks, backfills, version control, cost attribution, GDPR selective deletion, access control, auto-deprecation policies, usage-based retention
- **Trust signals**: Extended Airbnb's Data Quality Score to Minerva metrics and dimensions

## Architecture

Data warehouse → Semantic layer (Minerva) → Metrics computation → Metrics API → Analytics tools