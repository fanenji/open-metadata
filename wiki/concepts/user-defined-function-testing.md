---
type: concept
title: User-Defined Function Testing in dbt
created: 2026-05-08
updated: 2026-05-08
tags: [dbt, udf, testing, macros]
related: [dbt-testing-patterns, dbt-macros, dbt-unit-testing, singular-tests, dbt-expectations]
sources: ["research-dbt-testing-patterns-update-2026-05-08.md"]
---
# User-Defined Function Testing in dbt

User-defined functions (UDFs) lack first-class support in dbt (no native `ref()` or `source()` for UDFs), but they can be deployed and tested using a documented pattern involving macros, hooks, and singular tests.

## Deployment Pattern

1. **Define the UDF as a macro** that accepts a schema parameter (e.g., `{{ target.schema }}`).
2. **Create a macro that calls `CREATE OR REPLACE FUNCTION`** — placed in `macros/udfs/`.
3. **Execute the macro via a hook** in `dbt_project.yml` under `on-run-start`.
4. **Test the UDF** with a singular test that calls the function and expects no results.

### Example UDF Macro (BigQuery)

```sql
{% macro make_func_math_radian() %}
CREATE OR REPLACE FUNCTION f_math.radian() RETURNS FLOAT64 AS (
  `{{ target.project }}`.f_math.pi() / 180
);
{% endmacro %}
```

## Testing Approaches

- **Singular tests**: Write a SQL query that calls the UDF and returns rows when the function behaves incorrectly. This is the most common approach.
- **Unit tests (v1.8+)**: When a UDF is used within a model, unit tests can validate the model's logic including the UDF call, using mock inputs and expected outputs.
- **Limitations**: There is no first-class `dbt test` command for UDFs alone. Pre-hooks can clutter console output.

## Warehouse-Specific Considerations

- **BigQuery**: Requires fully qualified UDF references using `{{ target.project }}`.
- **Snowflake**: Applies the volatility attribute; BigQuery ignores it.
- **Redshift, Databricks**: Also supported with the same general pattern.

## Related Concepts

- [[dbt-testing-patterns]] — Overall categorization of dbt testing strategies.
- [[dbt-macros]] — Reusable Jinja code used to define UDF deployment logic.
- [[dbt-unit-testing]] — Native unit test feature for validating model logic.
- [[singular-tests]] — One-off SQL queries used for UDF testing.