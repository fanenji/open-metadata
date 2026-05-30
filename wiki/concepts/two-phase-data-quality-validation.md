---
type: concept
title: "Two Phase Data Quality Validation"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Two-Phase Data Quality Validation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, architecture, etl, validation]
related: [dataframe-chunk-based-validation, dataframe-validator, test-runner, data-quality, data-profiling]
sources: ["dataframe-chunk-based-validation---openmetadata-do-20260514.md"]
---
# Two-Phase Data Quality Validation

Two-phase data quality validation is a recommended architectural pattern for validating large datasets that do not fit in memory. It splits validation into two distinct phases, each using the appropriate tool and test type.

## Phase 1: Column-Level Tests During ETL

During the ETL (Extract, Transform, Load) process, use [[dataframe-validator]] with chunk-based validation to run column-level tests on each chunk as it is processed. These tests do not require the full dataset and are safe for chunk processing.

**Suitable tests:** `ColumnValuesToBeNotNull`, `ColumnValuesToBeUnique`, `ColumnValuesToBeBetween`, etc.

**Tool:** [[dataframe-validator]] with the `run()` method and success/failure callbacks.

## Phase 2: Table-Level Tests After Loading

After all chunks have been successfully loaded into the database, use [[test-runner]] to run full-table tests that require the complete dataset.

**Suitable tests:** `TableRowCountToBeBetween`, `ColumnValuesSumToBeBetween`, etc.

**Tool:** [[test-runner]] (automatically publishes results to OpenMetadata).

## Benefits

- **Memory efficiency:** Large datasets are processed in chunks during ETL.
- **Correctness:** Full-table tests are run against the complete dataset after loading.
- **Atomicity:** Transaction-safe chunk processing ensures all-or-nothing behavior.
- **Comprehensive coverage:** Both column-level and table-level quality are validated.

## Example

```python
# Phase 1: Validate chunks during ETL (column-level only)
chunk_validator = DataFrameValidator()
chunk_validator.add_tests(
    ColumnValuesToBeNotNull(column="id"),
    ColumnValuesToBeUnique(column="id"),
    ColumnValuesToBeBetween(column="amount", min_value=0)
)
result = chunk_validator.run(
    pd.read_csv("data.csv", chunksize=10000),
    on_success=load_chunk,
    on_failure=rollback
)

# Phase 2: Validate table metrics after loading (table-level)
if result.success:
    table_validator = TestRunner.for_table("Postgres.warehouse.staging.transactions")
    table_validator.add_tests(
        TableRowCountToBeBetween(min_count=10000),
        ColumnValuesSumToBeBetween(column="amount", min_value=1000000)
    )
    table_results = table_validator.run()
```

## Connections

- Phase 1 uses [[dataframe-chunk-based-validation]] for memory-efficient processing.
- Phase 2 uses [[test-runner]] for full-table validation.
- Both phases are part of the [[data-quality]] framework.
- Related to [[data-profiling]] for understanding data structure before validation.