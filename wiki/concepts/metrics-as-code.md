---
type: concept
title: Metrics-as-Code
created: 2026-05-06
updated: 2026-05-06
tags: [metrics, code, governance, semantic-layer]
related: [semantic-layer-architecture, minerva, metrics-repo, unified-metrics-platform, data-contract-platform, YAML-data-contract-format]
sources: ["Semantic Layer in Big Tech.md"]
---
# Metrics-as-Code

The practice of defining business metrics programmatically (in Python, YAML, DSL, or similar) and managing them in version-controlled repositories with code review, static validation, and test runs.

## Key Characteristics

- Metrics are defined in code, not inside BI tools or SQL pipelines
- Definitions go through code review, static validation, and test runs
- Version control enables changelogs, rollbacks, and lifecycle management
- Intermediate computations are reused across use cases

## Examples

- **Netflix Metrics Repo**: Python framework where users define programmatically generated SQL queries and metric definitions
- **Airbnb Minerva**: Metric and dimension definitions stored in a centralized GitHub repository with code review, static validation, and test runs
- **LinkedIn UMP**: Centralized metric definitions to eliminate duplication and inconsistency

## Benefits

- Reproducibility: Every experiment relies on the same metric definitions
- Consistency: Eliminates discrepancies between metrics calculated by different teams
- Governance: Ownership, deprecation policies, and lifecycle management are formalized
- Reuse: Metrics can be consumed by BI, experimentation, ML, and AI systems

## Relationship to Data Contracts

Metrics-as-code is complementary to [[data-contract-platform]]. While data contracts define the schema and constraints of data products, metrics-as-code defines the business meaning and computation of metrics built on top of those data products.