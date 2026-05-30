---
type: source
title: "Publishing Results & Best Practices - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, data-quality-as-code, publishing, best-practices, openmetadata]
related: [data-quality, data-quality-as-code, publishing-quality-results, dynamic-test-generation, multi-table-validation, test-runner, dataframe-validator]
sources: ["publishing-results-best-practices---openmetadata-d-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/publishing-and-best-practices"
venue: OpenMetadata Documentation
---

# Publishing Results & Best Practices - OpenMetadata Documentation

This source document covers the "Publishing Results & Best Practices" section of the OpenMetadata v1.12.x documentation, part of the Data Quality as Code guide. It provides code examples and guidance for publishing validation results back to OpenMetadata, implementing error handling with retries, generating tests dynamically from table metadata, and running multi-table validation workflows. The document emphasizes the benefits of publishing results for historical tracking, alerting, dashboards, collaboration, and compliance. It also includes a best practices summary covering version control, environment variables, retries, incremental validation, and separation of concerns between data stewards and engineers.

Key code examples include:
- [[DataFrameValidator]] for validating pandas DataFrames and publishing results
- [[TestRunner]] for running tests against a table FQN with retry logic
- Dynamic test generation using column constraints (NOT NULL, PRIMARY KEY)
- Multi-table validation with aggregated summary reporting
- Error handling patterns distinguishing retryable (ConnectionError) from non-retryable (ValueError) errors