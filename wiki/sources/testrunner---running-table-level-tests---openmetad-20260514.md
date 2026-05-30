---
type: source
title: "Testrunner   Running Table Level Tests   Openmetad 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "TestRunner - Running Table-Level Tests - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, test-runner, python]
related: [test-runner, data-quality-as-code, data-quality, sdk-configuration, external-secrets-manager-setup, test-definitions-reference]
sources: ["testrunner---running-table-level-tests---openmetad-20260514.md"]
---

# TestRunner - Running Table-Level Tests - OpenMetadata Documentation

**Source:** https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/test-runner

This official OpenMetadata v1.12.x documentation page introduces the `TestRunner` class, a fluent API for executing data quality tests against tables cataloged in OpenMetadata. It covers basic usage, running tests defined in the UI, customizing test metadata, configuring row count computation, integration with ETL workflows, error handling, best practices, and external secrets manager setup.

Key topics include:
- Creating a `TestRunner` via `TestRunner.for_table(fqn)` using the fully qualified name format `{service}.{database}.{schema}.{table}`
- Adding table-level and column-level tests using built-in test definition classes (e.g., `TableRowCountToBeBetween`, `ColumnValuesToBeNotNull`)
- Running tests previously configured in the OpenMetadata UI for a collaborative steward-engineer workflow
- Customizing test names, display names, and descriptions via a fluent API
- Configuring row count computation for detailed pass/fail metrics
- The `setup()` method with parameters: `force_test_update`, `log_level`, `raise_on_error`, `success_threshold`, `enable_streamable_logs`
- Understanding test results with status values: Success, Failed, Aborted
- Integrating TestRunner into ETL pipelines for post-load validation with rollback capability
- External secrets manager setup for AWS, Azure, and GCP when credentials are not stored in the database
- Troubleshooting common errors: "Cannot decrypt service connection", "Access Denied", "Module not found", connection errors