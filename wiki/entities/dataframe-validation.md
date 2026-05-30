---
type: entity
title: DataFrame Validation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, etl, pandas]
related: [data-quality, data-quality-as-code, data-quality-sdk, ingestion-framework, data-profiling]
sources: ["dataframe-validation---openmetadata-documentation-20260514.md"]
---
# DataFrame Validation

DataFrame Validation is a feature of the OpenMetadata Python SDK that enables validating pandas DataFrames directly within ETL workflows, before data reaches its destination. It is implemented by the `DataFrameValidator` class in the `metadata.sdk.data_quality.dataframes` module.

## Overview

DataFrame validation allows data engineers to catch data quality issues early in the pipeline, preventing bad data from contaminating data warehouses or analytics systems. It supports:

- Validating transformed data before loading to destinations
- Processing large datasets in chunks with memory efficiency
- Short-circuiting ETL pipelines on validation failures
- Providing immediate feedback during data transformations
- Publishing validation results back to OpenMetadata

## Basic Usage

### Creating a Validator

```python
from metadata.sdk import configure
from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

configure(
    host="http://localhost:8585/api",
    jwt_token="your-jwt-token"
)

validator = DataFrameValidator()
```

### Adding Tests

Tests are added using the `add_test()` or `add_tests()` methods. Available test classes include:

- `ColumnValuesToBeNotNull(column="column_name")`
- `ColumnValuesToBeUnique(column="column_name")`
- `ColumnValuesToBeBetween(column="column_name", min_value=0, max_value=120)`
- `ColumnValuesToMatchRegex(column="column_name", regex="pattern")`

### Validating a DataFrame

```python
result = validator.validate(df)

if result.success:
    print("✓ Validation passed - safe to load data")
else:
    for test_case, test_result in result.test_cases_and_results:
        if test_result.testCaseStatus != "Success":
            print(f"  - {test_case.name.root}: {test_result.result}")
```

## Loading Tests from OpenMetadata

Instead of defining tests in code, tests can be loaded from OpenMetadata:

```python
validator = DataFrameValidator()
validator.add_openmetadata_table_tests("BigQuery.analytics.staging.customers")
result = validator.validate(df)
```

This enables separation of concerns: data stewards define quality criteria in the UI, while engineers execute them in code. Test criteria changes do not require code deployments.

## Publishing Results

Validation results can be published back to OpenMetadata:

```python
result.publish("Postgres.warehouse.public.customers")
```

This ensures all data stakeholders are kept up to date with validation outcomes.

## Related Concepts

- [[data-quality-as-code]] — The broader philosophy of defining and running data quality tests programmatically.
- [[data-quality-sdk]] — Reference for the `metadata.sdk.data_quality` module and available test classes.
- [[data-quality]] — The overall data quality framework in OpenMetadata.
- [[data-profiling]] — Complements validation by observing data characteristics rather than enforcing rules.
- [[ingestion-framework]] — Validation acts as a gate before ingestion/loading.