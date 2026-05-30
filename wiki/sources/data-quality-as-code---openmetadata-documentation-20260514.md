---
type: source
title: Data Quality as Code - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, python, testing, documentation]
related: [data-quality-as-code, testrunner-api, dataframe-validation, test-definition-sources, data-quality, ingestion-framework, personal-access-token, data-observability-alerts]
sources: ["data-quality-as-code---openmetadata-documentation-20260514.md"]
---
# Data Quality as Code - OpenMetadata Documentation

Official OpenMetadata documentation (v1.12.x) introducing the Data Quality as Code approach, which enables programmatic building, running, and management of data quality tests within ETL workflows using the OpenMetadata Python SDK.

## Key Topics

- **TestRunner API**: Execute data quality tests against tables cataloged in OpenMetadata and publish results back.
- **DataFrame Validation**: Validate pandas DataFrames before loading to destinations, with chunk-based validation for large datasets.
- **Multiple Test Definition Sources**: Define tests inline, load from OpenMetadata UI, or import from YAML files.
- **Collaborative Quality Management**: Data stewards define tests in the UI, engineers execute them in code pipelines.
- **Comprehensive Test Library**: Access all table and column test types supported by OpenMetadata.

## Requirements

- Python 3.10+
- `openmetadata-ingestion` package v1.11.0.0+
- OpenMetadata instance v1.11.0+
- Valid JWT token for authentication

## Architecture

The SDK integrates with OpenMetadata's existing data quality infrastructure: test definitions, execution engine, result publishing, and service connections.

## Related Pages

- [[data-quality-as-code]] — Main concept page
- [[testrunner-api]] — TestRunner API reference
- [[dataframe-validation]] — DataFrame validation reference
- [[test-definition-sources]] — Test definition sources comparison
- [[data-quality]] — Core data quality concept
- [[ingestion-framework]] — Metadata ingestion framework
- [[personal-access-token]] — JWT token authentication
- [[data-observability-alerts]] — Alerting on test results