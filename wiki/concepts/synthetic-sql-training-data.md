---
type: concept
title: Synthetic SQL Training Data
created: 2026-04-29
updated: 2026-04-29
tags: [synthetic-data, training-data, text2sql, llm, duckdb]
related: [duckdb-nsql-7b, numbers-station, text2sql-patterns, duckdb]
sources: ["Introducing DuckDB-NSQL-7B, A LLM for DuckDB SQL.md"]
---
# Synthetic SQL Training Data

Synthetic SQL training data refers to artificially generated SQL queries and their corresponding natural language descriptions, created to train text-to-SQL models. This approach is particularly valuable when real-world query logs are scarce, proprietary, or insufficiently diverse.

The [[DuckDB-NSQL-7B]] model exemplifies this methodology: approximately 200k DuckDB SQL queries were synthetically generated and validated, guided by the DuckDB documentation. This synthetic data was designed to cover DuckDB-specific syntax and features, including friendly SQL constructs (e.g., `ORDER BY ALL`, `GROUP BY ALL`), nested types, data import functions (e.g., `read_csv_auto`), and extension-specific queries (Postgres, SQLite, Iceberg, JSON, GeoSpatial).

Key characteristics of this approach include:
- **Documentation-guided generation**: The synthetic queries are derived from official documentation, ensuring coverage of documented features.
- **Validation**: Generated queries are validated to ensure syntactic correctness and semantic plausibility.
- **Domain specificity**: The synthetic data targets a specific SQL dialect (DuckDB), enabling the model to generate dialect-aware queries that general Text2SQL models may not produce correctly.

This technique addresses the challenge of training models for specialized SQL dialects where large-scale, high-quality training data does not naturally exist.