---
type: source
title: "Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B"
created: 2026-05-07
updated: 2026-05-07
tags: [text2sql, duckdb, llm, huggingface, prompt-engineering]
related: [duckdb-nsql-7b, huggingface-dataset-viewer-api, duckdb-nsql-7b-prompt-template, text2sql-patterns, duckdb, llama-cpp]
sources: ["Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B.md"]
authors: [Andrea Soria, Till Döhmen, Sen Wu, Laurel Orr, Vishal]
year: 2024
url: "https://huggingface.co/blog/duckdb-nsql-7b"
venue: "Hugging Face Blog"
---
# Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B

A tutorial demonstrating an end-to-end pipeline for converting natural language questions into DuckDB SQL queries using the DuckDB-NSQL-7B model, the Hugging Face Dataset Viewer API for parquet file access, and DuckDB for schema extraction and query execution.

## Summary

The article presents a practical approach to Text2SQL generation that enables non-technical users to query datasets using plain language. The pipeline consists of four steps: (1) schema extraction from a Hugging Face dataset's parquet file using DuckDB, (2) prompt construction using a structured template with instruction, schema DDL, and question, (3) SQL generation using the quantized DuckDB-NSQL-7B model via llama.cpp, and (4) SQL execution against the parquet file using DuckDB. The demo uses the world-cities-geo dataset and validates results against the Hugging Face dataset viewer's search and filter APIs.

## Key Contributions

- Reusable pipeline pattern: schema extraction → prompt construction → model inference → SQL execution → result validation
- Structured prompt template for DuckDB SQL generation with `### Instruction`, `### Input`, `### Question`, and `### Response` sections
- Technique for inferring CREATE TABLE DDL from a single parquet row using DuckDB's `duckdb_tables()` function
- Integration of Hugging Face's auto-converted parquet files as a data source for LLM-powered querying

## Connections

- Strengthens [[duckdb-nsql-7b]] with concrete usage patterns and prompt structure
- Extends [[text2sql-patterns]] with a specific implementation
- Introduces [[huggingface-dataset-viewer-api]] as a reusable data access pattern
- Documents [[duckdb-nsql-7b-prompt-template]] as a reusable prompt format
