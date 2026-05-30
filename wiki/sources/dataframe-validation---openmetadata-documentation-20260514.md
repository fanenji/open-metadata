---
type: source
title: "DataFrame Validation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, dataframe-validation, sdk, etl]
related: [dataframe-validation, data-quality-as-code, data-quality-sdk, data-quality]
sources: ["dataframe-validation---openmetadata-documentation-20260514.md"]
---
# DataFrame Validation - OpenMetadata Documentation

**Source:** [https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/dataframe-validation](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/dataframe-validation)

This official OpenMetadata documentation page introduces the `DataFrameValidator` class, which enables validating pandas DataFrames directly within ETL workflows before data reaches its destination. It covers basic usage, adding tests, validating DataFrames, a complete ETL example, and loading tests from OpenMetadata.

## Key Content

- **DataFrameValidator class**: Core tool for in-ETL validation of pandas DataFrames.
- **SDK configuration**: Using `metadata.sdk.configure()` with host and JWT token.
- **Test definitions**: Examples using `ColumnValuesToBeNotNull`, `ColumnValuesToBeUnique`, `ColumnValuesToBeBetween`, and `ColumnValuesToMatchRegex`.
- **Short-circuit ETL pattern**: Halting pipeline execution on validation failure to prevent downstream contamination.
- **Test loading from OpenMetadata**: Using `validator.add_openmetadata_table_tests()` to load tests defined in the UI, enabling separation of concerns.
- **Result publishing**: Using `result.publish()` to send validation results back to OpenMetadata.

## Relevance

This source is directly relevant to the [[data-quality]] concept and introduces the [[dataframe-validation]] and [[data-quality-as-code]] patterns. It demonstrates how OpenMetadata's data quality framework can be used programmatically within ETL pipelines.