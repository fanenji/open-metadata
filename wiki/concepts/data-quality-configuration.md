---
type: concept
title: Data Quality Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, configuration, how-to]
related: [data-quality, test-suite, test-definition, test-case, data-observability-alerts, data-profiling]
sources: ["configure-data-quality-official-documentation---op-20260514.md"]
---
# Data Quality Configuration

This page documents the procedure for configuring and running Data Quality tests in OpenMetadata, based on the official documentation.

## Requirements

- A running OpenMetadata deployment (including the server, [[elasticsearch-7x|Elasticsearch]], [[mysql-8x|MySQL]], and Airflow for ingestion workflows).
- Python version 3.9.0 or later.

## Building Trust with Data Quality

OpenMetadata positions Data Quality as the mechanism to make data assets **trustable**, complementing metadata ingestion which makes assets **discoverable**. The configuration workflow involves defining tests using the built-in test library.

## Configuration Workflow

1. **Define Test Definitions** — Create generic test templates specifying test name, column name, and data type.
2. **Create Test Cases** — Instantiate Test Definitions with specific pass/fail conditions (e.g., `max=n`).
3. **Organize into Test Suites** — Group related Test Cases into Logical or Executable Test Suites.
4. **Run Executable Test Suites** — Execute tests on associated tables to verify data integrity.

## Key Distinctions

- **Logical Test Suite**: Groups test cases from multiple tables; no execution pipeline. Used for consolidated visualization and management.
- **Executable Test Suite**: Associated with a single table; has an execution pipeline for direct testing.
- **Test Definition**: Generic template (name, column, data type).
- **Test Case**: Specific condition (e.g., `max=n`) linked to a Test Definition.

## Related Concepts

- [[data-quality]] — The overarching capability.
- [[test-suite]] — Logical container for test cases.
- [[test-definition]] — Generic test template.
- [[test-case]] — Specific test condition.
- [[data-observability-alerts]] — Alerting system that Test Suites are designed to reduce overload for.
- [[data-profiling]] — Companion capability for understanding data structure and content.