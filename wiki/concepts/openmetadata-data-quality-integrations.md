---
type: concept
title: OpenMetadata Data Quality Integrations
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, data-quality, great-expectations, dbt, deequ, soda, integrations]
related: [openmetadata, openmetadata-standards-overview, openmetadata-data-quality, great-expectations-for-data-contracts, dbt-testing-patterns, data-quality-dimensions]
sources: ["openmetadata-standards-overview.md"]
---
# OpenMetadata Data Quality Integrations

OpenMetadata's Data Quality domain provides a unified framework for defining, executing, and tracking quality tests across data assets. The specification integrates with multiple data quality tools:

- **OpenMetadata Native Tests**: Built-in quality tests for all database connectors
- **Great Expectations**: Integration via the Great Expectations connector, enabling Expectation Suites to be managed within OpenMetadata
- **dbt**: Integration with dbt test results, allowing dbt's singular and generic tests to be surfaced in OpenMetadata's quality dashboard
- **Deequ**: Integration with Amazon's Deequ library for automated quality constraint suggestion on Spark DataFrames
- **Soda**: Integration with Soda Core for SQL-based quality checks

The specification supports quality tests, validation execution, data profiling (statistical analysis of data content and structure), and quality metrics over time (historical tracking of DQ test results for trend analysis and observability).

This concept extends the wiki's existing [[openmetadata-data-quality]] page by providing the broader integration context, and connects to [[great-expectations-for-data-contracts]] and [[dbt-testing-patterns]] by showing how these tools interoperate within the OpenMetadata ecosystem. It also strengthens [[data-quality-dimensions]] by adding profiling and temporal metrics as additional dimensions.