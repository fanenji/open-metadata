---
type: entity
title: OpenMetadata Profiler
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, data-quality, profiling]
related: [openmetadata-data-quality, openmetadata, data-quality-dimensions]
sources: ["OpenMetadata Data Quality Management Guide.md"]
---
# OpenMetadata Profiler

The OpenMetadata Profiler is a companion feature to the [[openmetadata-data-quality]] module. It performs automated data profiling across all supported database connectors, generating statistics and metrics about the data (e.g., row counts, null percentages, distinct values, min/max values, data type distributions). These profiling results feed into the data quality test system, enabling users to set informed thresholds and detect anomalies.

The profiler is a key enabler of the "native tests" pillar of OpenMetadata's data quality framework, as it provides the baseline measurements against which test assertions are evaluated. It is tightly integrated with the OpenMetadata platform and does not require separate installation or configuration beyond enabling the profiler workflow for a given database service.

## Capabilities

- Automated profiling of tables and columns across all supported connectors.
- Generation of descriptive statistics (row count, null count, distinct count, min/max, mean, standard deviation).
- Detection of schema changes and data type inconsistencies.
- Integration with the data quality test system for threshold-based assertions.

## Limitations

- Performance impact at scale on large tables (e.g., Iceberg tables with billions of rows) is not documented.
- Profiling frequency and sampling strategies are configurable but require manual tuning.
- No built-in support for custom metric definitions beyond the standard set.

## Connections

- Works in tandem with [[openmetadata-data-quality]] for test execution.
- Provides input data for [[data-quality-dimensions]] like completeness and accuracy.
- Part of the broader [[openmetadata]] platform ecosystem.