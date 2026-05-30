---
type: entity
title: metadata.sdk.data_quality
created: 2026-05-14
updated: 2026-05-14
tags: [python-sdk, data-quality, module]
related: [data-quality, test-runner, dataframe-validation]
sources: ["test-definitions-reference---openmetadata-document-20260514.md"]
---
# metadata.sdk.data_quality

The `metadata.sdk.data_quality` Python module is the central import source for all built-in data quality test definitions in OpenMetadata. It provides 25 test classes organized into two categories: table-level tests and column-level tests.

## Import

```python
from metadata.sdk.data_quality import (
    # Table tests
    TableRowCountToBeBetween,
    TableColumnCountToBeBetween,
    TableCustomSQLQuery,
    # Column tests
    ColumnValuesToBeNotNull,
    ColumnValuesToBeUnique,
    ColumnValuesToBeBetween,
)
```

## Test Categories

- **Table-Level Tests** (9): Validate properties of entire tables — row counts, column counts, schema, custom SQL, and table comparisons.
- **Column-Level Tests** (16): Validate properties of specific columns — nulls, uniqueness, set membership, regex patterns, numeric ranges, statistical measures, string lengths, and positional values.

## Customization

All tests support fluent method chaining:

```python
test = ColumnValuesToBeNotNull(column="email") \
    .with_name("email_completeness_check") \
    .with_display_name("Email Completeness Validation") \
    .with_description("Ensures all customer records have email addresses") \
    .with_compute_row_count(True)
```

Or constructor parameters:

```python
test = ColumnValuesToBeNotNull(
    column="email",
    name="email_completeness_check",
    display_name="Email Completeness Validation",
    description="Ensures all customer records have email addresses"
)
```

## Related

- [[data-quality]] — The concept page for data quality in OpenMetadata
- [[test-runner]] — Next step: how to execute these tests
- [[dataframe-validation]] — Next step: applying tests to DataFrames