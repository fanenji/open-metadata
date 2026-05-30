---
type: concept
title: Custom SQL Test Definitions
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sql, test-library, openmetadata]
related: [test-library, test-platforms, data-quality]
sources: ["test-library-custom-sql-based-data-quality-tests---20260514.md"]
---
# Custom SQL Test Definitions

Custom SQL test definitions are the core building blocks of the [[test-library|Test Library]]. They are reusable, parameterized SQL queries that define data quality validation rules. The test fails if the query returns one or more rows; an empty result set means the test passes (fail-on-rows semantics).

## Reserved Parameters

These parameters are automatically resolved at runtime:

| Parameter | Description |
|-----------|-------------|
| `{{ table_name }}` | The fully qualified name of the table being tested |
| `{{ column_name }}` | The name of the column being tested (for column-level tests) |

## User-Defined Parameters

Custom placeholders defined by the test creator using the `{{ parameter_name }}` syntax. Users provide values when creating test cases. Parameters are defined in the test definition form by clicking **Add Parameter** and entering the name and optional description.

## SQL Expression Examples

### Example 1: Column Values Greater Than Threshold
```sql
SELECT {{ column_name }} AS col
FROM {{ table_name }}
WHERE {{ column_name }} < {{ min_value }}
```
Parameters: `min_value` (minimum acceptable value)

### Example 2: Column Values Within Range
```sql
SELECT {{ column_name }} AS col
FROM {{ table_name }}
WHERE {{ column_name }} < {{ min_value }} OR {{ column_name }} > {{ max_value }}
```
Parameters: `min_value`, `max_value`

### Example 3: No Null Values in Required Columns
```sql
SELECT {{ column_name }}
FROM {{ table_name }}
WHERE {{ column_name }} IS NULL
```
Parameters: None (uses only reserved parameters)

### Example 4: Table Row Count Within Expected Range
```sql
SELECT COUNT(*) AS row_count
FROM {{ table_name }}
HAVING COUNT(*) < {{ min_rows }} OR COUNT(*) > {{ max_rows }}
```
Parameters: `min_rows`, `max_rows`

### Example 5: Referential Integrity Check
```sql
SELECT t.{{ column_name }}
FROM {{ table_name }} t
LEFT JOIN {{ reference_table }} r ON t.{{ column_name }} = r.{{ reference_column }}
WHERE r.{{ reference_column }} IS NULL
AND t.{{ column_name }} IS NOT NULL
```
Parameters: `reference_table`, `reference_column`

### Example 6: Date Freshness Check
```sql
SELECT MAX({{ date_column }}) AS latest_date
FROM {{ table_name }}
HAVING MAX({{ date_column }}) < CURRENT_DATE - INTERVAL '{{ max_age_days }}' DAY
```
Parameters: `date_column`, `max_age_days`

**Note**: Date interval syntax varies by database. The example uses PostgreSQL syntax; adjust for your supported data sources.

## Best Practices

- **Return failing rows**: Structure queries to return rows that fail validation.
- **Be specific**: Check one condition per test.
- **Consider performance**: Use WHERE clauses; avoid full table scans.
- **Test your SQL**: Validate manually before creating the test definition.
- **Documentation**: Provide clear descriptions and examples for parameters.