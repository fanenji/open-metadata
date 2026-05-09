---
type: concept
title: OpenMetadata Data Quality
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, data-quality, observability]
related: [openmetadata-profiler, openmetadata-database-connectors, data-quality-resolution-workflow, data-observability-definition, data-incident-management, great-expectations-for-data-contracts, dbt-expectations]
sources: ["OpenMetadata Data Quality Management Guide.md"]
---
# OpenMetadata Data Quality

OpenMetadata Data Quality is the built-in data quality module of the [[openmetadata]] platform. It provides an integrated solution for monitoring and enforcing data quality across all supported database connectors, organized around four pillars:

1. **Native Tests** — Built-in assertions at table and column levels for all database connectors. Tests can verify completeness, freshness, accuracy, uniqueness, and other [[data-quality-dimensions]] without requiring external tools or custom code.

2. **Alerting System** — Sends notifications (email, Slack, webhook) when tests fail, enabling real-time incident response. Alerts can be configured per test or per data asset.

3. **Health Dashboard** — Provides real-time visibility into test failure rates, trends, and prioritization. The dashboard helps teams identify the most critical data quality issues at a glance.

4. **Resolution Workflow** — Informs data consumers when previously failed tests are resolved, closing the feedback loop. This is a concrete implementation of the [[data-quality-resolution-workflow]] pattern.

The module is claimed to be **extensible**, allowing users to adapt tests to custom needs, though the official documentation (as of v1.12.x) does not provide concrete examples or API details for custom test creation.

## Relationship to Profiler

The [[openmetadata-profiler]] is a companion feature that automatically profiles data sources, generating statistics that inform test thresholds and anomaly detection. The profiler and DQ module work together: profiling provides baseline measurements, and DQ tests assert against those baselines.

## Comparison with Other Tools

- **vs. [[great-expectations-for-data-contracts]]**: OpenMetadata DQ is tightly integrated with the metadata catalog, offering a unified experience. Great Expectations provides more extensive test libraries and is tool-agnostic.
- **vs. [[dbt-expectations]]**: dbt-expectations brings Great Expectations-style tests to dbt, which is transformation-native. OpenMetadata DQ is catalog-native. The choice depends on whether the team's workflow centers on dbt or on the metadata platform.

## Open Questions

- Performance impact of running profiler + DQ tests at scale (e.g., on large Iceberg tables) is not documented.
- Does the resolution workflow support automated remediation (e.g., re-running failed pipelines) or is it purely notification-based?
- How does test coverage and flexibility compare to dedicated DQ tools like Great Expectations?

## Connections

- Strengthens [[openmetadata]] as a data catalog tool with integrated quality features.
- Extends [[data-observability-definition]] by adding the resolution workflow as an eighth dimension.
- Related to [[data-incident-management]] through alerting and resolution patterns.
- Competes with [[great-expectations-for-data-contracts]] and [[dbt-expectations]] for DQ enforcement.