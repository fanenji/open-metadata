---
type: concept
title: RAG for Table Selection
created: 2026-04-29
updated: 2026-04-29
tags: [rag, table-selection, text-to-sql, retrieval]
related: [pinterest-text-to-sql-architecture, table-summarization-prompt-pattern, text2sql-patterns, opensearch]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# RAG for Table Selection

RAG for Table Selection is a pattern for using Retrieval-Augmented Generation to identify relevant database tables from a large corpus (hundreds of thousands) when generating SQL from natural language. This addresses the real-world challenge that users often don't know which tables contain the data they need.

## Pinterest's Implementation

1. **Offline Vector Index Creation**: An offline job generates embeddings for:
   - **Table summaries**: LLM-generated descriptions of tables using schema + sample queries.
   - **Query summaries**: LLM-generated summaries of historical queries with purpose and tables used.
2. **Similarity Search**: The user's question is embedded and searched against the vector index using [[OpenSearch]].
3. **Scoring Strategy**: Table summaries carry more weight than query summaries. Multiple occurrences of a table are aggregated.
4. **Table Re-selection**: An LLM re-ranks the top-N tables to top-K by evaluating the question alongside table summaries.

## Key Findings

- Table documentation quality is the highest-leverage factor: hit rate without documentation = 40%, with documentation weight = 90%.
- The NLP-based table search is also used in general table search in [[Querybook]], not just Text-to-SQL.

## Future Improvements

- Include additional metadata (tiering, tags, domains) for refined filtering.
- Implement scheduled or real-time index updates.
- Fine-tune similarity search and scoring strategies.