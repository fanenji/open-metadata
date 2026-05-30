---
type: concept
title: "Test Definitions Reference"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Test Definitions Reference
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, testing, reference]
related: [test-runner, data-quality-as-code, data-quality]
sources: ["testrunner---running-table-level-tests---openmetad-20260514.md"]
---

# Test Definitions Reference

This page catalogs the built-in test definition classes available in the OpenMetadata Python SDK for programmatic data quality testing. These classes are used with the [[test-runner|TestRunner]] fluent API.

## Table-Level Tests

| Class | Description | Parameters |
|-------|-------------|------------|
| `TableRowCountToBeBetween` | Validates that the total row count of a table falls within a specified range | `min_count`, `max_count` |

## Column-Level Tests

| Class | Description | Parameters |
|-------|-------------|------------|
| `ColumnValuesToBeNotNull` | Ensures no null values exist in a specified column | `column` |
| `ColumnValuesToBeUnique` | Validates that all values in a column are unique | `column` |
| `ColumnValuesToMatchRegex` | Checks column values against a regular expression pattern | `column`, `regex` |
| `ColumnValuesToBeBetween` | Validates that numeric column values fall within a specified range | `column`, `min_value`, `max_value` |

## Customizing Test Metadata

All test classes support fluent customization:

```python
test = ColumnValuesToBeNotNull(column="email") \
    .with_name("email_not_null_check") \
    .with_display_name("Email Not Null Validation") \
    .with_description("Ensures all customer records have valid email addresses")
```

Or via constructor parameters:

```python
test = ColumnValuesToBeNotNull(
    column="email",
    name="email_not_null_check",
    display_name="Email Not Null Validation",
    description="Ensures all customer records have valid email addresses"
)
```

## Row Count Computation

Some tests support computing the number and percentage of rows that passed or failed:

```python
test = ColumnValuesToBeBetween(
    column="age",
    min_value=18,
    max_value=120
).with_compute_row_count(True)
```

## Test Results

Results contain:
- `testCase.name.root` — Test name
- `testCase.testDefinition.name` — Test type
- `testCaseResult.testCaseStatus` — Status: Success, Failed, or Aborted
- `testCaseResult.result` — Detailed result message
- `testCaseResult.timestamp` — Execution timestamp
- `testCaseResult.passedRows` / `failedRows` — Row-level statistics (if enabled)
- `testCaseResult.passedRowsPercentage` — Pass percentage

## Related

- [[test-runner]] — The SDK class that executes these test definitions
- [[data-quality-as-code]] — The paradigm of programmatic data quality testing
- [[data-quality]] — Core concept of data quality in OpenMetadata