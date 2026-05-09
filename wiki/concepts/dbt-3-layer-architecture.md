---
type: concept
title: dbt 3-Layer Architecture
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, architecture, best-practices, data-modeling]
related: [dbt-anti-patterns, dbt-materialization-strategy-matrix, data-mesh, dbt-mesh]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
---
# dbt 3-Layer Architecture

A practical, minimal dbt project architecture that avoids the complexity of over-engineered multi-layer designs. Based on the principle that 3 clear layers beat 7 confusing ones.

## The Layers

```
models/
├── staging/       # One model per source table: clean + rename + type cast
├── intermediate/  # OPTIONAL: complex joins or reusable business logic only
└── marts/         # Final business entities, wide and denormalized
```

### Staging Layer
- Always 1:1 with source tables
- Only cleaning, renaming, and type casting
- No joins, no business logic, no aggregations
- One model per source table

### Intermediate Layer (Optional)
- Only created when logic is reused by 3+ models OR the join is super complex
- Not required for every project
- Can be skipped entirely for simple pipelines

### Marts Layer
- Final business entities ready for consumption
- Wide and denormalized (analyst-friendly)
- Contains business logic, aggregations, and segmentations
- Directly answers business questions

## The Over-Architecture Anti-Pattern

Symptoms of having too many layers:
- "Which layer should this logic go in?" debates
- Simple customer data flowing through 7 different models
- Customer address appearing in 3 different models
- 7 table scans for a simple query
- New features taking days instead of hours

## Results

- New features 3x faster to implement
- New analysts productive in days, not weeks
- Eliminated 4 unnecessary table scans per query
- "Which layer?" discussions eliminated entirely