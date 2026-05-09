---
type: concept
title: DuckDB-NSQL-7B Prompt Template
created: 2026-05-07
updated: 2026-05-07
tags: [prompt-engineering, text2sql, duckdb, llm]
related: [duckdb-nsql-7b, huggingface-dataset-viewer-api, text2sql-patterns, duckdb]
sources: ["Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B.md"]
---
# DuckDB-NSQL-7B Prompt Template

A structured prompt format designed for the [[duckdb-nsql-7b]] model to generate DuckDB SQL from natural language questions. The template uses a three-part structure with instruction, schema context, and question.

## Template Structure

```
### Instruction:
Your task is to generate valid duckdb SQL to answer the following question.

### Input:
Here is the database schema that the SQL query will run on:
{ddl_create}

### Question:
{query_input}

### Response (use duckdb shorthand if possible):
```

## Components

- **`### Instruction`**: Fixed preamble defining the task (generate valid DuckDB SQL)
- **`### Input`**: Database schema as a `CREATE TABLE` DDL statement, inferred from the parquet file using DuckDB's `duckdb_tables()` function
- **`### Question`**: The user's natural language query
- **`### Response`**: The model's output, with a hint to use DuckDB shorthand

## Usage Pattern

1. Extract schema DDL from a single parquet row using DuckDB
2. Construct the prompt by filling `{ddl_create}` and `{query_input}`
3. Send to the model via llama.cpp or transformers pipeline
4. Post-process the output to replace `FROM data` with the actual parquet file URL

## Related

- [[text2sql-patterns]] — General Text2SQL pipeline patterns
- [[huggingface-dataset-viewer-api]] — Data source for schema extraction
