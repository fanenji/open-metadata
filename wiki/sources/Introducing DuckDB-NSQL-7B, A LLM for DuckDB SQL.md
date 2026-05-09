---
type: source
title: "Introducing DuckDB-NSQL-7B, A LLM for DuckDB SQL"
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, text2sql, llm, ai, synthetic-data]
related: [duckdb-nsql-7b, numbers-station, synthetic-sql-training-data, text2sql-patterns, duckdb]
sources: ["Introducing DuckDB-NSQL-7B, A LLM for DuckDB SQL.md"]
authors: [MotherDuck]
year: 2024
url: "https://motherduck.com/blog/duckdb-text2sql-llm/"
venue: MotherDuck Blog
---
# Introducing DuckDB-NSQL-7B, A LLM for DuckDB SQL

This blog post from MotherDuck (published January 25, 2024) announces the release of DuckDB-NSQL-7B, a fine-tuned 7B-parameter language model specialized for generating DuckDB SQL queries from natural language. Developed in collaboration with [[Numbers Station]], the model is trained on approximately 200k synthetically generated and validated DuckDB SQL queries guided by the DuckDB documentation, plus over 250k general Text2SQL questions from Numbers Station's NSText2SQL dataset.

The model's key differentiator is its awareness of DuckDB-specific syntax and features, including friendly SQL (e.g., `ORDER BY ALL`, `GROUP BY ALL`), nested types, varied data import options (e.g., `read_csv_auto`), and the extension ecosystem (Postgres, SQLite, Iceberg, JSON, GeoSpatial). The authors frame the model as a "documentation oracle" that reduces the need to consult DuckDB documentation while writing queries.

The model weights are released on Hugging Face in both full and quantized GGUF formats (for use with llama.cpp). A Hugging Face space provides an interactive demo, powered by an OctoAI endpoint. The source notes that MotherDuck already provides text-to-SQL functionality using OpenAI's most powerful models, but DuckDB-NSQL-7B targets lower-latency, less expensive inference by trading off some expressivity through a smaller model size.

The source is a blog post announcement, not a rigorous evaluation paper. No benchmark results or accuracy metrics are provided. The claims about DuckDB feature awareness are plausible but unvalidated in this document.