---
type: entity
title: "Validation Result"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: ValidationResult
created: 2026-05-14
updated: 2026-05-14
tags: [sdk, python, data-quality, validation]
related: [dataframe-validator, dataframe-chunk-based-validation, data-quality]
sources: ["dataframe-chunk-based-validation---openmetadata-do-20260514.md"]
---
# ValidationResult

`ValidationResult` is a class in the OpenMetadata Python SDK (`metadata.sdk.data_quality.dataframes`) that encapsulates the outcome of a data quality validation. It provides methods for accessing individual test results, merging results from multiple chunks, and publishing aggregated results back to OpenMetadata.

## Key Properties

- **`success: bool`** — Whether all tests passed.
- **`test_cases_and_results`** — Iterable of `(test_case, test_result)` pairs, where `test_result.testCaseStatus` indicates pass/fail and `test_result.result` contains details.

## Key Methods

- **`ValidationResult.merge(*results) -> ValidationResult`** — Static method that merges multiple `ValidationResult` instances (e.g., from different chunks) into a single aggregated result.
- **`publish(table_fqn: str)`** — Publishes the validation results to OpenMetadata for historical tracking, alerting, and visualization in the UI.

## Usage

```python
from metadata.sdk.data_quality.dataframes import ValidationResult

# Merge results from multiple chunks
merged_result = ValidationResult.merge(*results)

# Publish aggregated results
merged_result.publish("Postgres.warehouse.staging.transactions")
```

## Connections

- Returned by [[dataframe-validator]] methods `validate()` and `run()`.
- Used in [[dataframe-chunk-based-validation]] for aggregating chunk results.
- Enables centralized data quality reporting in the [[data-quality]] framework.