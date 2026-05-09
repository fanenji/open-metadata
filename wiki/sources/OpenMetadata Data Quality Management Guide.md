---
type: source
title: "Data Quality | OpenMetadata Quality Management Guide"
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, data-quality, observability]
related: [openmetadata-data-quality, openmetadata-profiler, data-quality-resolution-workflow, data-observability-definition, data-incident-management]
sources: ["OpenMetadata Data Quality Management Guide.md"]
authors: ["OpenMetadata Documentation"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality"
venue: "OpenMetadata Documentation"
---
# Data Quality | OpenMetadata Quality Management Guide

This is the official OpenMetadata documentation page for the Data Quality module. It describes the four pillars of OpenMetadata's integrated data quality solution: native tests for all database connectors, an alerting system for test failures, a health dashboard for real-time visibility, and a resolution workflow to close the feedback loop with data consumers. The document also claims extensibility for adapting tests to custom needs, though no concrete examples or API details are provided.

The source is authoritative as official product documentation but promotional in nature. It provides no independent benchmarks, case studies, or comparisons with other data quality tools. Its value lies in documenting the canonical feature set and workflow of OpenMetadata's DQ module as of version 1.12.x.

## Key Points

- OpenMetadata supports data quality tests for all supported database connectors.
- Tests can be run at table and column levels for both business and technical use cases.
- The four pillars are: native tests, alerting system, health dashboard, and resolution workflow.
- The system is claimed to be extensible for custom needs.
- The profiler is a companion feature that feeds into data quality tests.

## Connections

- Strengthens [[openmetadata-data-quality]] with official documentation backing.
- Extends [[data-quality-resolution-workflow]] as a concrete implementation example.
- Related to [[data-observability-definition]] through alerting and dashboard features.
- Related to [[data-incident-management]] through alerting and resolution workflows.