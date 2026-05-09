---
type: concept
title: Full Data Stack Observability
created: 2026-05-06
updated: 2026-05-06
tags: [data-observability, monitoring, lineage, anomaly-detection]
related: [data-observability-definition, data-observability-three-pillars, data-incident-management, data-root-cause-analysis, sifflet, data-catalog-critique]
sources: ["Data Quality Monitoring is dead. Say Hello to Full Data Stack Observability.md"]
---
# Full Data Stack Observability

Full Data Stack Observability is an overseeing layer for the modern data stack that ensures data reliability at every stage of the enterprise data pipeline — from ingestion through storage and processing to BI tools and data science models. It extends the concept of [[data-observability-definition]] by explicitly covering all compartments of the data journey.

The framework is built on three pillars adapted from software observability:
- **Metrics** — measuring data quality (freshness, completeness, duplication, schema, accuracy)
- **Metadata** — data about the data (schema changes, volume, pipeline status)
- **Lineage** — dependencies between data assets enabling root cause analysis and impact assessment

Key applications include anomaly detection, incident management, root cause analysis, and post-mortem analysis. The term was introduced by [[Sifflet]], positioning it as the first Full Data Stack Observability platform.
