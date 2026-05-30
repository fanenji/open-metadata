---
type: source
title: Configure Data Quality | Official Documentation - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-suite, test-definition, test-case, official-documentation]
related: [data-quality, test-suite, test-definition, test-case, data-observability-alerts, ingestion-framework, elasticsearch-7x, mysql-8x]
sources: ["configure-data-quality-official-documentation---op-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/configure"
venue: "OpenMetadata Documentation"
---
# Configure Data Quality | Official Documentation

This source is the official OpenMetadata v1.12.x documentation page for configuring Data Quality. It introduces the core concepts of Test Suites (Logical and Executable), Test Definitions, and Test Cases, and positions Data Quality as the mechanism to make data assets "trustable" (as opposed to "discoverable" via metadata ingestion). The page lists OpenMetadata (with Elasticsearch, MySQL, Airflow) and Python 3.9+ as requirements.

Key contributions to the wiki:
- Defines the **Test Suite** as a logical container for grouping related Test Cases from different tables to reduce alerting overload.
- Introduces the critical distinction between **Logical Test Suites** (multi-table, no execution pipeline) and **Executable Test Suites** (single-table, runnable).
- Defines **Test Definition** as a generic test template specifying test name, column name, and data type.
- Defines **Test Case** as a specific condition (e.g., max=n) linked to a Test Definition.
- Positions Data Quality as a companion to Data Profiling for building trust in data assets.