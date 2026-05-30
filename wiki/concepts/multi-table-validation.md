---
type: concept
title: Multi-Table Validation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, testing, validation, workflow, openmetadata]
related: [data-quality, data-quality-as-code, test-runner, publishing-quality-results]
sources: ["publishing-results-best-practices---openmetadata-d-20260514.md"]
---

# Multi-Table Validation

Multi-table validation is a workflow pattern in OpenMetadata where data quality tests are executed across multiple tables in a single programmatic run, with aggregated summary reporting. This enables pipeline-level quality gates and comprehensive data estate health checks.

## How It Works

A dictionary of tables and their validation configurations is defined. A [[TestRunner]] is instantiated for each table, tests are added based on the configuration, and results are collected into a summary:

```python
from metadata.sdk.data_quality import TestRunner, TableRowCountToBeBetween

tables_to_validate = {
    "Postgres.warehouse.public.customers": {"min_rows": 10000},
    "Postgres.warehouse.public.orders": {"min_rows": 50000},
    "Postgres.warehouse.public.products": {"min_rows": 1000}
}

validation_results = {}
for table_fqn, config in tables_to_validate.items():
    runner = TestRunner.for_table(table_fqn)
    runner.add_test(TableRowCountToBeBetween(min_count=config["min_rows"]))
    results = runner.run()
    validation_results[table_fqn] = {
        "passed": all(r.testCaseResult.testCaseStatus == "Success" for r in results),
        "details": results
    }

total_tables = len(validation_results)
passed_tables = sum(1 for v in validation_results.values() if v["passed"])
print(f"Validation Summary: {passed_tables}/{total_tables} tables passed")
```

## Benefits

- **Pipeline-level quality gates**: Validate all tables in a data pipeline before promoting data
- **Aggregated reporting**: Single summary of data estate health
- **Consistent test application**: Apply the same test pattern across multiple tables
- **Integration with publishing**: Results can be published back to OpenMetadata for centralized tracking

## Best Practices

- Define validation thresholds per table based on business requirements
- Combine with [[dynamic-test-generation]] for schema-responsive multi-table validation
- Publish results using [[publishing-quality-results]] for historical tracking and alerting
- Handle partial failures gracefully — report which tables passed and which failed
- Use the aggregated summary to trigger downstream pipeline decisions