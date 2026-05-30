---
type: entity
title: TableCustomSQLQuery
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-definitions, custom-sql]
related: [table-level-tests, data-quality, metadata-sdk-data-quality]
sources: ["test-definitions-reference---openmetadata-document-20260514.md"]
---
# TableCustomSQLQuery

`TableCustomSQLQuery` is a table-level test definition that validates data using a custom SQL query expression. It is the most flexible test in the OpenMetadata data quality framework, enabling arbitrary business logic validation.

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `sql_expression` | str | Yes | SQL query to execute |
| `strategy` | str | No | `"ROWS"` (default) or `"COUNT"` |

## Strategies

### ROWS Strategy (default)
Returns the failing rows from the query. The test passes if no rows are returned.

```python
test = TableCustomSQLQuery(
    sql_expression="SELECT * FROM {table} WHERE price < 0",
    strategy="ROWS"
)
```

### COUNT Strategy
Expects the query to return a single row with a count. The test passes if the count is 0.

```python
test = TableCustomSQLQuery(
    sql_expression="""
    SELECT COUNT(*) FROM {table} t
    LEFT JOIN parent_table p ON t.parent_id = p.id
    WHERE p.id IS NULL
    """,
    strategy="COUNT"
)
```

## The `{table}` Placeholder

The `{table}` placeholder in the SQL expression resolves to the table being tested at runtime. This enables reusable custom SQL tests that can be applied across different tables without modification.

## Use Cases

- Implement custom business logic validation
- Validate referential integrity across tables
- Check complex data relationships
- Detect orphaned records
- Validate derived or computed fields

## Related

- [[table-level-tests]] — Parent category of table-level tests
- [[data-quality]] — The overarching data quality concept