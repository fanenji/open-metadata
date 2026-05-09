---
type: concept
title: Context Management vs Semantic Layer
created: 2026-04-29
updated: 2026-04-29
tags: [data-architecture, ai, semantic-layer, context-management]
related: [ai-data-stack, data-agent-architecture, quirk-knowledge-store, dbt, jamie-quint]
sources: ["How to Build a Data Agent in 2026.md"]
---
# Context Management vs Semantic Layer

A comparison of two approaches to bridging business concepts and data infrastructure in the AI Data Stack era.

## Semantic Layer (Traditional)

A static, hand-maintained mapping between business concepts and SQL (metrics, dimensions, relationships). Tools like MetricFlow and Cube.dev exemplify this approach.

**Advantages:**
- Precise, curated definitions for core metrics
- Predictable behavior for well-defined questions
- No runtime investigation overhead

**Disadvantages:**
- Painful to build and maintain
- Brittle — cannot cover edge cases
- Creates bottleneck: data team must anticipate every question
- Requires constant updates as data changes

## Context Management (AI Data Stack)

Dynamic investigation of source code (dbt models, application code) at query time. A context sub-agent reads transformation logic, traces dependencies, and builds a brief for the main agent.

**Advantages:**
- Adaptive — learns from corrections and usage
- Scales with codebase (reads the code)
- No pre-definition required
- Covers edge cases naturally

**Disadvantages:**
- Runtime overhead (context agent investigation)
- Depends on well-annotated dbt models
- Requires advanced AI model (e.g., Opus 4.6)
- No built-in governance or access control

## Hybrid Approach

The author recommends keeping 20% of the semantic layer: human-authored metric definitions for core KPIs that get asked about constantly. These are stored in the same knowledge store as quirks and retrieved the same way, but authored by humans when they feel like it rather than required for the system to function.