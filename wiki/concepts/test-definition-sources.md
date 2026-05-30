---
type: concept
title: Test Definition Sources
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, python, testing, configuration]
related: [data-quality-as-code, testrunner-api, dataframe-validation, data-quality]
sources: ["data-quality-as-code---openmetadata-documentation-20260514.md"]
---
# Test Definition Sources

Test Definition Sources refers to the three flexible ways to define data quality tests when using the OpenMetadata Python SDK: inline code, loading from the OpenMetadata UI, and importing from YAML files.

## Inline Code

Define tests directly in Python code using the SDK's test classes:

```python
from metadata.sdk.data_quality import TableRowCountToBeBetween
runner.add_test(TableRowCountToBeBetween(min_count=100, max_count=1000))
```

**Advantages**: Full programmatic control, dynamic test generation, version-controlled alongside code.

## From OpenMetadata UI

Load test definitions that were configured by data stewards in the OpenMetadata UI:

```python
runner = TestRunner.for_table("BigQuery.analytics.customer_360")
results = runner.run()  # Runs all tests defined in UI
```

**Advantages**: Enables collaborative workflow where domain experts define quality rules without writing code.

## From YAML Files

Load test configurations from YAML workflow files:

```python
# Load tests from YAML configuration
runner.load_tests_from_yaml("tests_config.yaml")
```

**Advantages**: Declarative configuration, reusable across pipelines, version-controllable.

## Comparison

| Source | Version Control | Requires Code | Best For |
|--------|----------------|---------------|----------|
| Inline Code | Yes | Yes | Dynamic tests, programmatic generation |
| OpenMetadata UI | No (open question) | No | Domain experts, collaborative definition |
| YAML Files | Yes | Minimal | Declarative, reusable configurations |

## Related Concepts

- [[data-quality-as-code]] — The overarching programmatic approach.
- [[testrunner-api]] — Table-targeted test execution.
- [[dataframe-validation]] — DataFrame validation.
- [[data-quality]] — Core data quality concept.