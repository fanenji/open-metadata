---
type: source
title: "Metrics | OpenMetadata Profiler Metrics Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [profiler, metrics, data-quality, data-profiling]
related: [profiler-metrics, system-metrics, data-profiling, data-quality, profiler-workflow]
sources: ["metrics-openmetadata-profiler-metrics-guide---open-20260514.md"]
---
# Metrics | OpenMetadata Profiler Metrics Guide

**URL:** https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/metrics

This source is the official OpenMetadata documentation page for Profiler Metrics (v1.12.x). It defines the concept of a Metric as a computation on a Table or Column returning a value, built generically via SQLAlchemy for cross-database portability. The page catalogs all supported metrics across three categories: Table Metrics (Row Count, Column Count), System Metrics (DML Operations, Rows Affected by DML Operation — available only for Snowflake, Redshift, and BigQuery), and Column Metrics (20+ metrics including Values Count, Null Count, Unique Count, Distinct Count, Min, Max, Mean, Median, Standard Deviation, Histogram, Quartiles, and Nonparametric Skew). It also documents the complex types limitation (ARRAY and STRUCT not supported) and provides database-specific grant access instructions for System Metrics.

## Key Content

- **Metric Definition:** A computation on a Table or Column returning a value; the primary building block of the Profiler. Metrics are SQLAlchemy expressions, not database-specific.
- **Profiler Definition:** The binding between a set of metrics and the external world (Table + Session); executes the metrics.
- **Table Metrics:** Row Count, Column Count.
- **System Metrics:** DML Operations (timeseries of INSERT/UPDATE/DELETE) and Rows Affected by DML Operation. Only for Snowflake, Redshift, BigQuery. Monitors data freshness over a 24-hour / previous-day window.
- **Column Metrics:** 20+ metrics with precise definitions and formulas (e.g., Duplicate Count = count(col) - count(distinct(col)); Nonparametric Skew = (mean - median) / standard deviation).
- **Complex Types Limitation:** ARRAY and STRUCT not supported; future implementation noted.
- **Grant Access Instructions:** Required system tables/views for Snowflake (QUERY_HISTORY_BY_WAREHOUSE), Redshift (SVV_TABLE_INFO, STL_INSERT, STL_DELETE, etc.), and BigQuery (INFORMATION_SCHEMA.JOBS).