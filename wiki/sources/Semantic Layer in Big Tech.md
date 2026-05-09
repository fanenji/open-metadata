---
type: source
title: "Secrets of the Semantic Layer in Big Tech: How Uber, Netflix, and Airbnb Manage Metrics"
created: 2026-05-06
updated: 2026-05-06
tags: [semantic-layer, metrics, big-tech, data-platform, ai-context]
related: [semantic-layer-architecture, metrics-as-code, umetric, minerva, metrics-repo, unified-metrics-platform, semantic-layer-evolution, semantic-layer-ai-context, data-quality-score, context-store, data-catalog-critique, data-contract-platform]
sources: ["Semantic Layer in Big Tech.md"]
authors: [Sergey Gromov]
year: 2026
url: "https://pub.towardsai.net/secrets-of-the-semantic-layer-in-big-tech-how-uber-netflix-and-airbnb-manage-metrics-1b9f7680ac25"
venue: "Towards AI"
---
# Secrets of the Semantic Layer in Big Tech

This article by Sergey Gromov synthesizes publicly available engineering blogs, papers, and talks from Uber, Netflix, LinkedIn, Airbnb, Spotify, Pinterest, and Google to reconstruct the real architecture of a semantic layer in large technology companies.

## Core Thesis

Big Tech treats the semantic layer as a **platform infrastructure component** — not a BI feature. It manages the full lifecycle of metrics: definition, computation, quality, serving, governance, and AI grounding.

## Key Case Studies

- **Uber (uMetric)**: Centralized platform covering the entire metric lifecycle. Used for both analytics and ML features. Their conversational agent Finch relies on curated marts and metadata aliases, not raw SQL generation.
- **Netflix (Metrics Repo)**: Python framework for programmatic metric definitions. Primarily used for A/B testing and experimentation, not just BI. Reveals a federated pattern of domain-specific repositories.
- **LinkedIn (Unified Metrics Platform)**: Centralized metric definitions, computation, and serving via a Metrics API. Solved the problem of different teams calculating the same metrics differently.
- **Airbnb (Minerva)**: 12,000+ metrics, 4,000+ dimensions, 200+ data producers. Metrics defined in a centralized GitHub repo with code review, static validation, and test runs. Principle: "define once, use everywhere." Extended Data Quality Score to metrics.
- **Spotify**: API in front of the data warehouse. Metrics must be reproducible across experiments.
- **Pinterest**: Enriches LLM context with table descriptions, glossary terms, metric definitions, data quality caveats, and recommended date ranges — maintained automatically through AI-generated documentation and semantic matching.

## Evolution Phases (2010-2026)

1. **2010-2014**: Metrics live in reports and pipelines (fragmented, siloed)
2. **2015-2019**: Standardization for experimentation (Netflix Metrics Repo, LinkedIn UMP)
3. **2020-2022**: Metrics-as-Code and serving layer (Spotify API, Uber uMetric, Airbnb Minerva)
4. **2023-2024**: Open ecosystems and composability (Google Looker Open SQL Interface)
5. **2024-2026**: Semantic layer as AI context layer (Google Gemini + Looker + MCP, Uber Finch)

## Maturity Stages

1. Stop the chaos (no Excel/BI-calculated fields as source of truth)
2. Define once (centralized specification/code layer)
3. Compute once (same computation everywhere)
4. Serve everywhere (APIs, query layers, semantic endpoints)
5. Add trust (quality checks, ownership, review processes)
6. Ground AI on it (semantic layer as context for AI agents)

## Key Insights

- The semantic layer is **not a tool** but the **operating system of business metrics**
- Enterprise-grade semantic layers require three components: definition of meaning, computation mechanism, and trust/quality signal
- In the AI era, the semantic layer must include synonyms, quality caveats, acceptable date ranges, and valid join paths — not just formulas
- The real architecture is often closer to **federated semantic governance** (Netflix) than a single universal system

## Caveats

- The article is published on Towards AI (not peer-reviewed) and promotes DataForge, introducing potential vendor bias
- The author does not resolve the tension between centralized (Airbnb, LinkedIn) and federated (Netflix) patterns