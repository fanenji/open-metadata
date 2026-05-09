---
type: concept
title: Hybrid Dimensional + One Big Table Modeling
created: 2026-04-04
updated: 2026-04-04
tags: [data-modeling, dimensional-modeling, one-big-table, star-schema, dbt]
related: [dbt, data-quality-dimensions, data-lakehouse, data-mart]
sources: ["Modern data warehouse modeling and ensuring data quality with dbt and OpenMetadata.md"]
---
# Hybrid Dimensional + One Big Table Modeling

A two-layer data modeling architecture that combines a dimensional model (star schema) as the base layer with a denormalized One Big Table (OBT) as the mart layer. This approach serves both technical power users and non-technical business users from the same data pipeline.

## Architecture

### Base Layer: Dimensional Model (Star Schema)
- **Target Audience**: Power users, data analysts, data engineers proficient in SQL.
- **Structure**: Data organized into fact and dimension tables in a star schema.
- **Characteristics**: Normalized to reduce redundancy, optimized for complex joins and aggregations.
- **Use Case**: Foundation for advanced analytics and granular data exploration.

### Mart Layer: One Big Table (OBT)
- **Target Audience**: Business users, executives, non-technical stakeholders.
- **Structure**: Single denormalized table containing all relevant data.
- **Characteristics**: Flattened view, no joins required, simplified queries.
- **Use Case**: Ad-hoc reporting, dashboards, self-service analytics.

## Benefits

- **Dual Audience Coverage**: Serves both SQL-proficient analysts and business users from the same pipeline.
- **Single Source of Truth**: Both layers derive from the same transformations, ensuring consistency.
- **Reduced Maintenance**: No separate ETL for the mart layer; OBT is built directly from the dimensional model.
- **Performance**: Power users get optimized star schema queries; business users get fast, join-free OBT queries.

## Implementation with dbt

In the reference implementation, dbt models are organized as:
- `models/dimensions/` — Dimension tables (e.g., `dim_address`, `dim_customer`)
- `models/facts/` — Fact tables (e.g., `fact_sales`)
- `models/marts/` — One Big Table (e.g., `obt_sales`) built by joining fact and dimension tables

## Related Wiki Pages

- [[dbt]] — The transformation tool used to implement this pattern.
- [[data-quality-dimensions]] — Quality checks applied to both layers.
- [[data-lakehouse]] — The broader architectural context.
- [[data-mart]] — The OBT layer functions as a data mart.