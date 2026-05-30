---
type: source
title: "Source: tests---yaml-config-openmetadata-quality-config-gu-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["tests---yaml-config-openmetadata-quality-config-gu-20260514.md"]
tags: []
related: []
---

# Source: tests---yaml-config-openmetadata-quality-config-gu-20260514.md

## Key Entities

- **OpenMetadata** (platform) — Central entity; the system that defines and executes these tests.
- **Test Definition** (concept) — Generic definition of a test; becomes a Test Case when parameters are specified.
- **Test Case** (concept) — Parameterized instance of a Test Definition; the executable unit.
- **Table Tests** (category) — Tests applied at the table level (10 listed).
- **Column Tests** (category) — Tests applied at the column level (referenced but not detailed in this source).
- **Supported Connectors** (list) — Snowflake, BigQuery, Athena, Redshift, Postgres, MySQL, MSSQL, Oracle, Trino, SAP Hana (for the `tableDiff` test only).
- **YAML Config / JSON Config** (format) — The two serialization formats for defining test cases programmatically.
- **Test Suite** (concept) — Logical grouping of test cases; referenced in `tableDiff` and `tableDataToBeFresh` examples.

**Wiki Status:** All entities likely already exist in the wiki under [[data-quality]] or related pages. The specific test definitions and their YAML/JSON configurations are new content.

## Key Concepts

- **Test Definition vs. Test Case** — A Test Definition is a generic template; a Test Case binds it to specific parameters and an entity. This is the core abstraction for programmatic quality configuration.
- **Dimension** — Each test is classified under a quality dimension: Integrity (most table tests), Consistency (`tableDiff`), Accuracy (`tableDataToBeFresh`). This maps to standard data quality frameworks.
- **Threshold** — A numeric limit for pass/fail determination; used in `tableCustomSQLQuery` (default 0) and `tableDiff` (default 0). Rows returned above threshold → failure.
- **Strategy (ROWS vs. COUNT)** — For `tableCustomSQLQuery`: ROWS returns matching rows (risk of OOM), COUNT returns a single count value. Affects performance and memory.
- **Cross-Service Comparison** — `tableDiff` supports comparing tables across different database services (e.g., Snowflake vs. Redshift), a notable capability.
- **Partition Conflict** — `tableRowInsertedCountToBeBetween` cannot be executed against tables with a configured partition in OpenMetadata; it behaves like a filtered row count test.

**Wiki Status:** The Test Definition/Test Case distinction and the dimension classification are likely new. The concept of programmatic YAML/JSON configuration for quality tests is not yet documented in the wiki.

## Main Arguments & Findings

- **Core Claim:** OpenMetadata supports 10 table-level data quality tests, each with a specific purpose, dimension, properties, and pass/fail behavior.
- **Evidence:** The source provides complete YAML and JSON configuration examples for each test, along with behavior tables and property definitions.
- **Strength:** High — this is official documentation from the OpenMetadata project (v1.12.x). The examples are concrete and directly usable.

## Connections to Existing Wiki

- **[[data-quality]]** — This source is a direct sub-topic of d
