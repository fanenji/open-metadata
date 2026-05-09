---
type: entity
title: dbt Semantic Layer
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, semantic-layer, metrics, governance]
related: [dbt-mcp-server, governed-ai-access, dbt-cloud, dbt-core]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# dbt Semantic Layer

The dbt Semantic Layer is a feature of [[dbt-cloud]] that provides a governed, version-controlled interface for querying business metrics. It defines metrics with their business logic, dimensions, and time grains, ensuring consistent definitions across all consumers.

## Role in the dbt MCP Server

The Semantic Layer is the critical component that enables [[governed-ai-access]] through the [[dbt-mcp-server]]. Instead of AI systems writing ad-hoc SQL against raw tables, they query pre-defined metrics through the Semantic Layer, receiving your organization's actual, governed definitions every time.

## Key Capabilities Exposed via MCP

- `list_metrics` — Discover available metrics with their definitions
- `query_metrics` — Query metrics with dimensions and time grains
- Metric definitions with business logic baked in

## Benefits

- Eliminates hallucination from AI data queries
- Ensures consistent business definitions across all AI clients
- Provides governed access without requiring SQL knowledge
- Version-controlled metric definitions prevent drift