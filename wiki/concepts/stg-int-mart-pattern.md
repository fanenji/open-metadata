---
type: concept
title: STG $\rightarrow$ INT $\rightarrow$ MART Pattern
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, architecture, modeling]
related: [dbt, data-lineage]
sources: ["10 Game-Changing dbt Tips I Wish I Knew Before My First Production Model 1.md"]
---
# STG $\rightarrow$ INT $\rightarrow$ MART Pattern

The **STG $\rightarrow$ INT $\rightarrow$ MART** pattern is a layered architectural approach to data modeling in [[dbt]]. It promotes modularity, traceability, and reusability by separating concerns into distinct layers.

## Layers

1.  **Staging (STG)**: The entry point for raw data. This layer focuses on cleaning, renaming columns, and basic type casting. It should mirror the source structure but in a standardized format.
2.  **Intermediate (INT)**: The transformation layer. This is where complex business logic, joins, and aggregations occur. These models are typically not exposed to end-users but serve as building blocks for marts.
3.  **Mart (MART)**: The presentation layer. These models are optimized for reporting and analytics. They are the final outputs consumed by BI tools and stakeholders.

## Benefits

- **Modularity**: Changes in source logic are isolated to the STG layer.
- **Traceability**: Clear path from raw data to final reporting.
- **Reusability**: Intermediate models can be reused across multiple marts.
- **Testing**: Easier to implement granular tests at each stage of the pipeline.
