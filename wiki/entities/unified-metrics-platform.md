---
type: entity
title: Unified Metrics Platform (UMP)
created: 2026-05-06
updated: 2026-05-06
tags: [linkedin, metrics-platform, semantic-layer]
related: [semantic-layer-architecture, metrics-as-code]
sources: ["Semantic Layer in Big Tech.md"]
---
# Unified Metrics Platform (UMP)

LinkedIn's centralized metrics platform designed to solve the problem of different teams calculating the same metrics in different ways. UMP centralizes metric definitions, computation, and serving.

## Key Characteristics

- Centralized metric definitions to eliminate duplication and inconsistency
- Batch and stream processing for metric computation
- Metrics store for serving
- Metrics API for consumption by dashboards and services

## Architecture

Raw events → Kafka → Batch + stream processing → Metrics computation → Metrics store → Metrics API → Dashboards / services

## Key Insight

LinkedIn turned the semantic layer into a real service — not a SQL model, but a metrics API.