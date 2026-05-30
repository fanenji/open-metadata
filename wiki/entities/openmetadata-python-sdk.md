---
type: entity
title: "Openmetadata Python Sdk"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: OpenMetadata Python SDK
created: 2026-05-14
updated: 2026-05-14
tags: [sdk, python, data-quality, ingestion]
related: [data-quality-as-code, testrunner-api, data-quality, personal-access-token, ingestion-framework, metadata-cli]
sources: ["getting-started-with-data-quality-as-code---openme-20260514.md"]
---
# OpenMetadata Python SDK

The OpenMetadata Python SDK is the programmatic interface for interacting with the OpenMetadata platform. It is distributed as part of the `openmetadata-ingestion` Python package and provides modules for authentication, metadata operations, and data quality testing.

## Key Components

- **`metadata.sdk.configure()`**: The entry point for SDK configuration. Accepts `host` (API URL) and `jwt_token` parameters, or reads them from environment variables (`OPENMETADATA_HOST`, `OPENMETADATA_JWT_TOKEN`).
- **`metadata.sdk.data_quality.TestRunner`**: The primary class for running table-level data quality tests programmatically.
- **`metadata.sdk.data_quality.TableRowCountToBeBetween`**: An example test definition class for verifying row counts are within a specified range.

## Installation

The SDK is installed via pip:

```bash
pip install "openmetadata-ingestion>=1.12.0.0"
```

Optional extras are available for database connectors (e.g., `[postgres]`, `[mysql]`, `[bigquery]`) and DataFrame support (`[pandas]`).

## Authentication

The SDK uses JWT token authentication. The `configure()` function accepts a `jwt_token` parameter or reads it from the `OPENMETADATA_JWT_TOKEN` environment variable. Tokens can be obtained from pre-configured bots (like the `ingestion-bot`) or custom bots created in Settings > Bots.

## Relationship to Other Components

- The `openmetadata-ingestion` package is the same package used by the [[ingestion-framework]] for metadata ingestion pipelines.
- The SDK shares authentication patterns with [[personal-access-token]] and [[metadata-cli]].
- The SDK enables the [[data-quality-as-code]] workflow, providing a programmatic alternative to UI-based [[data-quality]] configuration.