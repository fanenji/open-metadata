---
type: entity
title: TestRunner
created: 2026-05-14
updated: 2026-05-14
tags: ["data-quality", "sdk", "python", "testing", "validation", "openmetadata"]
related: ["data-quality-as-code", "data-quality", "sdk-configuration", "test-definitions-reference", "external-secrets-manager-setup", "ingestion-framework", "dataframe-validator", "dataframe-chunk-based-validation", "two-phase-data-quality-validation", "publishing-quality-results", "dynamic-test-generation", "multi-table-validation"]
sources: ["testrunner---running-table-level-tests---openmetad-20260514.md", "dataframe-chunk-based-validation---openmetadata-do-20260514.md", "publishing-results-best-practices---openmetadata-d-20260514.md"]
---

# TestRunner

`TestRunner` is a core class in the OpenMetadata Python SDK (`metadata.sdk.data_quality`) that serves as the execution engine for running data quality tests against a table Fully Qualified Name (FQN). It provides methods for adding predefined or custom tests, executing them, and returning results.

## Key Methods

- `TestRunner.for_table(table_fqn)` — Factory method to create a runner for a specific table
- `runner.add_test(test_instance)` — Add a test (e.g., `ColumnValuesToBeNotNull`, `ColumnValuesToBeUnique`, `TableRowCountToBeBetween`)
- `runner.run()` — Execute all added tests and return results

## Usage Patterns

- **Single table validation**: Create a runner for one table, add tests, run, and publish results
- **[[dynamic-test-generation|Dynamic test generation]]**: Create a runner, iterate over table columns from metadata, add tests based on constraints, and run
- **[[multi-table-validation|Multi-table validation]]**: Create a runner per table in a loop, add tests per configuration, run, and aggregate results

## Error Handling

When used with retry logic, `TestRunner` operations should handle `ConnectionError` (retryable, transient) separately from `ValueError` (non-retryable, configuration error). See [[data-quality-as-code]] for the retry pattern.

## Related Classes

- [[DataFrameValidator]] — Validates pandas DataFrames against OpenMetadata table test definitions
- `ColumnValuesToBeNotNull` — Predefined test for NOT NULL column constraints
- `ColumnValuesToBeUnique` — Predefined test for UNIQUE column constraints
- `TableRowCountToBeBetween` — Predefined test for row count ranges