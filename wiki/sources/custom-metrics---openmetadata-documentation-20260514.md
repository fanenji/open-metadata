---
type: source
title: Custom Metrics - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, custom-metrics, data-quality]
related: [custom-metrics, data-profiling, data-quality, profiler-agent, metadata-agent, data-observability-alerts]
sources: ["custom-metrics---openmetadata-documentation-20260514.md"]
---
# Custom Metrics - OpenMetadata Documentation

**Source:** [OpenMetadata v1.12.x Documentation - Custom Metrics](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/custom-metrics)

This official documentation page describes the **Custom Metrics** feature in OpenMetadata v1.12.x. Custom metrics allow users to define and compute unique business metrics using custom SQL queries at both the table and column levels. These metrics are incorporated into the profiler workflow and displayed alongside system metrics in table and column profiles.

## Key Content

- **Purpose:** Enhance profiling capabilities by enabling user-defined business metrics beyond system defaults.
- **Table-Level Metrics:** Defined via the Table Profile UI in the Data Observability tab; SQL queries aggregate over an entire table.
- **Column-Level Metrics:** Defined via the Column Profile UI; SQL queries are scoped to a single column with column selection.
- **Workflow:** Define metric → Run Profiler Agent → View computed value in profile.
- **Prerequisite:** The Profiler Agent must be executed after defining a custom metric to compute and display its value.

## Relevance

This source is the primary reference for the [[custom-metrics]] concept page. It extends the [[data-profiling]] and [[data-quality]] documentation by introducing a user-extensibility mechanism for profiling metrics.