---
type: concept
title: Publishing Quality Results
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, publishing, results, openmetadata, sdk]
related: [data-quality, data-quality-as-code, test-runner, dataframe-validator, data-observability-alerts]
sources: ["publishing-results-best-practices---openmetadata-d-20260514.md"]
---

# Publishing Quality Results

Publishing quality results is the process of sending data validation outcomes from external or programmatic test execution back to OpenMetadata. This enables centralized observability, historical tracking, alerting, and compliance auditing.

## How It Works

After running tests using [[TestRunner]] or [[DataFrameValidator]], the results object exposes a `publish()` method that sends the validation outcomes to OpenMetadata. The method accepts the table Fully Qualified Name (FQN) as a parameter.

```python
from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Postgres.staging.public.customers")
result = validator.validate(df)
result.publish("Postgres.staging.public.customers")
```

## Benefits

- **Historical tracking**: View trends over time for test results
- **Alerting**: Trigger notifications on failures via [[data-observability-alerts]]
- **Dashboards**: Centralized data quality monitoring in OpenMetadata
- **Collaboration**: Share results across teams
- **Compliance**: Maintain audit trails of data quality over time

## Integration with Alerts and Dashboards

Published results feed into OpenMetadata's alerting system, enabling notifications on test failures. They also populate data quality dashboards, providing a centralized view of data estate health. This makes publishing a critical step for operationalizing data quality.

## Best Practices

- Always publish results after validation to enable tracking
- Combine publishing with [[dynamic-test-generation]] for automated, schema-responsive quality checks
- Use [[multi-table-validation]] patterns to publish aggregated summaries for pipeline-level quality gates
- Implement [[data-quality-as-code|error handling with retries]] to ensure results are published even after transient failures