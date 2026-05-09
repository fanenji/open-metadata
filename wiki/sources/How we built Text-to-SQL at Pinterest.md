---
type: source
title: "How we built Text-to-SQL at Pinterest"
created: 2026-04-29
updated: 2026-04-29
tags: [text-to-sql, rag, pinterest, llm, sql-generation]
related: [text2sql-patterns, rag-for-table-selection, table-summarization-prompt-pattern, low-cardinality-column-handling, realistic-text-to-sql-benchmarks, llm-sql-generation-evaluation, pinterest-text-to-sql-architecture]
sources: ["How we built Text-to-SQL at Pinterest.md"]
authors: [Adam Obeng, J.C. Zhong, Charlie Gu]
year: 2024
url: "https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff"
venue: "Pinterest Engineering Blog"
---
# How we built Text-to-SQL at Pinterest

This blog post by Pinterest Engineering describes the design, implementation, and evaluation of a Text-to-SQL feature deployed in [[Querybook]], Pinterest's in-house open-source SQL query tool. The article covers two major iterations: a baseline LLM-based SQL generator and an enhanced version incorporating Retrieval-Augmented Generation (RAG) for table selection.

## Key Contributions

- **Production Text-to-SQL Architecture**: Detailed architecture including table schema retrieval, low-cardinality column handling, column pruning for context windows, and response streaming via WebSocket and Langchain.
- **RAG for Table Selection**: An offline pipeline generates vector embeddings of table summaries and historical query summaries, enabling NLP-based table search across hundreds of thousands of tables.
- **Table Re-selection**: An LLM re-ranks the top-N tables from vector search to the top-K most relevant tables before SQL generation.
- **Real-World Metrics**: Reports a 35% improvement in task completion speed (observational) and a first-shot acceptance rate increase from 20% to over 40%.
- **Critique of Existing Benchmarks**: Argues that benchmarks like Spider are unrealistic because they use a small number of pre-specified, well-normalized tables, whereas real-world problems involve many denormalized tables and require table search.

## Architecture

1. **Initial Version**: User selects tables → schema retrieved → prompt compiled → LLM generates SQL → streamed response.
2. **Second Version (RAG)**: Offline vector index of table and query summaries → user question embedded → similarity search → top-N tables → LLM re-selects top-K → user validates → standard Text-to-SQL.

## Evaluation & Learnings

- Table documentation quality is the highest-leverage factor: search hit rate without documentation = 40%, with documentation weight = 90%.
- Most queries require multiple human-AI iterations.
- Calls for more realistic benchmarks with denormalized tables and table search as a core task.

## Connections

- Extends [[text2sql-patterns]] with a production RAG-based architecture.
- Challenges [[llm-sql-generation-evaluation]] by arguing benchmarks are unrealistic.
- Related to [[duckdb-nsql-7b]] and [[semantic-sql-testing-benchmark]] as alternative approaches.
- Aligns with [[data-catalog-critique]] emphasis on embedded metadata quality.