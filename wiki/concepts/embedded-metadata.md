---
type: concept
title: Embedded Metadata
created: 2026-05-07
updated: 2026-05-07
tags: [metadata, data-governance, data-catalog, workflow-integration]
related: [data-catalog-critique, data-contract-platform, dbt-testing-patterns, model-context-protocol, geospatial-analytics-with-dbt]
sources: ["Data Catalog - A Broken Promise.md"]
---
# Embedded Metadata

The pattern of capturing metadata directly within data creation and transformation tools (e.g., dbt, Airflow) rather than relying on a separate data catalog interface. This approach, advocated by [[Ananth Packkildurai]] in his critique of data catalogs, eliminates the adoption barrier of requiring users to learn and use a standalone system.

## Key Principles

- **Capture at Source**: Metadata is generated automatically as a byproduct of data work, not as a separate documentation task.
- **No Separate UI**: Users interact with metadata through the tools they already use (dbt docs, Airflow DAG views, etc.).
- **Workflow Integration**: Governance and discovery are embedded into the engineering workflow, reducing friction.

## Examples in Practice

- [[dbt-testing-patterns]] and [[dbt-expectations]] — Tests and documentation are defined alongside transformations in dbt.
- [[geospatial-analytics-with-dbt]] — H3 indexes and OSM tags serve as embedded metadata within the transformation layer.
- [[model-context-protocol]] — Exposes metadata through AI interfaces rather than requiring a separate catalog UI.

## Trade-offs

- **Pros**: Higher adoption, lower training overhead, metadata stays in sync with code.
- **Cons**: Less accessible to non-technical users, may not satisfy compliance requirements for a separate audit trail, harder to provide cross-tool discovery.