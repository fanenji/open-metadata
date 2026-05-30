---
type: source
title: "Dimensional Validation Data Quality Testing By Dim 20260514"
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
title: Dimensional Validation | Data Quality Testing by Dimension
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, dimensional-validation, openmetadata]
related: [dimensional-validation, impact-score, data-quality, data-profiling, profiler-partitioning]
sources: ["dimensional-validation-data-quality-testing-by-dim-20260514.md"]
---
# Dimensional Validation | Data Quality Testing by Dimension

**Source:** Official OpenMetadata documentation (v1.12.x) covering the dimensional validation feature for data quality testing.

## Summary

This document introduces dimensional validation, a feature that allows data quality tests to be grouped by a categorical dimension column, producing per-segment results instead of a single pass/fail outcome. It covers key concepts (dimension column, dimension group, top dimensions, "Others" group, cardinality, impact score), when to use and when not to use the feature, a quick start guide, results interpretation, best practices, real-world examples, limitations, and troubleshooting.

## Key Contributions

- Defines the concept of dimensional validation and its value for granular data quality analysis
- Introduces the impact score (0.0-1.0) as a ranking mechanism balancing failure rate and absolute failure volume
- Provides cardinality guidance (recommended 5-25 unique values for optimal performance)
- Documents the "Others" group mechanism for handling dimensions with more than 10 unique values
- Includes three real-world examples (e-commerce product descriptions, multi-region email validation, financial transaction monitoring)
- Covers limitations: high cardinality performance impact (5-10x longer execution) and "Others" group information loss

## Connections

- Directly extends [[data-quality]] with an advanced testing capability
- References [[data-profiling]] for Profile Sample configuration as an optimization
- References partitioning (see [[profiler-partitioning]]) as another optimization
- The impact score ranking is a key differentiator (see [[impact-score]])