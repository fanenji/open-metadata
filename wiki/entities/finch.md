---
type: entity
title: Finch
created: 2026-05-06
updated: 2026-05-06
tags: [uber, conversational-agent, ai, semantic-layer]
related: [umetric, semantic-layer-ai-context, semantic-layer-architecture]
sources: ["Semantic Layer in Big Tech.md"]
---
# Finch

Uber's conversational data agent described in 2025. Finch operates on curated single-table data marts and a semantic layer built on metadata. It uses metadata aliases for columns and values stored in OpenSearch, allowing the LLM to generate more accurate WHERE filters and significantly reduce errors.

## Key Insight

Uber did not rely on the idea that "the LLM will figure out the schema itself." Instead, they rely on curated marts, metadata aliases, and governed access. Real enterprise AI built on top of data relies on a pre-constructed semantic context, not raw SQL generation.