---
type: concept
title: dbt Naming Conventions
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, naming-conventions, style-guide, best-practices]
related: [dbt-project-structure, dbt-project-scaffolding]
sources: ["Report dettagliato su dbt software.md"]
---
# dbt Naming Conventions

Adopting and enforcing a style guide is fundamental for long-term readability and maintainability of dbt projects. The following conventions are recommended by dbt Labs.

## General Rules

- Use `snake_case` for all objects (models, columns, schemas).
- Model names should be plural (e.g., `orders`, `customers`).

## Column Naming

| Column Type | Convention | Example |
|-------------|------------|---------|
| Primary Key | `<object>_id` | `order_id`, `customer_id` |
| Boolean | `is_` or `has_` prefix | `is_active`, `has_ordered` |
| Timestamp | `_at` suffix | `created_at`, `updated_at` |
| Date | `_date` suffix | `order_date`, `ship_date` |
| Foreign Key | `<referenced_object>_id` | `customer_id`, `product_id` |

## Model Prefixes

| Layer | Prefix | Example |
|-------|--------|---------|
| Staging | `stg_` | `stg_customers.sql` |
| Intermediate | `int_` | `int_orders_aggregated.sql` |
| Dimension | `dim_` | `dim_customers.sql` |
| Fact | `fct_` | `fct_orders.sql` |

## General Guidelines

- Use explicit names — avoid abbreviations (use `customer_id` instead of `cust_id`).
- Be consistent across the entire project.
- Document naming conventions in a project-level `CONTRIBUTING.md` or similar file.
- Enforce conventions through code review and, where possible, automated linting.