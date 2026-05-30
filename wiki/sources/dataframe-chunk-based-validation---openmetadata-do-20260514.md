---
type: source
title: "Dataframe Chunk Based Validation   Openmetadata Do 20260514"
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
title: "DataFrame Chunk-Based Validation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, sdk, python, validation, chunking]
related: [dataframe-chunk-based-validation, dataframe-validator, two-phase-data-quality-validation, data-quality, test-runner]
sources: ["dataframe-chunk-based-validation---openmetadata-do-20260514.md"]
---
# DataFrame Chunk-Based Validation - OpenMetadata Documentation

**Source:** Official OpenMetadata v1.12.x documentation for chunk-based DataFrame validation.

**URL:** https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/dataframe-validation-chunking

## Summary

This document provides a practical, code-level guide for implementing data quality validation on large pandas DataFrames that do not fit in memory. It introduces the `DataFrameValidator` class from the OpenMetadata SDK (`metadata.sdk.data_quality.dataframes`) and presents two methods for chunk-based validation: manual chunk processing and the cleaner `run()` method with success/failure callbacks. The guide also covers transaction-safe chunk processing using context managers, failure modes (currently only `SHORT_CIRCUIT`), merging and publishing validation results, and the critical distinction between column-level tests (suitable for chunks) and full-table tests (which require the `TestRunner` after loading). A two-phase validation approach is recommended as best practice.

## Key Contributions

- Introduces chunk-based validation as a solution for memory-constrained environments.
- Provides two concrete implementation methods with executable code examples.
- Documents the `WholeTableTestsWarning` and the risks of applying full-table tests to chunks.
- Recommends a two-phase architecture: column-level tests during ETL, table-level tests after loading.
- Covers the `ValidationResult.merge()` and `ValidationResult.publish()` methods for aggregated reporting.

## Connections

- Extends the [[data-quality]] concept with practical implementation patterns.
- Related to [[data-profiling]] (profiling analyzes structure; validation checks against defined tests).
- Can be integrated into [[metadata-ingestion-workflow]] pipelines.
- The two-phase approach aligns with [[ingestion-framework]] patterns.