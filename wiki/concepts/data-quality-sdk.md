---
type: concept
title: Data Quality SDK
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, python, api]
related: [dataframe-validation, data-quality-as-code, data-quality, data-profiling]
sources: ["dataframe-validation---openmetadata-documentation-20260514.md"]
---
# Data Quality SDK

The Data Quality SDK is the Python module `metadata.sdk.data_quality` that provides programmatic access to OpenMetadata's data quality framework. It enables defining, running, and publishing data quality tests directly from code.

## Module Structure

The SDK is organized into submodules:

- `metadata.sdk.data_quality` — Core test classes and utilities
- `metadata.sdk.data_quality.dataframes` — DataFrame-specific validation tools
- `metadata.sdk.data_quality.dataframes.dataframe_validator` — The `DataFrameValidator` class

## Available Test Classes

The SDK provides a library of test classes for column-level validation. Examples documented in the official guide include:

| Test Class | Purpose | Parameters |
|------------|---------|------------|
| `ColumnValuesToBeNotNull` | Ensures column has no null values | `column` |
| `ColumnValuesToBeUnique` | Ensures all values in column are unique | `column` |
| `ColumnValuesToBeBetween` | Ensures values fall within a range | `column`, `min_value`, `max_value` |
| `ColumnValuesToMatchRegex` | Ensures values match a pattern | `column`, `regex` |

> **Note:** The full list of available test classes is not documented in this source. See the [Test Definitions Reference](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/tests-yaml-config) for a complete catalog.

## Key Classes

### DataFrameValidator

The primary class for validating pandas DataFrames. Located in `metadata.sdk.data_quality.dataframes.dataframe_validator`.

**Methods:**
- `add_test(test)` — Add a single test definition
- `add_tests(*tests)` — Add multiple test definitions
- `validate(df)` — Run all added tests against a DataFrame, returns a result object
- `add_openmetadata_table_tests(fqn)` — Load tests from OpenMetadata for a given table FQN

### Result Object

Returned by `validator.validate()`. Contains:
- `success` — Boolean indicating if all tests passed
- `test_cases_and_results` — Iterable of `(test_case, test_result)` pairs

**Methods:**
- `publish(fqn)` — Publish validation results to OpenMetadata

## Configuration

The SDK must be configured before use:

```python
from metadata.sdk import configure

configure(
    host="http://localhost:8585/api",
    jwt_token="your-jwt-token"
)
```

## Related Concepts

- [[dataframe-validation]] — The primary use case for the Data Quality SDK.
- [[data-quality-as-code]] — The broader philosophy enabled by the SDK.
- [[data-quality]] — The overall data quality framework in OpenMetadata.
- [[data-profiling]] — Complements the SDK's validation capabilities.