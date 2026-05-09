---
type: concept
title: dbt Core Cheat Sheet Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, patterns, best-practices]
related: [dbt-core-cheat-sheet, dbt-command-reference, dbt-testing-patterns, dbt-macros, dbt-project-scaffolding, dbt-cloud-environments, dbt-slim-ci]
sources: ["The Ultimate dbt Core Cheat Sheet.md"]
---
# dbt Core Cheat Sheet Patterns

A collection of practical [[dbt Core]] patterns extracted from [[The Ultimate dbt Core Cheat Sheet]] by [[Mihir Samant]]. These patterns complement the wiki's existing conceptual coverage with concrete, executable examples.

## CTE-Based Modular SQL Pattern

Organize models using Common Table Expressions (CTEs) for readability and maintainability:

```sql
with
source_data as (
    select * from {{ source('raw', 'table') }}
),
transformed as (
    select
        id as customer_id,
        first_name,
        last_name
    from source_data
)
select * from transformed
```

## Staging Model Template

Standard template for staging models that rename and type-cast raw columns:

```sql
with
source as (
    select * from {{ source('raw_data', 'customers') }}
),
renamed as (
    select
        id as customer_id,
        first_name,
        last_name,
        email,
        created_at,
        updated_at
    from source
)
select * from renamed
```

## Environment-Specific Logic

Use `target.name` to conditionally apply different logic in dev vs. prod:

```sql
select *
from my_huge_table
{% if target.name == 'prod' %}
where created_at >= current_date - 365
{% else %}
where created_at >= current_date - 7
{% endif %}
```

## Pre/Post Hook Pattern

Enforce constraints and permissions using hooks:

```sql
{{ config(
    materialized='table',
    pre_hook="alter table {{ this }} add constraint pk_customer primary key (customer_id)",
    post_hook="grant select on {{ this }} to role analytics_users"
) }}
```

## Incremental Model Pattern

Optimize large tables by processing only new or changed records:

```sql
{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

select * from {{ source('raw', 'orders') }}
{% if is_incremental() %}
    where updated_at >= (select max(updated_at) from {{ this }})
{% endif %}
```

## Custom Generic Test Pattern

Define reusable tests in `tests/generic/`:

```sql
{% test valid_email(model, column_name) %}
    select {{ column_name }}
    from {{ model }}
    where {{ column_name }} not like '%@%.%'
{% endtest %}
```

## Logging Pattern

Add visibility to model execution:

```sql
{{ log("Processing " ~ this ~ " at " ~ run_started_at, info=true) }}
```