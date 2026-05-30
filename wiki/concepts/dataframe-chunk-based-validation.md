---
type: concept
title: "Dataframe Chunk Based Validation"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: DataFrame Chunk-Based Validation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, python, validation, chunking, etl]
related: [dataframe-validator, two-phase-data-quality-validation, data-quality, test-runner, validation-result, failure-mode]
sources: ["dataframe-chunk-based-validation---openmetadata-do-20260514.md"]
---
# DataFrame Chunk-Based Validation

Chunk-based validation is a technique for performing data quality checks on large pandas DataFrames that do not fit in memory. Instead of loading the entire dataset at once, the data is split into smaller chunks, each chunk is validated individually, and the results are aggregated.

## Motivation

Standard data quality validation requires loading the full dataset into memory. For large datasets (e.g., multi-gigabyte CSV files), this is infeasible. Chunk-based validation solves this by processing data in manageable pieces.

## Implementation Methods

### Method 1: Manual Chunk Validation

The developer manually iterates over chunks, validates each one, collects results, and merges them at the end.

```python
import pandas as pd
from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator, ValidationResult

validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Postgres.warehouse.staging.transactions")
results = []

for chunk in pd.read_csv("large_file.csv", chunksize=10000):
    result = validator.validate(chunk)
    results.append(result)
    if result.success:
        load_chunk_to_database(chunk)
    else:
        rollback_all_chunks()
        break

final_result = ValidationResult.merge(*results)
final_result.publish("Postgres.warehouse.staging.transactions")
```

### Method 2: Using the `run()` Method (Recommended)

The `run()` method provides a cleaner approach with automatic chunk handling and success/failure callbacks.

```python
from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator
import pandas as pd

validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Postgres.warehouse.staging.orders")

def load_chunk(df, validation_result):
    # Load validated chunk to database
    pass

def handle_failure(df, validation_result):
    # Rollback on validation failure
    pass

result = validator.run(
    pd.read_csv("orders.csv", chunksize=5000),
    on_success=load_chunk,
    on_failure=handle_failure
)
result.publish("Postgres.warehouse.staging.orders")
```

## Transaction-Safe Chunk Processing

Use a context manager to ensure atomic all-or-nothing behavior when loading validated chunks. The `DatabaseSession` class wraps a database connection and transaction, providing `load_chunk` and `rollback` methods that can be passed directly to `validator.run()`.

## Failure Modes

As of SDK v1.11.0.0, only `SHORT_CIRCUIT` is supported: validation stops at the first chunk that fails, preventing further processing. Future versions are expected to add modes for reporting failing rows or skipping failing batches.

## Important Considerations

- **WholeTableTestsWarning:** The SDK warns when tests requiring the full dataset (e.g., `TableRowCountToBeBetween`, `ColumnValuesSumToBeBetween`) are applied to chunks, as they may produce incorrect results.
- **Column-level vs. Table-level tests:** Column-level tests (e.g., `ColumnValuesToBeNotNull`, `ColumnValuesToBeUnique`) are safe for chunks. Table-level tests (e.g., `TableRowCountToBeBetween`) require the full dataset.

## Best Practices

- Validate before loading to catch issues before contaminating the warehouse.
- Use transactional chunk processing for atomic behavior.
- Leverage OpenMetadata tests defined by data stewards.
- Publish results for tracking and alerting.
- Handle failures gracefully with rollback and alerting.
- Use appropriate tests for chunks — avoid full-table tests.

## Connections

- [[dataframe-validator]] — The SDK class that provides chunk-based validation.
- [[two-phase-data-quality-validation]] — The recommended architectural pattern.
- [[data-quality]] — The broader concept of data quality in OpenMetadata.
- [[test-runner]] — Used for full-table validation after loading.
- [[validation-result]] — Encapsulates validation outcomes with `merge()` and `publish()`.
- [[failure-mode]] — Enum controlling validation behavior on failure.