---
type: concept
title: Text2SQL Patterns
created: 2026-04-29
updated: 2026-04-29
tags: [ai, llm, sql, text2sql, data-access]
related: [duckdb-nsql-7b, llm-sql-generation-evaluation, semantic-sql-testing-benchmark, duckdb]
sources: ["DuckDB-NSQL-7B Model.md"]
---
# Text2SQL Patterns

Text2SQL is the task of converting natural language questions into SQL queries. This concept page documents the general pipeline pattern for AI-assisted data querying, as exemplified by the [[DuckDB-NSQL-7B]] model.

## Pipeline Architecture

A typical Text2SQL pipeline consists of three stages:

1. **Schema Discovery** — Automatically retrieve the schema (table names, column names, data types) of the target database or dataset. In the DuckDB-NSQL-7B example, this is done via the Hugging Face Dataset Viewer API.
2. **SQL Generation** — Use an LLM to generate a SQL query from the natural language question and the discovered schema. The model is specialized for a specific SQL dialect (e.g., DuckDB).
3. **Execution** — Run the generated SQL query against the database and return results to the user.

## Considerations

- **Schema context** — Providing accurate and complete schema information is critical for correct SQL generation.
- **Dialect specialization** — Models fine-tuned for a specific SQL dialect (e.g., DuckDB, PostgreSQL) tend to produce more accurate queries than general-purpose models.
- **Evaluation** — Text2SQL systems should be evaluated on execution match (does the query return correct results?) rather than text match (does the query look like the expected SQL?).

## Connections

- [[duckdb-nsql-7b]] is a concrete implementation of this pattern.
- [[llm-sql-generation-evaluation]] discusses evaluation approaches for Text2SQL.
- [[semantic-sql-testing-benchmark]] provides a benchmark for evaluating SQL generation from Small Language Models.