---
type: concept
title: Semantic Layer Architecture
created: 2026-05-06
updated: 2026-05-06
tags: [semantic-layer, data-platform, architecture, metrics]
related: [metrics-as-code, umetric, minerva, metrics-repo, unified-metrics-platform, semantic-layer-evolution, semantic-layer-ai-context, data-contract-platform, context-store, ECL-framework, data-quality-score]
sources: ["Semantic Layer in Big Tech.md"]
---
# Semantic Layer Architecture

The semantic layer in Big Tech is a **platform infrastructure component** — not a BI feature — that manages the full lifecycle of business metrics: definition, computation, quality, serving, governance, and AI grounding.

## Core Components

Based on the architectures of Uber, Netflix, LinkedIn, Airbnb, Spotify, Pinterest, and Google, an enterprise-grade semantic layer consists of:

1. **Metric Definitions (Code/Git)**: Programmatic definitions of business metrics in Python, YAML, or DSL, stored in version-controlled repositories with code review
2. **Metric Computation Engine**: Centralized computation that ensures metrics are calculated the same way everywhere
3. **Quality Validation**: Trust signals (data quality scores) attached to metrics as a non-optional component
4. **Metrics Catalog**: Searchable repository of metric definitions, descriptions, owners, lineage, and quality checks
5. **Metrics API / Serving Layer**: API-based consumption by BI tools, ML pipelines, applications, and AI agents
6. **Governance**: Ownership, access control, backfills, deprecation policies, cost attribution

## Unified Architecture

Data sources → Data warehouse/lakehouse → Transformation layer → Metric definitions (Git) → Metric computation engine → Metrics catalog → Metrics API → BI / ML / applications / AI

## Key Principles

- **Define once, use everywhere** (Airbnb Minerva)
- **Metrics as code** with version control, review, and lifecycle management
- **Trust signals are non-optional** — quality validation is a fundamental component
- **Federated governance** may be more realistic than a single universal system (Netflix pattern)
- **AI grounding** requires synonyms, quality caveats, valid join paths — not just formulas

## Relationship to Other Concepts

- [[data-contract-platform]]: Complementary — data contracts define producer-consumer agreements; semantic layers define business meaning. Both are needed for enterprise-grade data platforms.
- [[context-store]]: The semantic layer serves as a governed context store for AI agents, providing curated semantic context rather than raw schema.
- [[ECL-framework]]: The semantic layer operationalizes the "Contextualize" step by providing a versioned, queryable store of validated semantic definitions.
- [[data-quality-score]]: Extended to metric-level trust signals (Airbnb's DQ Score + Minerva, Uber's quality pillar).