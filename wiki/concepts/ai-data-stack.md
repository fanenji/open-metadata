---
type: concept
title: AI Data Stack
created: 2026-04-29
updated: 2026-04-29
tags: [data-architecture, ai, data-stack]
related: [context-management-vs-semantic-layer, data-agent-architecture, quirk-knowledge-store, dbt, jamie-quint]
sources: ["How to Build a Data Agent in 2026.md"]
---
# AI Data Stack

The AI Data Stack is the evolution of the Modern Data Stack, where AI agents replace the human translation layer (write SQL → build dashboard → schedule report → interpret results) with automated question-to-answer pipelines. While the Modern Data Stack made data accessible to analysts, the AI Data Stack makes data accessible to everyone.

## Key Differences from Modern Data Stack

| Aspect | Modern Data Stack | AI Data Stack |
|--------|-------------------|---------------|
| Primary user | Analysts | Everyone (non-technical teams) |
| Interface | Dashboards, SQL editors | Natural language (Slack, chat) |
| Translation layer | Human analyst | AI agent |
| Semantic model | Pre-defined, static | Dynamic context management |
| Knowledge retention | Analyst's memory | Quirk knowledge store |

## Core Components

1. **Ingestion** — Fivetran/Airbyte (same as Modern Data Stack)
2. **Organization** — dbt (same, but models become context source)
3. **Query Engine** — Snowflake/BigQuery (same)
4. **Context Agent** — Sub-agent that reads dbt models and app code at query time
5. **Main Agent** — Writes SQL based on context brief
6. **Knowledge Store** — Hybrid retrieval (vector + BM25) for quirks and metric definitions
7. **Self-Scoring Loop** — Agent evaluates its own output and retries

## Prerequisites

- Advanced AI model capable of data analysis (e.g., Opus 4.6)
- Accessible dbt repository and application codebase
- Annotated dbt base models with links to application code
- Slack integration for user interaction
- Knowledge store infrastructure (Postgres + pgvector)

## Limitations

- Model-dependent: relies on specific AI model capabilities
- No built-in security or access control mechanisms
- Requires careful management of knowledge store quality
- May not scale well to very large dbt projects without optimization