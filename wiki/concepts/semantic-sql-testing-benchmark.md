---
type: concept
title: Semantic SQL Testing Benchmark
created: 2026-04-29
updated: 2026-04-29
tags: [benchmark, sql-generation, llm-evaluation, semantic-model]
related: [llm-sql-generation-evaluation, dbt-testing-patterns, dbt-anomaly-detection-tests, djouallah]
sources: ["djouallah-semantic-sql-testing.md"]
---
# Semantic SQL Testing Benchmark

A reproducible benchmark methodology for evaluating Small Language Models (SLMs) on SQL generation tasks. The benchmark uses a well-defined semantic model (schema + measures + dimensions + anti-patterns + verified queries) to assess how accurately local LLMs can generate SQL from natural language questions.

## Methodology

1. **Semantic Model** — A detailed schema definition describing a TPC-DS star schema (store_sales, store_returns, date_dim, store, customer, item) with measures, dimensions, anti-patterns, and verified example queries
2. **20 Test Questions** — Ranging from simple aggregations to complex multi-year comparisons with return rates
3. **Local LLM Inference** — Models run locally via llama.cpp server, quantized to Q4_K_M (4-bit)
4. **Automated Judging** — Claude Opus generates the reference baseline; model outputs are validated by re-executing both SQLs against DuckDB and comparing results

## Evaluation Criteria

- **Exact result matching** — Every row must match (100% threshold); extra columns are counted as wrong. This is stricter than common text-based or execution-based metrics.
- **Numeric tolerance** — 0.5% relative tolerance for floating point aggregations
- **Raw vs feedback accuracy** — Reports both first-attempt accuracy and accuracy after self-correction via feedback loop

## Key Design Decisions

- **Never join fact tables directly** — Uses CTE pattern with FULL OUTER JOIN for combining sales and returns, avoiding anti-patterns
- **Feedback loop** — Models get a chance to self-correct their SQL after seeing initial results, measuring iterative improvement capability
- **Invisible baseline** — Reference answers are excluded from charts to avoid visual bias

## Connections to Existing Wiki

The benchmark methodology is related to [[dbt-testing-patterns]] and [[dbt-anomaly-detection-tests]] as an emerging pattern for LLM-generated SQL testing. The exact result matching approach complements existing SQL validation techniques used in dbt workflows.