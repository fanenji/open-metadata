---
type: source
title: "OpenMetadata for data quality"
created: 2026-02-13
updated: 2026-02-13
tags: [openmetadata, data-quality, llm, ollama, dremio, trino, duckdb, iceberg, dbt, datahub, soda-core, great-expectations, qwen, llama, mistral, deepseek]
related: [openmetadata, openmetadata-data-quality, openmetadata-local-llm-integration, openmetadata-dremio-connector-workaround, llm-model-selection-for-data-quality, openmetadata-vs-datahub-for-data-quality, dbt-expectations, data-catalog-tool-comparison, data-quality-dimensions, dbt-osmosis-llm-module, llm-sql-generation-evaluation, soda-core, great-expectations-for-data-contracts, ollama, qwen-2-5-coder, llama-3-1, mistral-codestral, deepseek-coder-v2]
sources: ["OpenMetadata for data quality.md"]
---
# OpenMetadata for data quality

A conversation (Gemini) evaluating open-source data quality tools for an on-premise Data Platform stack (Dremio/Trino/DuckDB, Iceberg, dbt, Kestra/Airflow, DataHub). The primary requirement is integration with a local LLM for suggesting quality tests, plus a dashboard and alerting.

## Summary

The conversation recommends **OpenMetadata** as the best fit because it natively integrates with **Ollama** for local LLM-based test suggestions, provides a built-in data quality dashboard, and supports alerting (Slack/Email/MS Teams). It can connect to Trino/DuckDB natively; for Dremio, a workaround via Trino or JDBC is needed. Alternative approaches include using **dbt-expectations + DataHub** with a custom LLM script, or **Soda Core** (which has native Dremio support but lacks a dashboard and LLM integration). The conversation also evaluates open-source LLMs for data quality tasks, ranking **Qwen 2.5 Coder** as the best for SQL, **Llama 3.1** as the safe enterprise standard, and **Mistral Codestral/Nemo** and **DeepSeek-Coder V2** as strong alternatives, with hardware guidance based on VRAM.

## Key Points

- OpenMetadata is the only tool offering native local LLM integration (via Ollama) for suggesting data quality tests out of the box.
- OpenMetadata lacks a dedicated Dremio connector; workaround via Trino or JDBC.
- OpenMetadata can ingest dbt artifacts for lineage and descriptions.
- dbt-expectations + DataHub + custom LLM script is a viable minimal-change alternative.
- Soda Core has native Dremio support but no built-in dashboard or LLM integration.
- Qwen 2.5 Coder (14B/32B) is recommended as the best open-source model for SQL/data quality tasks.
- Llama 3.1 is the safe enterprise standard for general NLP.
- Hardware requirements determine feasible model sizes (7B-8B for <16GB VRAM, 12B-14B for 24GB, 32B for 48GB+).

## Connections

- Strengthens [[openmetadata]] with specific data quality use case and local LLM integration details.
- Strengthens [[openmetadata-data-quality]] with deployment context and feature comparison.
- Validates [[dbt-expectations]] as a viable alternative within existing stack.
- Extends [[data-catalog-tool-comparison]] with local LLM integration as a new evaluation criterion.
- Related to [[dbt-osmosis-llm-module]] (similar pattern of LLM-assisted generation).
- Related to [[llm-sql-generation-evaluation]] (LLM models discussed are relevant to SQL generation).