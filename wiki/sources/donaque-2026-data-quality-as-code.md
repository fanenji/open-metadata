---
type: source
title: "How to Get Started with Data Quality as Code in Your Pipelines"
created: 2026-07-15
updated: 2026-07-15
tags: [data-quality, data-quality-as-code, sdk, pipelines, shift-left]
related: [data-quality-as-code, data-quality, openmetadata, great-expectations]
authors: [Eugenio Doñaque]
year: 2026
source_path: "[[raw/sources/How to Get Started with Data Quality as Code in Your Pipelines]]"
sources: ["https://blog.open-metadata.org/how-to-get-started-with-data-quality-as-code-in-your-pipelines-122af5b93d7f"]
venue: "OpenMetadata Blog"
---
# How to Get Started with Data Quality as Code in Your Pipelines

Official blog post by **Eugenio Doñaque** (January 20, 2026), Part 2 of a series on Data Quality as Code in OpenMetadata 1.11. The article is a hands-on implementation guide covering the Python SDK, circuit breaker patterns, and collaborative quality management across roles.

## Key Contributions

- **Practical implementation**: Code examples using `DataFrameValidator`, `TestRunner`, and `TableRowCountToBeBetween` from the `metadata.sdk.data_quality` package
- **Pipeline refactoring pattern**: Shift from "extract → transform → load → test-after" to "extract → transform → validate → load-only-if-pass"
- **Circuit breaker logic**: First-class support for halting pipelines, rolling back transactions, and filtering bad records
- **Comparison with Great Expectations**: OpenMetadata differentiates through unified metadata integration, incident management, and collaborative UI+SDK approach
- **Role-based collaboration model**: Data stewards (UI rules), engineers (SDK execution), consumers (visibility), platform teams (governance)

## Relevance to This Wiki

This source introduces [[data-quality-as-code]], a programmatic approach to data validation that extends the existing [[data-quality]] framework with SDK-driven, pipeline-embedded testing.