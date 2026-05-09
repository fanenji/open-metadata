---
type: concept
title: GenBI Architecture
created: 2026-05-07
updated: 2026-05-07
tags: [genbi, text2sql, architecture, rag]
related: [semantic-layer-for-text2sql, rag-for-database-schema, golden-queries-few-shot, text2sql-patterns, context-store]
sources: ["Text-to-SQL is Finally Production-Ready Building a Semantic Layer for GenBI.md"]
---
# GenBI Architecture

Generative Business Intelligence (GenBI) architecture is a pipeline pattern that enables non-technical users to query data warehouses using natural language. The core pipeline is:

**User Query → Embedding Model → Vector DB (Schema Store) → Top-K Retrieval → LLM Prompt (System Instructions + Retrieved Schema Context + User Query) → SQL Output → Database Execution**

The critical component is the **Schema Vector Store**, which holds enriched descriptions of metadata (not actual data rows). This architecture moves beyond zero-shot Text-to-SQL by applying [[rag-for-database-schema]] to database metadata.

## Production Considerations

- **Few-Shot Prompting with [[golden-queries-few-shot]]**: Maintain a vector store of verified, complex SQL queries paired with natural language equivalents for complex analytical questions.
- **Human-in-the-Loop UI**: Never auto-execute generated SQL in production; require user confirmation before execution.
- **Feedback Loops**: Capture user edits/rejections to update the semantic layer or add corrected queries to golden query examples.

## Relationship to Existing Wiki

This architecture extends [[text2sql-patterns]] by providing a concrete production-ready pattern. It is complementary to [[duckdb-nsql-7b]] (fine-tuned approach) and [[semantic-sql-testing-benchmark]] (evaluation approach). The semantic layer is essentially a specialized [[context-store]] for database schema.