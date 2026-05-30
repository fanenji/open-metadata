---
type: entity
title: DataFrameValidator
created: 2026-05-14
updated: 2026-05-15
tags: ["data-quality", "sdk", "dataframes", "openmetadata", "python", "validation"]
related: ["data-quality", "data-quality-as-code", "test-runner", "publishing-quality-results", "dataframe-chunk-based-validation", "validation-result", "failure-mode"]
sources: ["publishing-results-best-practices---openmetadata-d-20260514.md", "dataframe-chunk-based-validation---openmetadata-do-20260514.md"]
---
# DataFrameValidator

`DataFrameValidator` is a class in the OpenMetadata Python SDK (`metadata.sdk.data_quality.dataframes.dataframe_validator`) that validates pandas DataFrames against OpenMetadata-defined data quality tests. It supports chunk-based processing for large datasets that do not fit in memory and bridges data processing workflows with metadata-driven quality checks.

## Key Methods

- **`add_openmetadata_table_tests(table_fqn: str)`** — Fetches test definitions from OpenMetadata for the specified table and adds them to the validator.
- **`add_tests(*tests)`** — Adds individual test instances (e.g., `ColumnValuesToBeNotNull(column="id")`) directly.
- **`validate(df: pd.DataFrame) -> ValidationResult`** — Validates a single DataFrame chunk against the configured tests.
- **`run(data_chunks, on_success, on_failure, mode=FailureMode.SHORT_CIRCUIT) -> ValidationResult`** — Processes chunks with automatic success/failure callbacks and returns a merged result.

## Usage

### Validating a Single DataFrame

```python
from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Postgres.staging.public.customers")
result = validator.validate(df)
result.publish("Postgres.staging.public.customers")
```

### Chunk-Based Processing

```python
validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Postgres.warehouse.staging.orders")
result = validator.run(
    pd.read_csv("orders.csv", chunksize=5000),
    on_success=load_chunk,
    on_failure=rollback
)
```

## Publishing Results

The `publish()` method on the returned [[validation-result]] sends validation outcomes to OpenMetadata, enabling historical tracking, alerting, dashboards, collaboration, and compliance — see [[publishing-quality-results]].

## Relationship to TestRunner

While [[test-runner]] runs tests directly against a database table, `DataFrameValidator` runs tests against an in-memory DataFrame. This is useful for validating data after transformation but before loading, or for testing data in environments without direct database access.

## Related Classes

- [[validation-result]] — Return type of `validate()` and `run()`; supports `merge()` and `publish()`.
- [[failure-mode]] — Enum controlling validation behavior; currently only `SHORT_CIRCUIT`.
- [[test-runner]] — Alternative class for full-table validation against a database.

## Connections

- Used in [[dataframe-chunk-based-validation]] for processing large datasets.
- Part of the [[two-phase-data-quality-validation]] approach (Phase 1: column-level tests during ETL).
- Integrates with the [[data-quality]] framework in OpenMetadata.
- Enables [[data-quality-as-code]] practices.