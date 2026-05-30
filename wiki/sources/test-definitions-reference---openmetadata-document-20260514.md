---
type: source
title: "Test Definitions Reference - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-definitions, python-sdk, reference]
related: [data-quality, data-profiling, ingestion-framework, metadata-sdk-data-quality]
sources: ["test-definitions-reference---openmetadata-document-20260514.md"]
---
# Test Definitions Reference - OpenMetadata Documentation

This source is the official API reference for all 25 built-in data quality test definitions available in the OpenMetadata Python SDK (v1.12.x). It provides complete parameter specifications, code examples, and use cases for 9 table-level tests and 16 column-level tests, all importable from the `metadata.sdk.data_quality` module.

## Key Content

- **Import path**: `from metadata.sdk.data_quality import ...`
- **Common parameters**: `name`, `display_name`, `description` (all tests); `column` (column tests only)
- **Customization**: Fluent methods (`with_name`, `with_display_name`, `with_description`, `with_compute_row_count`) or constructor parameters
- **Table-level tests**: `TableRowCountToBeBetween`, `TableRowCountToEqual`, `TableColumnCountToBeBetween`, `TableColumnCountToEqual`, `TableColumnNameToExist`, `TableColumnToMatchSet`, `TableRowInsertedCountToBeBetween`, `TableCustomSQLQuery`, `TableDiff`
- **Column-level tests**: `ColumnValuesToBeNotNull`, `ColumnValuesToBeUnique`, `ColumnValuesToBeInSet`, `ColumnValuesToBeNotInSet`, `ColumnValuesToMatchRegex`, `ColumnValuesToNotMatchRegex`, `ColumnValuesToBeBetween`, `ColumnValueMaxToBeBetween`, `ColumnValueMinToBeBetween`, `ColumnValueMeanToBeBetween`, `ColumnValueMedianToBeBetween`, `ColumnValueStdDevToBeBetween`, `ColumnValuesSumToBeBetween`, `ColumnValuesMissingCount`, `ColumnValueLengthsToBeBetween`, `ColumnValuesToBeAtExpectedLocation`
- **Next steps**: [[test-runner]], [[dataframe-validation]], [[advanced-usage-patterns]]

## Connections

This source is the detailed API reference that extends the [[data-quality]] concept page. It provides the complete catalog of test definitions that the data quality system uses. Some tests (mean, median, stddev) depend on [[data-profiling]] data. Tests are configured and executed as part of [[ingestion-framework]] pipelines.