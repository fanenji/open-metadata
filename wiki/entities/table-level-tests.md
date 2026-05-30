---
type: entity
title: Table-Level Tests
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-definitions, table]
related: [data-quality, column-level-tests, metadata-sdk-data-quality, table-custom-sql-query]
sources: ["test-definitions-reference---openmetadata-document-20260514.md"]
---
# Table-Level Tests

Table-level tests are data quality tests that validate properties of entire tables. OpenMetadata provides 9 built-in table-level test definitions, all importable from [[metadata-sdk-data-quality]].

## Available Tests

| Test | Purpose | Key Parameters |
|------|---------|----------------|
| `TableRowCountToBeBetween` | Row count within range | `min_count`, `max_count` |
| `TableRowCountToEqual` | Exact row count | `row_count` |
| `TableColumnCountToBeBetween` | Column count within range | `min_count`, `max_count` |
| `TableColumnCountToEqual` | Exact column count | `column_count` |
| `TableColumnNameToExist` | Specific column exists | `column_name` |
| `TableColumnToMatchSet` | Columns match expected set | `column_names`, `ordered` |
| `TableRowInsertedCountToBeBetween` | Inserted rows in time range | `min_count`, `max_count`, `range_type`, `range_interval` |
| `TableCustomSQLQuery` | Custom SQL validation | `sql_expression`, `strategy` |
| `TableDiff` | Compare two tables | `table2`, `key_columns`, `use_columns` |

## Common Use Cases

- **Data volume monitoring**: Detect data loss or unexpected surges using row count tests
- **Schema validation**: Ensure column counts and names match expectations
- **Schema evolution tracking**: Monitor column additions, removals, and renames
- **Ingestion pipeline monitoring**: Validate ETL job completions with inserted count tests
- **Custom business logic**: Implement complex validation rules via [[table-custom-sql-query]]
- **Data migration validation**: Compare source and target tables with `TableDiff`

## Related

- [[column-level-tests]] — The complementary category of column-level tests
- [[data-quality]] — The overarching data quality concept
- [[table-custom-sql-query]] — Detailed page for the custom SQL test