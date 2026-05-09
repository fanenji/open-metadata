---
type: concept
title: Impact Analysis
created: 2026-04-04
updated: 2026-04-04
tags: [data-governance, dbt, change-management]
related: [dbt-exposures, downstream-lineage, data-contract-observability]
sources: ["Why aren’t you using dbt Exposures?.md"]
---
# Impact Analysis

Impact analysis in data engineering refers to the practice of determining which downstream assets (dashboards, reports, ML models, applications) will be affected by a change to a data model. [[dbt-exposures]] enable impact analysis by explicitly documenting the dependencies between dbt models and their downstream consumers.

## Benefits

- Reduces the anxiety of making changes to production models.
- Enables proactive, informed communication with stakeholders before changes are made.
- Transforms reactive firefighting ("who touched the revenue model?") into proactive partnership.
- Supports model review sessions by answering questions about model purpose and continued relevance.

## Relationship to Other Concepts

- [[downstream-lineage]] — The lineage graph that enables impact analysis.
- [[data-contract-observability]] — Impact analysis is a key component of data contract observability.