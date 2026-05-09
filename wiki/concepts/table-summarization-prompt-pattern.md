---
type: concept
title: Table Summarization Prompt Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [prompt-engineering, table-summarization, llm, text-to-sql]
related: [rag-for-table-selection, pinterest-text-to-sql-architecture, text2sql-patterns]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# Table Summarization Prompt Pattern

The Table Summarization Prompt Pattern is a technique for generating concise, informative summaries of database tables using LLMs. These summaries are used to enable semantic table search in RAG-based Text-to-SQL systems.

## Pinterest's Implementation

1. Retrieve the table schema from the metadata store.
2. Gather the most recent sample queries that utilize the table.
3. Incorporate as many sample queries as possible into the prompt (within context window limits), along with the table schema.
4. Forward the prompt to the LLM to generate a summary.
5. Generate and store embeddings in the vector store.

The table summary includes:
- Description of the table
- The data it contains
- Potential use scenarios

## Query Summarization

In addition to table summaries, individual historical queries are also summarized with:
- The query's purpose
- The tables utilized

## Importance

Table summaries are the primary documents in the vector index for NLP-based table search. They carry more weight than query summaries in the scoring strategy. The quality of these summaries directly impacts the search hit rate, which was shown to reach 90% with good documentation.