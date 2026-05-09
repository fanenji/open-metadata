---
type: source
title: Suggested Data Quality Tools
created: 2026-03-19
updated: 2026-03-19
tags: [data-quality, llm, openmetadata, dbt, ollama]
related: [openmetadata, openmetadata-data-quality, openmetadata-ai-assistant, openmetadata-dq-dashboard, ollama-integration-pattern, llm-model-selection-for-dq, mistral-small-4, qwen3.5-122b-a10b, dbt-expectations, datahub, dbt-osmosis, dbt-osmosis-benchmarking, data-quality-dimensions]
sources: ["Suggested Data Quality Tools.md"]
---
# Suggested Data Quality Tools

This source is a composite of two AI conversations (Gemini and Claude) evaluating data quality tools for an on-premise, open-source data platform. The stack includes Dremio/Trino/DuckDB, Iceberg, dbt, Kestra/Airflow, and DataHub.

The Gemini conversation recommends **OpenMetadata** as the best fit, citing its native Ollama integration for local LLM-based DQ test suggestions, built-in dashboard, and alerting. It compares OpenMetadata against dbt + DataHub and Great Expectations.

The Claude conversation confirms OpenMetadata is already in the stack and recommends activating its Data Quality module. It provides detailed LLM model selection guidance for the DQ suggestion task, evaluating models in the 14B–123B range, including MoE architectures like Mistral-Small-4 and Qwen3.5-122B-A10B. It recommends a split: Mistral-Small-4 for OpenMetadata DQ suggestions, Qwen3.5-122B-A10B for dbt-osmosis documentation generation.

Key findings: OpenMetadata is the only open-source, on-premise tool with native local LLM integration for DQ suggestions. No new components are needed — activating existing OpenMetadata features covers all requirements.