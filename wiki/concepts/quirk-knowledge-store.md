---
type: concept
title: Quirk Knowledge Store
created: 2026-04-29
updated: 2026-04-29
tags: [knowledge-management, ai, retrieval, dbt]
related: [data-agent-architecture, ai-data-stack, context-management-vs-semantic-layer, dbt, jamie-quint]
sources: ["How to Build a Data Agent in 2026.md"]
---
# Quirk Knowledge Store

A pattern for storing and retrieving learned corrections from user feedback in an AI data agent system. When a user corrects the agent ("no, that metric needs this filter" or "that table has duplicate rows, you need to dedup on X"), the correction is extracted into a durable, reusable piece of knowledge called a "quirk."

## Quirk Format

A quirk is a short, reusable piece of knowledge, for example:
> "The orders table has duplicate rows per order when there are multiple shipments; always dedup on order_id."

## Storage Implementation

- **Vector Store:** Postgres with pgvector extension
- **Embeddings:** OpenAI text-embedding-3-small
- **Keyword Search:** pg_textsearch for BM25
- **Retrieval:** Hybrid (vector similarity + keyword search)

## Retrieval Tuning

- **Collection weights** — Balance how much to favor metrics vs. quirks in results
- **Reviewed-item multiplier** — Ensure human-approved knowledge ranks higher than agent-learned knowledge
- **Reciprocal-rank fusion** — Blend vector and BM25 candidates into a single ranked list
- **Fixed context budget** — Prevent stuffing the entire knowledge store into every prompt

## Human-Authored Metric Definitions

In addition to quirks, the knowledge store also contains human-authored definitions for core KPIs. These are structured definitions with inference guidance (how to calculate, what filters apply, etc.). This represents the 20% of the semantic layer that was actually useful, maintained by humans when they feel like it rather than required for the system to function.

## Benefits

- Institutional knowledge that used to live in one analyst's head becomes durable and searchable
- The semantic layer rebuilds itself from usage rather than requiring an analyst to maintain it
- Scales with usage — more corrections make the system smarter over time
- Reduces onboarding time for new team members