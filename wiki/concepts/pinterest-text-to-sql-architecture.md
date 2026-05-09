---
type: concept
title: Pinterest Text-to-SQL Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [text-to-sql, architecture, pinterest, rag]
related: [text2sql-patterns, rag-for-table-selection, table-summarization-prompt-pattern, low-cardinality-column-handling, querybook, pinterest-engineering]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# Pinterest Text-to-SQL Architecture

The Pinterest Text-to-SQL architecture is a production system deployed in [[Querybook]] that converts natural language analytical questions into SQL queries. It evolved through two major iterations.

## Initial Version

1. User selects tables and asks an analytical question.
2. Table schemas are retrieved from the metadata store (table name, description, columns, types, descriptions).
3. Low-cardinality column values are incorporated into the schema for precise WHERE clauses.
4. Column pruning excludes tagged columns to fit context window limits.
5. A prompt is compiled with the question, SQL dialect, and schemas.
6. The LLM generates SQL, streamed via WebSocket using [[Langchain]] for JSON parsing.

## Second Version (RAG-Enhanced)

1. An offline job creates a vector index of table summaries and historical query summaries.
2. If no tables are specified, the user's question is embedded and similarity-searched against the vector index (using [[OpenSearch]]).
3. Top-N tables are retrieved and passed to an LLM for re-selection to top-K.
4. The user validates the selected tables.
5. Standard Text-to-SQL proceeds with confirmed tables.

## Key Techniques

- **Low-cardinality column handling**: Unique values of low-cardinality columns are included in the schema to prevent incorrect filter values.
- **Column pruning**: Tagged columns are excluded from the schema to manage context window limits.
- **Table summarization**: LLM generates summaries of tables using schema + sample queries.
- **Query summarization**: LLM summarizes historical queries with purpose and tables used.
- **Table re-selection**: LLM re-ranks top-N to top-K based on question + summaries.

## Evaluation

- First-shot acceptance rate: 20% → 40% over time.
- Task completion speed improvement: 35% (observational).
- Table documentation is critical: hit rate without docs = 40%, with docs = 90%.
- Most queries require multiple human-AI iterations.