---
type: source
title: How to Build a Data Agent in 2026
created: 2026-03-07
updated: 2026-03-07
tags: [ai-data-stack, data-agent, context-management, dbt]
related: [ai-data-stack, context-management-vs-semantic-layer, data-agent-architecture, quirk-knowledge-store, dbt, jamie-quint]
sources: ["How to Build a Data Agent in 2026.md"]
authors: [Jamie Quint]
year: 2026
url: "https://x.com/jamiequint/article/2029705203457609785"
venue: ""
---
# How to Build a Data Agent in 2026

A practical guide by [[Jamie Quint]] on building an AI data agent that replaces the traditional semantic layer with dynamic context management. The author, who built the initial data stack at Notion in 2020, describes a 3-week build that leverages advanced AI models (Opus 4.6) to create a system capable of 5x+ data team bandwidth.

## Core Thesis

The "Modern Data Stack" (Fivetran, dbt, Snowflake, Census) made data accessible to analysts. The "AI Data Stack" makes data accessible to everyone by replacing the human translation layer (SQL → dashboard → interpretation) with agents that go from question to answer automatically. With Opus 4.6's superior data analysis capabilities, the need for an advanced semantic layer has collapsed.

## Key Innovations

1. **Context Management over Semantic Layer** — Instead of pre-defining mappings between business concepts and SQL, a context sub-agent reads dbt model files, traces upstream dependencies, and checks application code at query time.
2. **Quirk Knowledge Store** — User corrections are extracted into durable, reusable pieces of knowledge stored with embeddings for hybrid retrieval (vector + BM25).
3. **Self-Scoring Agent** — The agent scores its own SQL on structural correctness, execution reliability, and context alignment, then builds a context-gap brief to drive recovery loops.
4. **Hybrid Retrieval Tuning** — Collection weights, reviewed-item multipliers, reciprocal-rank fusion, and fixed context budgets for optimal knowledge retrieval.

## Caveats

- The approach depends on Opus 4.6 being superior to Codex 5.3 xhigh for data analysis — a model-specific claim.
- The author admits 20% of the semantic layer (human-authored metric definitions for core KPIs) remains useful.
- No discussion of security, access control, or data governance implications.
- Evidence is anecdotal (single company, 3-week build, no benchmarks).