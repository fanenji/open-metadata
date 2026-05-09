---
type: concept
title: Governed AI Access
created: 2026-05-07
updated: 2026-05-07
tags: [ai, data-governance, semantic-layer, mcp]
related: [dbt-mcp-server, dbt-semantic-layer, model-context-protocol, data-contract-platform]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# Governed AI Access

Governed AI access is the paradigm where AI systems query governed, semantically understood data rather than writing ad-hoc SQL against raw tables. This is the core architectural insight behind the [[dbt-mcp-server]].

## The Problem

When LLMs connect directly to warehouses, they:
- Don't know what "revenue" means at your company
- Don't know that `fct_orders` excludes internal test orders
- Don't know currency conversion logic lives in a macro
- Write raw SQL against raw tables and hallucinate calculations

## The Solution

Instead of the AI guessing what metrics mean by reading raw SQL, it queries pre-defined, version-controlled semantic layer metrics from the [[dbt-semantic-layer]]. This provides:
- Your company's actual, governed definition every time
- No hallucination
- No drift
- No inconsistency

## Three Shifts Enabled

1. **From BI dashboards to conversational data**: Analysts stop building charts and start answering questions. The AI queries the governed metric directly.
2. **From manual dbt workflows to agentic pipelines**: Scheduled jobs get augmented by AI agents that can detect anomalies, trigger reruns, debug failures, and report results autonomously.
3. **From ad-hoc SQL to governed queries**: `text_to_sql` generates SQL using project context, not generic patterns — reducing hallucinations dramatically against raw table schemas.

## Relationship to Data Contracts

Governed AI access complements [[data-contract-platform]] by ensuring that AI agents consume data through the same governed interfaces that enforce producer-consumer agreements. The semantic layer becomes the enforcement point for both human and AI data consumers.