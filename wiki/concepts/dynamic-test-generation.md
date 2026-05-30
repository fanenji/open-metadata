---
type: concept
title: Dynamic Test Generation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, testing, automation, metadata, openmetadata]
related: [data-quality, data-quality-as-code, test-runner, data-profiling, publishing-quality-results]
sources: ["publishing-results-best-practices---openmetadata-d-20260514.md"]
---

# Dynamic Test Generation

Dynamic test generation is the practice of programmatically creating data quality tests based on table metadata — such as column constraints, data types, and primary keys — rather than manually defining tests in static YAML configuration files. This approach ensures test coverage automatically adapts to schema changes.

## How It Works

Using the OpenMetadata Python SDK, a [[TestRunner]] is instantiated for a table. The table's metadata is fetched via the OpenMetadata client, and tests are added based on column properties:

```python
from metadata.sdk import configure, client
from metadata.sdk.data_quality import (
    TestRunner,
    ColumnValuesToBeNotNull,
    ColumnValuesToBeUnique
)

configure(host="http://localhost:8585/api", jwt_token="token")
om_client = client()
table = om_client.ometa.get_by_name(
    entity=Table,
    fqn="Postgres.warehouse.public.customers"
)

runner = TestRunner.for_table(table.fullyQualifiedName.root)
for column in table.columns:
    if column.constraint == "NOT NULL":
        runner.add_test(ColumnValuesToBeNotNull(column=column.name.root))
    if column.constraint == "PRIMARY KEY":
        runner.add_test(ColumnValuesToBeUnique(column=column.name.root))

results = runner.run()
```

## When to Use Dynamic Generation

- **Rapidly evolving schemas**: Tests automatically adjust when columns are added, removed, or modified
- **Large schemas**: Reduces manual effort of writing tests for hundreds of columns
- **Automated pipelines**: Integrates with CI/CD for schema-responsive quality gates

## Relationship to Static YAML Configuration

Dynamic generation complements the YAML-based approach. YAML configs are version-controlled and audit-friendly, making them suitable for stable, well-understood schemas. Dynamic generation is schema-responsive and automated, ideal for dynamic environments. Both can be combined: use YAML for core business rules and dynamic generation for schema-derived constraints.

## Connection to Data Profiling

Dynamic test generation leverages metadata from [[data-profiling]] — specifically column constraints and types — to drive test creation. This creates a feedback loop where profiling informs quality testing, and published results inform future profiling and monitoring.