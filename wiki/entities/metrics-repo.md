---
type: entity
title: Metrics Repo
created: 2026-05-06
updated: 2026-05-06
tags: [netflix, metrics-platform, semantic-layer]
related: [semantic-layer-architecture, metrics-as-code, federated-semantic-governance]
sources: ["Semantic Layer in Big Tech.md"]
---
# Metrics Repo

Netflix's internal Python framework for centralized metric definitions. Metrics are defined programmatically, generating SQL queries from Python code. The system is primarily used for A/B testing, product experimentation, and causal inference — not just BI.

## Key Characteristics

- Metrics defined programmatically, not inside a BI tool
- Metric computation moves out of ETL pipelines and closer to analysts
- Used primarily for experimentation platform, not just dashboards
- Part of a federated pattern: domain-specific metric repositories for different use cases (experimentation, efficiency analytics, creative analytics)

## Architecture

Raw data → Data warehouse → Metrics Repo (definitions in code) → Experimentation platform → Statistics engine → Dashboards / decision systems