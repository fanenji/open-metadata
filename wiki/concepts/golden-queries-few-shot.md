---
type: concept
title: Golden Queries for Few-Shot Prompting
created: 2026-05-07
updated: 2026-05-07
tags: [few-shot, text2sql, prompting, genbi]
related: [genbi-architecture, semantic-layer-for-text2sql, rag-for-database-schema, text2sql-patterns]
sources: ["Text-to-SQL is Finally Production-Ready Building a Semantic Layer for GenBI.md"]
---
# Golden Queries for Few-Shot Prompting

A pattern for improving Text-to-SQL generation on complex analytical questions by maintaining a vector store of verified, complex SQL queries paired with their natural language equivalents.

## How It Works

When a user asks a complex question (e.g., involving window functions or complex date math), the system retrieves similar "golden queries" from a vector store and inserts them into the prompt as few-shot examples. This dramatically improves performance on complex analytical questions beyond what RAG-over-schema alone can achieve.

## Production Considerations

- Golden queries must be verified for correctness before being added to the store
- The vector store for golden queries is separate from the schema vector store
- User edits and corrections can be captured via feedback loops to add new golden queries
- Golden queries are particularly important for questions involving window functions, date math, and multi-step analytical patterns

## Relationship to Existing Wiki

This concept extends [[text2sql-patterns]] by adding a few-shot prompting dimension. It is complementary to [[rag-for-database-schema]] — RAG handles schema retrieval, while golden queries handle complex query pattern retrieval.