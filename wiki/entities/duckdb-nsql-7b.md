---
type: entity
title: DuckDB-NSQL-7B
created: 2026-04-29
updated: 2026-05-07
tags: [duckdb, ai, llm, text2sql, model, open-source]
related: [duckdb, motherduck, hugging-face, text2sql-patterns, llm-sql-generation-evaluation, numbers-station, synthetic-sql-training-data]
sources: ["DuckDB-NSQL-7B Model.md", "Introducing DuckDB-NSQL-7B", "A LLM for DuckDB SQL.md"]
---
# DuckDB-NSQL-7B

**DuckDB-NSQL-7B** is a 7-billion-parameter language model fine-tuned for generating [[DuckDB]] SQL queries from natural language descriptions. Developed by [[MotherDuck]] in collaboration with [[Numbers Station]], it was released on January 25, 2024. The model acts as a "documentation oracle," producing exact DuckDB SQL and reducing the need to consult the official DuckDB documentation. The full model weights are hosted on [[Hugging Face]] at `motherduckdb/DuckDB-NSQL-7B-v0.1`.

## Training Data

The model was trained on approximately 200,000 synthetically generated and validated DuckDB SQL queries, guided by the DuckDB 0.9.2 documentation. In addition, over 250,000 general Text2SQL questions from Numbers Station's NSText2SQL dataset were used. The synthetic data covers DuckDB-specific features such as friendly SQL syntax (`ORDER BY ALL`, `GROUP BY ALL`), nested types, data import functions (`read_csv_auto`), and the extension ecosystem (Postgres, SQLite, Iceberg, JSON, GeoSpatial).

## Key Design Decisions

- **Small model trade-off**: The 7B parameter size was chosen deliberately to trade some expressivity for faster and less expensive inference compared to larger models (e.g., GPT-4).
- **DuckDB-specific awareness**: Unlike general Text2SQL models, DuckDB-NSQL-7B is aware of DuckDB's unique syntax and features, making it particularly useful for DuckDB users.
- **Quantized format**: The model is available in GGUF format for local execution via llama.cpp, enabling offline, low-latency inference.

## Availability and Integrations

- **Model Weights**: The full model (version 0.1) is available on Hugging Face at `motherduckdb/DuckDB-NSQL-7B-v0.1`. A quantized GGUF version is also hosted at `motherduckdb/DuckDB-NSQL-7B-v0.1-GGUF`.
- **Interactive Demo**: Try the model directly on Hugging Face Spaces; a companion Colab notebook is also provided for guided experimentation.
- **Source Code**: The training and inference code is open-sourced on GitHub under `NumbersStationAI/DuckDB-NSQL`.
- **Schema Discovery**: The model integrates with the Hugging Face Dataset Viewer API to automatically discover table schema from datasets, simplifying query generation.

## Limitations

- Version 0.1 — early-stage maturity, not production-ready.
- No published accuracy metrics or comparisons to other models.
- Specialized for DuckDB; not suitable for other SQL dialects without adaptation.
- The model was trained exclusively on DuckDB 0.9.2 syntax and is not maintained for later versions. Its performance on complex or edge-case queries has not been rigorously evaluated.

## Connections

- The model strengthens [[duckdb]]'s positioning as an AI-friendly query engine.
- It is a concrete implementation of the [[text2sql-patterns]] pipeline.
- Its evaluation approach contrasts with [[semantic-sql-testing-benchmark]], which assesses Small Language Models (SLMs) on SQL generation.
- Training leverages Numbers Station's [[NSText2SQL]] dataset and broader [[synthetic-sql-training-data]] generation techniques.