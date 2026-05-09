---
type: source
title: DuckDB-NSQL-7B Model
created: 2026-01-15
updated: 2026-04-29
tags: [duckdb, ai, text2sql, llm]
related: [duckdb, duckdb-nsql-7b, text2sql-patterns, llm-sql-generation-evaluation, semantic-sql-testing-benchmark]
sources: ["DuckDB-NSQL-7B Model.md"]
authors: [MotherDuck]
year: 2026
url: "https://huggingface.co/blog/duckdb-nsql-7b"
venue: "Hugging Face Blog"
---
# DuckDB-NSQL-7B Model

A blog post introducing DuckDB-NSQL-7B, a fine-tuned 7B-parameter language model for Text2SQL generation specialized for the DuckDB SQL dialect. The model is hosted on Hugging Face by MotherDuck and demonstrated via a Colab notebook and a Hugging Face Space.

## Summary

The source presents a pipeline for natural language querying of datasets hosted on Hugging Face. The pipeline combines schema discovery via the Hugging Face Dataset Viewer API with DuckDB-specific SQL generation using the DuckDB-NSQL-7B model. A working Colab notebook and a Hugging Face Space demonstrate the approach end-to-end.

## Key Claims

- DuckDB-NSQL-7B enables natural language querying of Hugging Face datasets.
- The model is specialized for DuckDB SQL dialect, leveraging DuckDB's functions and syntax.
- The pipeline uses the Dataset Viewer API for automatic schema discovery.

## Limitations

- The model is version 0.1, indicating early-stage maturity.
- No accuracy metrics or comparisons to other models are provided.
- The source is a blog post with a demo, not a formal evaluation.

## Connections

- Directly related to [[duckdb]] as the target SQL dialect.
- Related to [[llm-sql-generation-evaluation]] and [[semantic-sql-testing-benchmark]] as another approach to LLM-based SQL generation.
- Tangentially related to [[dbt-mcp-server]] as another AI-driven data access pattern.