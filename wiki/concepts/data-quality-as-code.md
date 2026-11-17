---
sources: []
tags: []
related: []
updated: 2026-07-07
---
# Data Quality as Code

A programmatic approach to data validation that **shifts quality checks left** in the data pipeline — executing tests during transformation, before data reaches production. Introduced in OpenMetadata 1.11, Data Quality as Code complements the existing [[data-quality]] UI with an SDK-driven, pipeline-embedded testing model.

## The Problem with Traditional Data Quality

Traditional data quality testing follows a **test-after** pattern:

1. Extract data from operational systems
2. Transform: clean, enrich, aggregate
3. Load into the destination table
4. OpenMetadata runs scheduled quality tests
5. If tests fail, alert the team — **but data is already in production**

By the time validation catches errors, bad data has already reached dashboards, influenced decisions, and eroded trust.

## The Data Quality as Code Pattern

With Data Quality as Code, validation is **shifted left** into the transformation layer:

1. Extract data
2. Transform
3. **Validate** — run quality tests against the in-memory DataFrame
4. **Load only if validation passes** (circuit breaker)
5. Publish results to OpenMetadata

This uses a **circuit breaker pattern**: if critical tests fail, the pipeline stops before writing bad data. Results (pass/fail, error details, affected rows) are published to OpenMetadata and surface in the UI alongside existing observability features.

## Core SDK Components

### DataFrameValidator
Validates a DataFrame against tests defined in OpenMetadata for a specific table:

```python
validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Warehouse.staging.user_data")
result = validator.validate(df)
if result.success:
    load_to_warehouse(df)
else:
    alert_team(result.failures)
result.publish("Warehouse.staging.user_data")
```

### TestRunner
Programmatic test execution for specific tables:

```python
from metadata.sdk.data_quality import TestRunner, TableRowCountToBeBetween

runner = TestRunner.for_table("MySQL.ecommerce.public.customers")
runner.add_test(TableRowCountToBeBetween(min_count=1000, max_count=100000))
results = runner.run()
```

### Authentication Setup

```python
from metadata.sdk import configure
configure(
    host="http://localhost:8585/api",
    jwt_token="your-jwt-token-here"
)
```

> **Security**: Never hardcode JWT tokens. Use environment variables or secure credential management.

## Requirements

- Python 3.10+
- `openmetadata-ingestion` package ≥ 1.11.0.0
- OpenMetadata instance ≥ 1.11
- Valid JWT token for authentication

## How It Differs from Great Expectations

While [[great-expectations]] offers more individual test types, OpenMetadata differentiates through the **completeness of the solution**:

| Aspect | OpenMetadata | Great Expectations |
|--------|-------------|-------------------|
| Circuit breaker | Built-in SDK patterns | Add-on |
| Metadata integration | Unified knowledge graph (lineage, ownership, glossary) | Isolated |
| Incident management | Native tracking and resolution | Not available |
| End-to-end observability | Schema changes, freshness, usage in one platform | Tests only |
| UI-driven creation | Business users via UI, engineers via SDK | Primarily code-driven |

## Collaborative Quality Management

Data Quality as Code enables a **shared ownership model** across roles:

- **Data stewards** — Define business quality rules in the OpenMetadata UI
- **Data engineers** — Execute rules (plus structural checks) in production pipelines via SDK
- **Data consumers** — See test results and incident alerts without pipeline code access
- **Platform teams** — Govern standards through OpenMetadata's policies and RBAC

## Enterprise Integration

- **Security**: Inherits OpenMetadata's [[hybrid-rbac-abac-model]] — test execution respects data access policies
- **Service Connection Reuse**: Uses database credentials already stored in OpenMetadata, no separate authentication management
- **Flexible Architecture**: Works with both ETL (validate before loading) and ELT (validate during transformation, gate staging→production promotion)
- **Unified Visibility**: Test results appear in the UI alongside UI-created tests, profiling metrics, and observability signals

## Relationship to Existing Concepts

- **[[data-quality]]** — Data Quality as Code extends the existing quality framework with programmatic, pipeline-embedded testing
- **[[data-observability-alerts]]** — Test failures trigger the alerting/incident infrastructure
- **[[unified-metadata-graph]]** — Tests link to lineage, ownership, glossary terms, and usage patterns
- **[[ingestion-framework]]** — SDK reuses existing service connections and credentials
- **[[metadata-cli]]** — Complementary to CLI-based ingestion; SDK is for pipeline-embedded testing

## Version

Available from **OpenMetadata 1.11** (January 2026) and Collate's managed service.