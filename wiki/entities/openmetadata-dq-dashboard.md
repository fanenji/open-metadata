---
type: entity
title: OpenMetadata Data Quality & Profiling Dashboard
created: 2026-03-19
updated: 2026-03-19
tags: [openmetadata, data-quality, dashboard, profiling]
related: [openmetadata, openmetadata-data-quality, openmetadata-ai-assistant, data-quality-dimensions]
sources: ["Suggested Data Quality Tools.md"]
---
# OpenMetadata Data Quality & Profiling Dashboard

The OpenMetadata Data Quality & Profiling Dashboard is a built-in UI component that provides real-time visibility into data quality test results and table profiles. It is part of [[openmetadata]]'s Data Quality module.

## Features

- **Test success/failure rates**: Visual overview of pass/fail ratios across all tests
- **Test history**: Timeline of test results for trend analysis
- **Profile statistics**: Column-level statistics including min, max, null counts, and distribution
- **Integration with dbt**: Ingests dbt test results via the dbt connector, surfacing them alongside native tests
- **Alerting**: Native webhook alerts (Slack, Email, MS Teams) triggered on test failures

## Role in the Stack

The dashboard fulfills the requirement for a centralized DQ overview without adding a separate visualization component. It complements [[datahub]] by providing dedicated DQ visualization, while DataHub serves as the broader catalog.

## Related Concepts

The dashboard visualizes metrics aligned with [[data-quality-dimensions]] and supports the [[data-quality-resolution-workflow]] by providing the visibility needed to track issue resolution.