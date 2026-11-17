---
sources: [sources.md, Announcing OpenMetadata 1.12 1.md]
tags: [openmetadata, data-quality, data-governance, testing, profiling]
related: [openmetadata, data-profiling, ingestion-framework, test-library, test-definition, test-case, test-suite, test-runner, data-quality-as-code, data-contracts, data-observability-alerts, incident-manager]
type: concept
title: Data Quality
created: 2024-05-24
updated: 2026-07-07
---
# Data Quality

Data quality in OpenMetadata refers to the ability to define and run tests on data to ensure its reliability and trustworthiness. It encompasses the tools, workflows, and frameworks for measuring, monitoring, and enforcing data quality standards across the organization.

## Purpose

Data quality tests help organizations maintain high standards for their data, detect anomalies, and prevent issues from propagating downstream. Tests are defined and executed by the [[ingestion-framework|Ingestion Framework]], and results are displayed in the [[openmetadata|OpenMetadata]] UI alongside the data assets.

## Quality Approaches

OpenMetadata supports three complementary approaches to data quality:

1. **UI-Driven Tests**: Create and run tests through the graphical interface — table-level, column-level, and custom SQL tests
2. **[[data-quality-as-code|Data Quality as Code]]** (v1.11): SDK-driven, pipeline-embedded testing with circuit breaker patterns — quality enforced in CI/CD
3. **[[data-contracts|Data Contracts]]** (v1.9): Formal producer-consumer agreements with quality SLAs

## Data Quality Test Library (v1.12)

The **[[test-library|Data Quality Test Library]]**, introduced in 1.12, transforms how organizations standardize quality testing:

- **Reusable templates**: Administrators define parameterized SQL-based test templates once
- **GUI-driven**: Users apply templates through a no-code interface — fill in parameters, no SQL required
- **Centralized governance**: Admins control which tests are available organization-wide
- **Superior to dbt generic tests**: Unlike dbt's YAML-based approach requiring technical expertise, the Test Library provides a visual interface for defining and applying tests

### Example

An administrator creates an "ARR validation" test template with a threshold parameter. Data stewards apply it to any table by filling in the threshold value — no SQL rewriting needed.

## Test Components

| Component | Description |
|-----------|-------------|
| [[test-definition]] | Reusable test logic (SQL query or metric assertion) |
| [[test-case]] | Instance of a test definition applied to a specific asset |
| [[test-suite]] | Collection of test cases for organized execution |
| [[test-runner]] | Execution engine that runs tests and produces [[test-case-result|results]] |

## Quality Workflows

- [[incident-manager|Incident Manager]]: Track and resolve quality failures
- [[data-observability-alerts|Alerts & Notifications]]: Real-time quality monitoring
- [[data-profiling|Data Profiling]]: Automated column statistics and pattern detection

## See Also

- [[test-library]] — Test Library feature details
- [[data-quality-as-code]] — SDK-driven quality in pipelines
- [[data-contracts]] — Formal producer-consumer quality agreements
- [[publishing-quality-results]] — Best practices for publishing results
