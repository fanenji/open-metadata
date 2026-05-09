---
type: entity
title: uMetric
created: 2026-05-06
updated: 2026-05-06
tags: [uber, metrics-platform, semantic-layer]
related: [semantic-layer-architecture, metrics-as-code, finch, semantic-layer-ai-context, data-quality-score]
sources: ["Semantic Layer in Big Tech.md"]
---
# uMetric

Uber's centralized unified metrics platform that manages the entire lifecycle of metrics: definition, discovery, computation, quality validation, and consumption. uMetric serves as both a semantic layer and a metric platform.

## Key Characteristics

- Covers full metric lifecycle from definition to consumption
- Extends metrics into machine learning features, bridging analytics and ML
- Includes a quality pillar for metric-level validation
- Supports Uber's conversational data agent Finch through curated data marts and metadata aliases

## Architecture

Event streams → Data pipelines → Metric definitions → Metric computation engine → Quality validation → Metric API → Dashboards / ML / Apps