---
type: concept
title: Semantic Layer as AI Context Layer
created: 2026-05-06
updated: 2026-05-06
tags: [semantic-layer, ai, llm, context, governance]
related: [semantic-layer-architecture, semantic-layer-evolution, finch, model-context-protocol, context-store, ECL-framework, data-catalog-critique]
sources: ["Semantic Layer in Big Tech.md"]
---
# Semantic Layer as AI Context Layer

The evolution of the semantic layer into a governed context layer for AI agents (Phase 5, 2024-2026). Rather than relying on LLMs to generate raw SQL from schema, Big Tech provides AI agents with pre-constructed semantic context.

## What the AI Context Layer Includes

Beyond simple metric formulas, the AI-era semantic layer provides:

- **Synonyms and aliases** for fields and values (Uber Finch uses OpenSearch for column/value aliases)
- **Data quality caveats** attached to metrics (Airbnb DQ Score + Minerva)
- **Acceptable date ranges** for time-series queries (Pinterest)
- **Valid join paths** between tables (Pinterest)
- **Table and column descriptions** (Pinterest AI-generated documentation)
- **Standardized glossary terms** (Pinterest)

## Key Examples

- **Google**: Looker semantic layer integrated with Gemini, Conversational Analytics API, and MCP. AI should query the semantic layer rather than generate raw SQL.
- **Uber Finch**: Operates on curated single-table data marts and a semantic layer built on metadata. Uses metadata aliases for accurate WHERE filters.
- **Pinterest**: Enriches LLM context with table descriptions, glossary terms, metric definitions, data quality caveats, and recommended date ranges before interpreting queries.

## Key Insight

Real enterprise AI built on top of data does not rely on raw SQL generation. It relies on a pre-constructed semantic context. Without this context, an LLM only sees raw tables and columns and loses the business meaning of the data.

## Relationship to MCP

The [[model-context-protocol]] provides a standard way for AI agents to access tools and data sources. The semantic layer provides the curated business context that makes those interactions meaningful and accurate. Together, they enable organizationally-aware AI.