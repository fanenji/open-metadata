---
type: entity
title: Column-Level Tests
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-definitions, column]
related: [data-quality, table-level-tests, metadata-sdk-data-quality]
sources: ["test-definitions-reference---openmetadata-document-20260514.md"]
---
# Column-Level Tests

Column-level tests are data quality tests that validate properties of specific columns in a table. OpenMetadata provides 16 built-in column-level test definitions, all importable from [[metadata-sdk-data-quality]].

## Available Tests

| Test | Purpose | Key Parameters |
|------|---------|----------------|
| `ColumnValuesToBeNotNull` | No null values | `column` |
| `ColumnValuesToBeUnique` | All values unique | `column` |
| `ColumnValuesToBeInSet` | Values in allowed set | `column`, `allowed_values` |
| `ColumnValuesToBeNotInSet` | No forbidden values | `column`, `forbidden_values` |
| `ColumnValuesToMatchRegex` | Values match pattern | `column`, `regex` |
| `ColumnValuesToNotMatchRegex` | Values don't match pattern | `column`, `regex` |
| `ColumnValuesToBeBetween` | Values in numeric range | `column`, `min_value`, `max_value` |
| `ColumnValueMaxToBeBetween` | Max value in range | `column`, `min_value`, `max_value` |
| `ColumnValueMinToBeBetween` | Min value in range | `column`, `min_value`, `max_value` |
| `ColumnValueMeanToBeBetween` | Mean in range | `column`, `min_value`, `max_value` |
| `ColumnValueMedianToBeBetween` | Median in range | `column`, `min_value`, `max_value` |
| `ColumnValueStdDevToBeBetween` | Std dev in range | `column`, `min_value`, `max_value` |
| `ColumnValuesSumToBeBetween` | Sum in range | `column`, `min_value`, `max_value` |
| `ColumnValuesMissingCount` | Count of missing values | `column`, `missing_count_value`, `missing_value_match` |
| `ColumnValueLengthsToBeBetween` | String length in range | `column`, `min_length`, `max_length` |
| `ColumnValuesToBeAtExpectedLocation` | Value at row position | `column`, `expected_value`, `row_index` |

## Common Use Cases

- **Data completeness**: Ensure required fields are populated (`ColumnValuesToBeNotNull`, `ColumnValuesMissingCount`)
- **Uniqueness validation**: Validate primary keys and unique identifiers (`ColumnValuesToBeUnique`)
- **Categorical validation**: Enforce enum constraints (`ColumnValuesToBeInSet`, `ColumnValuesToBeNotInSet`)
- **Format validation**: Ensure data format consistency (`ColumnValuesToMatchRegex`, `ColumnValuesToNotMatchRegex`)
- **Statistical monitoring**: Detect data drift and outliers (`ColumnValueMeanToBeBetween`, `ColumnValueStdDevToBeBetween`)
- **String constraints**: Validate lengths and prevent truncation (`ColumnValueLengthsToBeBetween`)
- **Sorted data validation**: Check ordered results (`ColumnValuesToBeAtExpectedLocation`)

## Related

- [[table-level-tests]] — The complementary category of table-level tests
- [[data-quality]] — The overarching data quality concept
- [[data-profiling]] — Statistical tests (mean, median, stddev) depend on profiling data