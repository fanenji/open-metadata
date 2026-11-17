---
type: source
title: "OpenMetadata for Data Quality — AI Studio Conversation"
created: 2026-07-15
updated: 2026-07-15
tags: [data-quality, openmetadata, ollama, llm, ai-assistant, datahub]
related: [data-quality, agentic-ai, mcp-server, ollama, data-quality-as-code, dbt-expectations]
authors: []
year: 2026
source_path: "[[raw/sources/OpenMetadata for data quality]]"
sources: ["https://aistudio.google.com/u/1/prompts/12pyOVNHefRrcRS5vjPsrwEwHKb3hi-Tr"]
venue: "Google AI Studio"
---
# OpenMetadata for Data Quality — AI Studio Conversation

A conversation on Google AI Studio (February 2026) where a user with a data platform (Dremio/Trino/DuckDB, Iceberg, dbt, DataHub) asks for an open-source, on-premises data quality tool with local LLM integration. The model recommends **OpenMetadata** as the primary solution, highlighting its native integration with Ollama for AI-suggested quality tests.

## Key Findings

- **OpenMetadata recommended over DataHub** for native LLM-based test suggestions via Ollama
- **AI Assistant** feature supports local LLMs (Llama 3, Mistral) through Ollama, keeping data on-premises
- **Native connectors** for Trino, Dremio, DuckDB — tests push computation to existing query engines
- **Built-in alerting** (Slack, Email, MS Teams) on test failure
- **Data Quality & Profiling dashboard** with test success/failure rates, history, and profile statistics
- **dbt + dbt-expectations + DataHub** presented as alternative but lacks native LLM suggestions

## Relevance

This source confirms OpenMetadata's positioning as an AI-augmented data quality platform with native [[ollama]] integration, bridging the [[agentic-ai]] vision with practical [[data-quality]] workflows.