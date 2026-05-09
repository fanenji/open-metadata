---
type: concept
title: dbt Modeling Layers
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, architecture, data-modeling]
related: [dbt-best-practices, software-defined-assets]
sources: ["Best Practices for Workflows A Guide to Effective dbt Use-20260506.md"]
---
# dbt Modeling Layers

A structural pattern for organizing dbt models into discrete layers to separate raw data ingestion from complex business logic.

## Standard Layers
1. **Staging Layer (`models/staging/`):** 
   - Focuses on source alignment.
   - Performs renaming and recasting (e.g., converting types, standardizing timestamps).
   - References raw data via `{{ source(...) }}`.
2. **Intermediate Layer:** 
   - Breaks down complex, multi-CTE models into smaller, modular pieces.
   - Facilitates independent testing and reuse of logic.
3. **Mart/Analytics Layer (`models/analytics/`):** 
   - Contains business-centric transformations.
   - Provides the final, consumption-ready datasets for BI tools.

## Advantages
- **Maintainability:** Changes in source schemas are isolated to the staging layer.
- **Clarity:** Reduces code duplication by promoting modularity.
- **Testability:** Smaller models are easier to validate with `dbt tests`.