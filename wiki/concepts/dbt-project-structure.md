---
type: concept
title: dbt Project Structure
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, project-structure, best-practices, medallion-architecture]
related: [dbt-project-scaffolding, dbt-naming-conventions, dbt-macros, dbt-testing-patterns, data-quality-certification-vs-usability-certification]
sources: ["Report dettagliato su dbt software.md"]
---
# dbt Project Structure

The structure of a dbt project is a direct application of the software engineering principle of "separation of concerns" to data modeling. It is not an arbitrary convention but a design pattern that deliberately isolates different types of logic to maximize maintainability and reusability.

## Directory Anatomy

A standard dbt project created via `dbt init` contains the following directories:

| Directory | Purpose | Git-Ignored? |
|-----------|---------|--------------|
| `models/` | Core of the project — SQL/Python files defining transformations | No |
| `seeds/` | CSV files for static data loaded via `dbt seed` | No |
| `tests/` | Custom singular tests (SQL queries returning zero rows to pass) | No |
| `macros/` | Reusable Jinja macros | No |
| `snapshots/` | Snapshot configurations for tracking data changes over time | No |
| `analyses/` | One-off analysis queries benefiting from versioning and templating | No |
| `target/` | Compiled SQL, logs, and artifacts (auto-generated) | **Yes** |
| `dbt_packages/` | Downloaded external packages (auto-generated) | **Yes** |

## Model Layer Organization

The `models/` directory should be organized to reflect the Medallion Architecture:

### Staging Layer (`models/staging/`)
- One-to-one relationship with source tables
- Only transformations allowed: column renaming, data type casting, basic cleaning
- Files prefixed with `stg_` (e.g., `stg_customers.sql`)
- **Purpose:** Create a clean, consistent interface with raw data, isolating the rest of the project from upstream changes

### Intermediate Layer (`models/intermediate/`)
- Joins multiple staging models, applies complex business logic
- Often not exposed directly to end users
- Files prefixed with `int_` (e.g., `int_orders_aggregated.sql`)
- **Purpose:** Implement reusable business logic, preventing monolithic models

### Marts Layer (`models/marts/`)
- Final models ready for consumption (BI tools, ML, analytics)
- Wide, denormalized tables serving specific business domains
- Files prefixed with `dim_` (dimensions) and `fct_` (facts)
- **Purpose:** Act as an "API layer" for data consumers

## Key Configuration Files

- **`dbt_project.yml`:** Main project configuration — defines project name, version, paths, and default model configurations. This file is committed to version control.
- **`profiles.yml`:** Database connection credentials — stored outside the project directory (`~/.dbt/`) to prevent accidental credential commits. This separation is a deliberate security mechanism.