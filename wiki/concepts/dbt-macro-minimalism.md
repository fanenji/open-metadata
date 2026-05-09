---
type: concept
title: dbt Macro Minimalism
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, macros, best-practices, code-quality]
related: [dbt-anti-patterns, dbt-testing-patterns, dbt-macros]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
---
# dbt Macro Minimalism

A design philosophy for dbt macros that prioritizes readability and debuggability over reusability and cleverness. The core principle: "Readable beats reusable 90% of the time."

## Guidelines

1. **Single-purpose macros**: Each macro should do exactly one thing. If a macro has multiple parameters that change its behavior significantly, it's too complex.
2. **No macro-calling-macros**: Macros that call other macros create debugging nightmares. Error messages point to generated SQL, not the source of the problem.
3. **3+ model rule**: Only create a macro if it will be used in 3 or more models. Otherwise, inline the logic.
4. **Immediately readable**: A new team member should understand what a macro does without documentation.
5. **Simple over clever**: A simple CASE statement is better than a complex macro that generates CASE statements.

## Example: Before (Over-Engineered)

```sql
{% macro dynamic_aggregation_with_conditions(
    base_table, group_columns, metric_column,
    filters=[], aggregation_type='sum',
    include_percentiles=false, date_column=none, date_range_days=30
) %}
-- 8 parameters, calls other macros, generates complex SQL
{% endmacro %}
```

## Example: After (Minimalist)

```sql
{% macro recent_orders(days_back=30) %}
  order_date >= CURRENT_DATE - {{ days_back }}
  AND status = 'completed'
  AND channel IS NOT NULL
{% endmacro %}

{% macro revenue_aggregations(revenue_col='revenue') %}
  SUM({{ revenue_col }}) as total_revenue,
  AVG({{ revenue_col }}) as avg_revenue,
  COUNT(*) as order_count
{% endmacro %}
```

## Benefits

- Debugging time reduced from hours to minutes
- New team members can understand macros immediately
- Higher actual reuse (simple macros used in 15+ models vs. complex macros in 2)
- No need for macro documentation — the code is self-explanatory