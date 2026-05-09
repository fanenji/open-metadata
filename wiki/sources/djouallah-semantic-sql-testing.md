---
type: source
title: "djouallah/semantic_sql_testing"
created: 2026-04-29
updated: 2026-04-29
tags: [benchmark, sql-generation, llm-evaluation, semantic-model]
related: [semantic-sql-testing-benchmark, llm-sql-generation-evaluation, dbt-testing-patterns]
sources: ["djouallah-semantic-sql-testing.md"]
---
# djouallah/semantic_sql_testing

A benchmark for Small Language Models (SLMs) on SQL generation tasks. It uses a well-defined semantic model with verified SQL queries and sample values to evaluate how accurately local LLMs can generate SQL from natural language questions.

## Results

[![Text to SQL: Duration vs Accuracy](https://github.com/djouallah/semantic_sql_testing/raw/main/chart.png)](https://github.com/djouallah/semantic_sql_testing/blob/main/chart.png)

## How It Works

1. **Semantic Model** — A detailed schema definition (`semantic_model.txt`) describing a TPC-DS star schema (store_sales, store_returns, date_dim, store, customer, item) with measures, dimensions, anti-patterns, and verified example queries
2. **20 Test Questions** — Ranging from simple aggregations to complex multi-year comparisons with return rates (`questions.json`)
3. **Local LLM Inference** — Models run locally via [llama.cpp](https://github.com/ggml-org/llama.cpp) server, quantized to Q4_K_M (4-bit)
4. **Automated Judging** — Claude Opus generates the reference baseline; model outputs are validated by re-executing both SQLs against DuckDB and comparing results with exact row matching and 0.5% numeric tolerance

## Hardware

- **GPU**: NVIDIA RTX 2000 Mobile (4GB VRAM)
- **RAM**: 32GB
- **Inference**: llama.cpp b8770

## Models Tested

| Model | Parameters | Type | Quantization |
| --- | --- | --- | --- |
| Qwen3.5-4B | 4B | Dense (GDN+MoE) | Q4_K_M |
| Qwen3-4B-Instruct-2507 | 4B | Dense | Q4_K_M |
| Gemma4-E4B | ~4B active (7.5B total) | MoE | Q4_K_M |

## Evaluation

- **Exact match** — every row must match (100% threshold); extra columns are counted as wrong
- **Raw vs feedback accuracy** — summary reports both first-attempt accuracy and accuracy after self-correction via feedback loop
- **Numeric tolerance** — 0.5% relative tolerance for floating point aggregations

## Key Design Decisions

- **Never join fact tables directly** — Uses CTE pattern with FULL OUTER JOIN for combining sales and returns
- **Feedback loop** — Models get a chance to self-correct their SQL after seeing initial results
- **Exact result matching** — Judging requires 100% row match per column (column order ignored, numeric tolerance applied)
- **Invisible baseline** — The reference answers are excluded from charts, only evaluated models are shown