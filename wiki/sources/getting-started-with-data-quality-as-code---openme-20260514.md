---
type: source
title: "Getting Started With Data Quality As Code   Openme 20260514"
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
title: "Getting Started with Data Quality as Code - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, python, automation]
related: [data-quality-as-code, openmetadata-python-sdk, testrunner-api, data-quality, personal-access-token, ingestion-framework, metadata-cli]
sources: ["getting-started-with-data-quality-as-code---openme-20260514.md"]
---
# Getting Started with Data Quality as Code - OpenMetadata Documentation

This official OpenMetadata documentation page (v1.12.x) provides a comprehensive guide to installing, configuring, and using the OpenMetadata Python SDK to define and run data quality tests programmatically — an approach known as "Data Quality as Code."

## Key Content

- **Prerequisites**: Python 3.10+, pip, OpenMetadata instance v1.11.0+, and a JWT token.
- **Installation**: Instructions for installing the `openmetadata-ingestion` package with optional extras for database connectors (PostgreSQL, MySQL, BigQuery), DataFrame support (pandas), and multiple features.
- **Authentication**: Two methods for obtaining a JWT token — using the pre-configured `ingestion-bot` or creating a custom bot with specific roles. The SDK is configured via the `configure()` function, which can read from environment variables (`OPENMETADATA_HOST`, `OPENMETADATA_JWT_TOKEN`) for security.
- **First Test Walkthrough**: A complete code example demonstrating how to create a `TestRunner` for a specific table using its fully qualified name (FQN), add a `TableRowCountToBeBetween` test, execute it, and print results.
- **Troubleshooting**: Common issues such as connection timeouts and import errors, with recommended fixes.

## Significance

This source introduces the programmatic "Data Quality as Code" workflow as an alternative to UI-based data quality configuration. It enables CI/CD integration, version control, and automation of data quality pipelines. The SDK-based approach uses the same `openmetadata-ingestion` package as the [[ingestion-framework]] and shares authentication patterns with [[personal-access-token]] and [[metadata-cli]].

## Connections

- Directly related to [[data-quality]] — provides the programmatic implementation path.
- Related to [[personal-access-token]] — JWT authentication mechanism is shared.
- Related to [[ingestion-framework]] — the `openmetadata-ingestion` package is the same.
- Related to [[metadata-cli]] — both use the same underlying SDK for authentication and API communication.