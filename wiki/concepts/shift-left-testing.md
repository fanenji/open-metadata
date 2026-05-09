---
type: concept
title: Shift-Left Testing
created: 2026-04-07
updated: 2026-04-07
tags: [testing, devops, data-engineering]
related: [data-observability, github-actions]
sources: ["7 dbt testing best practices.md"]
---
# Shift-Left Testing

The practice of moving data quality checks earlier in the development lifecycle (the "left" side of the pipeline). In the context of dbt, this means validating transformations during the development phase and within the CI/CD pipeline before any code is merged into production.

### Benefits
- **Prevention over Detection:** Identifies errors before they propagate downstream.
- **Reduced Noise:** Decreases the number of production incidents that require observability-based detection.
- **Cost Efficiency:** Catching bugs during development is significantly cheaper than fixing them in production.
---END EXAMINE ---
---FILE: wiki/index.md---
# Wiki Index

## Entities
- [[dbt]] — Data transformation tool (SQL-based)
- [[dbt-expectations]] — Advanced testing capabilities for dbt
- [[data-diff]] — Value-level comparison of datasets
- [[github-actions]] — CI/CD automation platform

## Concepts
- [[data-contracts]] — Enforceable schema agreements for data stability
- [[data-diffing]] — (See [[data-diff]])
- [[data-lineage]] — Tracking data transformations and origins
- [[data-observability]] — Monitoring the health and accuracy of data pipelines
- [[data-governance]] — Rules and processes for managing data assets
- [[dbt-unit-testing]] — Validating model logic with fixed inputs
- [[dbt-testing-hierarchy]] — Multi-layered testing strategy (Generic, Unit, Diff)
- [[retrieval-augmented-generation]] — Technique for providing LLM context via external data
- [[shift-left-testing]] — Moving quality checks earlier in the lifecycle
- [[slim-ci]] — Efficient CI strategy for large-scale data projects
- [[smart-deferral]] — Technique to reuse production relations in CI
- [[vector-databases]] — Specialized databases for AI embeddings

## Sources
- [[3-reasons-data-engineers-are-the-unsung-heroes-of-genai]] — Article on the importance of data engineering in GenAI
- [[5-dbt-slim-ci-tactics-for-large-repos]] — Tactics for scaling dbt CI/CD
- [[7-dbt-testing-best-practices]] — Best practices for dbt testing strategies