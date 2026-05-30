---
type: concept
title: DataFrame Validation
created: 2026-05-14
updated: 2026-05-15
tags: [data-quality, sdk, python, pandas, validation, dataframe]
related: [data-quality-as-code, testrunner-api, test-definition-sources, data-quality, test-runner, metadata-sdk-data-quality]
sources: ["data-quality-as-code---openmetadata-documentation-20260514.md", "test-definitions-reference---openmetadata-document-20260514.md"]
---
# DataFrame Validation

DataFrame Validation is a feature of the OpenMetadata Python SDK that enables applying data quality test definitions directly to in-memory DataFrames (e.g., pandas DataFrames). It provides immediate feedback on data quality issues during ETL processing and before loading data to destinations.

This capability extends the [[test-runner]] concept by allowing tests to be executed against DataFrames rather than against database tables, making it ideal for pipeline, notebook, and pre‑load validation scenarios.

## Use Cases

- Validating data during ETL/ELT processing
- Testing data transformations before materialization
- Running quality checks in notebook environments
- Pre-load validation in data pipelines

## Usage

The SDK provides two complementary ways to validate DataFrames: a dedicated `DataFrameValidator` and direct integration via the `TestRunner`.

### Using DataFrameValidator

```python
import pandas as pd
from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator
from metadata.sdk.data_quality import ColumnValuesToBeNotNull

df = pd.read_csv('path/to/data.csv')
validator = DataFrameValidator()
validator.add_test(ColumnValuesToBeNotNull(column="email"))
result = validator.validate(df)

if result.success:
    load_to_destination(df)
result.publish("MySQL.default.db.table")  # publishes results to OpenMetadata
```

### Using TestRunner

```python
from metadata.sdk.data_quality import ColumnValuesToBeNotNull
from metadata.sdk.data_quality import TestRunner
import pandas as pd

df = pd.DataFrame({"email": ["a@b.com", None, "c@d.com"]})
test = ColumnValuesToBeNotNull(column="email")
runner = TestRunner()
result = runner.run(test, dataframe=df)
```

The `TestRunner` approach offers the same flexibility as the `DataFrameValidator` and can be combined with result publishing and chunk processing as needed.

## Chunk-Based Validation

For large datasets that do not fit into memory, DataFrame validation supports chunk-based processing with success/failure callbacks:

```python
validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Postgres.warehouse.transactions")
result = validator.run(
    pd.read_csv('large_file.csv', chunksize=10000),
    on_success=load_chunk,
    on_failure=rollback_transaction
)
```

## Key Features

- **Pre‑load validation**: Validate data before loading to destinations.
- **Result publishing**: Publish validation results back to OpenMetadata.
- **Chunk‑based processing**: Handle large datasets with configurable chunk sizes.
- **Callback support**: Define custom success and failure handlers for each chunk.
- **Integration with UI‑defined tests**: Load test definitions from OpenMetadata.

## Related Concepts

- [[data-quality-as-code]] — The overarching programmatic approach.
- [[testrunner-api]] — Table‑targeted test execution.
- [[test-definition-sources]] — How tests can be defined.
- [[data-quality]] — Core data quality concept.
- [[test-runner]] — The execution component for data quality tests.
- [[metadata-sdk-data-quality]] — The module providing test definitions.