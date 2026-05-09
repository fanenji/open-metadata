---
type: entity
title: Hugging Face Dataset Viewer API
created: 2026-05-07
updated: 2026-05-07
tags: [huggingface, api, dataset, parquet, data-access]
related: [duckdb, duckdb-nsql-7b, text2sql-patterns, duckdb-nsql-7b-prompt-template]
sources: ["Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B.md"]
---
# Hugging Face Dataset Viewer API

A REST API provided by Hugging Face that serves metadata and data access for over 120,000 datasets hosted on the Hub. It provides auto-converted parquet files, search, filter, and statistics endpoints.

## Key Features

- **Parquet file access**: Each dataset's splits are automatically converted to parquet files, accessible via a REST endpoint at `https://huggingface.co/api/datasets/{dataset}/parquet`
- **Search API**: Text search across dataset rows at `https://datasets-server.huggingface.co/search`
- **Filter API**: SQL-like filtering at `https://datasets-server.huggingface.co/filter`
- **Metadata endpoints**: Dataset splits, column names, data types, size, and statistics

## Usage in Text2SQL Pipeline

The API serves as the data source for the [[duckdb-nsql-7b]] Text2SQL pipeline. The parquet file URL is used directly in DuckDB queries, enabling schema inference and SQL execution without downloading the full dataset.

## Related

- [[duckdb-nsql-7b-prompt-template]] — The prompt structure used with this API
- [[text2sql-patterns]] — General Text2SQL pipeline patterns
