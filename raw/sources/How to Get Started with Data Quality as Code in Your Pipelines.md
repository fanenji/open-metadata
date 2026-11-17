---
title: "How to Get Started with Data Quality as Code in Your Pipelines"
source: "https://blog.open-metadata.org/how-to-get-started-with-data-quality-as-code-in-your-pipelines-122af5b93d7f"
author:
  - "[[Eugenio Doñaque]]"
published: 2026-01-20
created: 2026-06-29
description: "How to Get Started with Data Quality as Code in Your Pipelines Implementation introduction and advantages of OpenMetadata’s approach In Part 1, we explored why traditional data quality testing …"
tags:
  - "clippings"
topic:
type: "note"
---
## Implementation introduction and advantages of OpenMetadata’s approach

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OdZW9J4-YscWswrUtptxkw.png)

Data Quality as Code Implementation

In [Part 1](https://blog.open-metadata.org/introducing-data-quality-as-code-validate-data-before-it-lands-not-after-70867330b373), we explored why traditional data quality testing happens too late — after bad data has already reached production. Data Quality as Code shifts validation left, letting you catch issues during transformation before they propagate downstream. In Part 2, we’ll walk you through implementing Data Quality as Code in your pipelines. Let’s start with a concrete example of how this works in practice.

## How To Implement Data Quality as Code

Let’s walk through a scenario where a data engineer maintains a pipeline that processes customer data.

Previously, the pipeline followed the standard pattern:

1. Extract data from operational systems
2. Transform: clean, enrich, and aggregate
3. Load into the destination table
4. OpenMetadata runs scheduled quality tests
5. If tests fail, alert the team (but data is already in production)

With Data Quality as Code, the engineer refactors the pipeline:

```rb
# Extract
df = extract_from_source()

# Transform
df = transform_data(df)

# Validate
validator = DataFrameValidator()
validator.add_openmetadata_table_tests("Warehouse.staging.user_data")

result = validator.validate(df)

# Load only if validation passes
if result.success:
    load_to_warehouse(df)
else:
    alert_team(result.failures)

# Publish results to OpenMetadata
result.publish("Warehouse.staging.user_data")
```

When the pipeline runs, several things happen automatically:

1. **Test definitions load from multiple sources**: Tests can come from inline code, from the OpenMetadata UI, or from YAML configuration files
2. **Validation executes against the DataFrame**: All tests run against the in-memory data before it touches the warehouse
3. **Circuit breaker logic activates**: If critical tests fail, the pipeline stops before writing bad data
4. **Results are published to OpenMetadata**: Pass/fail outcomes, error details, and affected rows surface in the OpenMetadata UI alongside existing observability features
5. **Alerts fire automatically**: OpenMetadata’s incident management notifies stakeholders based on configured rules

## Quick Start

### Requirements

- Python 3.10 or higher
- `openmetadata-ingestion` package version 1.11.0.0 or later
- Access to an OpenMetadata instance (1.11.0 or later)
- Valid JWT token for authentication

### Installation

```rb
# Install the SDK
pip install "openmetadata-ingestion>=1.11.0.0"
```

### Running Data Quality tests

```rb
# Set up authentication
from metadata.sdk import configure

configure(
    host="http://localhost:8585/api",  # Your OpenMetadata API URL
    jwt_token="your-jwt-token-here"
)

from metadata.sdk.data_quality import TestRunner, TableRowCountToBeBetween

# Create a test runner for a specific table
runner = TestRunner.for_table("MySQL.ecommerce.public.customers")

# Add a test to verify row count is within expected range
runner.add_test(
    TableRowCountToBeBetween(min_count=1000, max_count=100000)
)

# Run the tests
results = runner.run()

# Print results
for result in results:
    test_case = result.testCase
    test_result = result.testCaseResult
    print(f"Test: {test_case.name.root}")
    print(f"Status: {test_result.testCaseStatus}")
    print(f"Result: {test_result.result}")
```

⚠️ Security Note: Never hardcode JWT tokens in production. Use environment variables or secure credential management:

```rb
import os

jwt_token = os.getenv("OPENMETADATA_JWT_TOKEN")
```

## Why OpenMetadata’s Data Quality as Code Is Different

Several tools offer programmatic data validation, most notably Great Expectations. Here’s what sets OpenMetadata apart:

### Complete Workflow Integration, Not Just Tests

Great Expectations offers more individual test types. OpenMetadata’s initial release focuses on the most commonly used validations. We plan to expand this library based on community needs.

Where Data Quality as Code stands apart is in the *completeness of the solution*:

- **Circuit Breaker Control**: OpenMetadata provides first-class support for halting pipelines, rolling back transactions, and filtering bad records based on test results. This isn’t an add-on — it’s built into the SDK’s validation patterns.
- **Unified Metadata Integration**: Tests don’t live in isolation. They integrate with OpenMetadata’s unified knowledge graph, automatically linking to data lineage, ownership, glossary terms, and usage patterns. When a test fails, you see not just the error, but also which dashboards and models depend on that data, who owns it, and what it means.
- **Incident Management**: OpenMetadata includes native incident tracking and resolution workflows. When quality tests fail, incidents can automatically surface with context about the data asset. Great Expectations does not have incident management capabilities.
- **End-to-End Observability**: Test results flow into the same platform that tracks schema changes, data freshness, and usage analytics. You get a complete picture of data health, not just quality test outcomes in isolation.
- **UI-Driven Test Creation**: Data stewards and business users can continue to define quality tests through the OpenMetadata UI without writing code. Both code-defined and UI-defined quality tests will appear in OpenMetadata’s UI data quality dashboards and reporting.

### Collaborative Quality Management

Perhaps the most distinctive aspect of Data Quality as Code is how it enables collaboration between different roles:

- **Data stewards** define business quality rules in the OpenMetadata UI based on their domain knowledge
- **Data engineers** execute those rules (plus structural checks) in production pipelines
- **Data consumers** see test results and incident alerts without needing to understand pipeline code
- **Platform teams** govern standards through OpenMetadata’s policies

This collaborative model means quality ownership is shared rather than siloed within engineering teams. Business logic lives with business experts, validation execution lives with engineers, and visibility extends to everyone who needs it.

### Enterprise-Grade Integration

Data Quality as Code inherits all the enterprise capabilities of OpenMetadata’s platform:

**Security and Governance**: Authentication and authorization use the same role-based access controls that govern the OpenMetadata UI and API. Test execution respects data access policies, ensuring users can only validate data they’re permitted to see.

**Service Connection Reuse**: The SDK automatically uses database credentials and connection configurations already stored in OpenMetadata. No need to manage separate authentication for test execution — it leverages your existing secure credential management.

**Unified Visibility**: Test results from code-based execution appear in the OpenMetadata UI alongside UI-created tests, profiling metrics, and observability signals. One platform shows the complete picture of data health.

**Flexible Architecture:** Works with both ETL and ELT patterns. For ETL, validate transformations before loading to the warehouse. If tests fail during transformation, prevent the load entirely. For ELT, validate during the transformation layer. Raw data is loaded into a staging area, transformations run within the warehouse, and quality tests gate promotion from staging to production tables.

### Shift Left on Data Quality

Data quality is too important to treat as an afterthought. By the time traditional validation catches errors, the damage is done, bad data has reached dashboards, influenced decisions, and eroded trust. Data Quality as Code shifts validation left in your pipelines, letting you catch issues during transformation, before they propagate downstream. This isn’t just a developer convenience; it’s a fundamental rethinking of when and how quality checks should run.

Combined with Collate’s unified metadata platform, you get the best of both worlds: programmatic control for engineers who build pipelines, and collaborative governance for stewards who define business rules. Test results surface in one place, incidents track automatically, and everyone, technical and non-technical, can see the health of your data.

Whether you’re building new pipelines or refactoring existing ones, Data Quality as Code gives you the tools to ensure only clean, validated data reaches production. Test early, fail fast, and keep your data trustworthy from source to insight.

## Get Started Today

Data Quality as Code is available now as part of OpenMetadata and Collate’s managed OpenMetadata service as part of Release 1.11.

Check out our [complete tutorials](https://github.com/open-metadata/OpenMetadata/tree/main/examples/python-sdk/data-quality) using Jupyter Notebooks. You will run through two typical scenarios where running your OpenMetadata tests in your ETLs will help you ensure your data meets your quality standards by reducing the time to discover issues.

[Sign up for Collate’s free tier](https://www.getcollate.io/welcome), explore our [sandbox with demo data](https://sandbox.open-metadata.org/), or dive into the [documentation](https://docs.open-metadata.org/latest/how-to-guides/data-quality-observability/quality/data-quality-as-code) to integrate Data Quality as Code into your pipelines today.