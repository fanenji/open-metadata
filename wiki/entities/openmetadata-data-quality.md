---
type: entity
title: OpenMetadata Data Quality
created: 2026-04-08
updated: 2026-04-08
tags: [openmetadata, data-quality, observability]
related: [openmetadata, data-quality-resolution-workflow, data-observability-definition, data-catalog-tool-comparison, great-expectations-for-data-contracts]
sources: ["Data Quality  OpenMetadata Quality Management Guide.md"]
---
# OpenMetadata Data Quality

OpenMetadata provides a comprehensive, no-code data quality platform integrated directly into its metadata catalog. It enables users to define, run, and monitor data quality tests without writing code, covering all supported database connectors.

## Core Capabilities

### Native Tests
OpenMetadata includes built-in assertions for table-level and column-level validation. These tests are available for all database connectors and cover common quality dimensions such as completeness, freshness, accuracy, and uniqueness. Tests are configured through the OpenMetadata UI or API, requiring no external testing framework.

### Alerting System
When a test fails, OpenMetadata can send notifications via its alerting system. Alerts can be configured to notify data producers, consumers, or governance teams, enabling real-time response to quality issues.

### Health Dashboard
A real-time dashboard displays test failure rates and trends, allowing teams to prioritize remediation efforts. The dashboard provides visibility into the overall health of data assets across the organization.

### Resolution Workflow
OpenMetadata includes a workflow to inform data consumers when a test failure has been resolved. This closes the feedback loop, ensuring that downstream consumers are aware of data quality improvements and can trust the data again.

### Extensibility
The platform claims extensibility, allowing organizations to adapt data quality checks to custom needs. However, concrete examples of extending beyond native tests are not provided in the source documentation.

## Relationship to Other Tools

OpenMetadata's data quality module competes with dedicated quality tools like [[great-expectations-for-data-contracts]] and [[dbt-expectations]]. Its key differentiator is tight integration with the metadata catalog, enabling quality signals to be surfaced alongside lineage, ownership, and governance information. This contrasts with standalone quality tools that require separate setup and context switching.

## Open Questions

- How does OpenMetadata's quality module compare to Great Expectations in practice for complex validation scenarios?
- What is the performance impact of running the profiler and tests at scale on large datasets?
- Are resolution workflows automated or do they require manual intervention?