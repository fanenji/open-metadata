---
type: concept
title: TestRunner API
created: 2026-05-14
updated: 2026-05-15
tags: [data-quality, sdk, python, testing, api]
related: [data-quality-as-code, dataframe-validation, test-definition-sources, data-quality, openmetadata-python-sdk]
sources: ["data-quality-as-code---openmetadata-documentation-20260514.md", "getting-started-with-data-quality-as-code---openme-20260514.md"]
---
# TestRunner API

The **TestRunner API** is the primary programmatic interface in the OpenMetadata Python SDK for executing data quality tests against tables cataloged in OpenMetadata. It is part of the `metadata.sdk.data_quality` module and publishes results back to OpenMetadata for visualization, alerting, and governance.

## Basic Usage

```python
from metadata.sdk import configure
from metadata.sdk.data_quality import TestRunner, TableRowCountToBeBetween

# Configure the SDK (required before using the TestRunner)
configure(host="http://localhost:8585/api", jwt_token="your-token")

# Create a runner for a specific table using its fully qualified name
runner = TestRunner.for_table("MySQL.ecommerce.public.customers")

# Add a test definition
runner.add_test(TableRowCountToBeBetween(min_count=1000, max_count=100000))

# Execute all tests and inspect results
results = runner.run()

for result in results:
    print(f"Test: {result.testCase.name.root}")
    print(f"Status: {result.testCaseResult.testCaseStatus}")
    print(f"Result: {result.testCaseResult.result}")
```

## Core Methods

### `TestRunner.for_table(fqn: str)`
Factory method that creates a `TestRunner` instance for a specific table identified by its fully qualified name (FQN) in the format `service.database.schema.table`. This is the entry point for all table-level data quality tests.

### `runner.add_test(test_definition)`
Adds a test definition to the runner. Test definitions are instances of test classes provided by the SDK, such as `TableRowCountToBeBetween(min_count=..., max_count=...)` or other table/column test types.

### `runner.run()`
Executes all added tests and returns a list of result objects. Each result contains:
- `testCase` (with a `name.root` property)
- `testCaseResult` (with `testCaseStatus` and `result` properties)

Results are automatically published to OpenMetadata for centralized monitoring.

## Key Features

- **Table‑targeted execution**: Run tests against any table cataloged in OpenMetadata.
- **Result publishing**: Test results are automatically published back to OpenMetadata for visualization, alerting, and governance.
- **Integration with UI‑defined tests**: Load and execute tests defined by data stewards in the OpenMetadata UI, enabling a collaborative workflow.
- **Comprehensive test library**: Access all table and column test types supported by OpenMetadata.
- **Programmatic counterpart**: The TestRunner API enables the **data‑quality‑as‑code** workflow (see [[data-quality-as-code]]), allowing tests to be defined, version‑controlled, and executed in automated pipelines.

## Requirements

- The SDK must be configured via `configure()` before using the `TestRunner` (e.g., providing host URL and JWT token).
- The fully qualified table name must match the OpenMetadata service hierarchy (`service.database.schema.table`).
- The target table must already be ingested into OpenMetadata.

## Collaborative Workflow

Data stewards can define tests in the OpenMetadata UI, and engineers can execute those tests in their pipelines without duplicating definitions:

```python
runner = TestRunner.for_table("BigQuery.analytics.customer_360")
results = runner.run()  # Runs all tests defined in the UI for that table
```

## Related Concepts

- [[data-quality-as-code]] — The overarching programmatic approach.
- [[dataframe-validation]] — DataFrame validation for pre‑load testing.
- [[test-definition-sources]] — How tests can be defined (inline, UI, YAML).
- [[data-quality]] — Core data quality concept.
- [[openmetadata-python-sdk]] — The SDK that encompasses the TestRunner API.