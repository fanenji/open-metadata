---
type: concept
title: "Profiler Partitioning"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Profiler Partitioning
created: 2026-05-14
updated: 2026-05-14
tags: [data-profiling, partitioning, optimization, openmetadata]
related: [data-profiling, dimensional-validation, data-quality]
sources: ["dimensional-validation-data-quality-testing-by-dim-20260514.md"]
---
# Profiler Partitioning

Profiler partitioning is an optimization feature in [[OpenMetadata]] that allows data profiling and data quality tests to focus on specific partitions of a table, rather than scanning the entire dataset. It is particularly useful for large tables and for [[dimensional-validation]] tests where performance is a concern.

## Purpose

- Reduces data scan volumes for profiling and quality test execution
- Enables tests to focus on meaningful data subsets (e.g., recent data by date partition)
- Mitigates the performance impact of [[dimensional-validation]] on large tables

## Configuration

Partitioning is configured through the Profiler Workflow settings in the OpenMetadata UI. The "Enable Partition" option allows you to specify a partition column and filter criteria.

## Relationship to Dimensional Validation

The [[dimensional-validation]] documentation recommends enabling partitioning for large tables as a performance optimization strategy. Partitioning and dimensional validation serve different purposes:

- **Partitioning:** Limits the *scope* of data scanned (e.g., only last 30 days)
- **Dimensional Validation:** Groups results by a *categorical dimension* for segmented analysis

They can be combined: a dimensional test can run on a partitioned subset of data.

## Best Practices

- Use partitioning columns that align with business time periods (e.g., `order_date`, `created_at`)
- Ensure partition configuration includes relevant date ranges for the test
- Verify that partitioning does not filter out all data (which would cause "No results" in dimensional tests)