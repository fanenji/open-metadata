---
type: entity
title: Ollama
created: 2026-07-15
updated: 2026-07-15
tags: [llm, ai, local-models, open-source, on-premises]
related: [agentic-ai, mcp-server, openmetadata]
sources: ["https://aistudio.google.com/u/1/prompts/12pyOVNHefRrcRS5vjPsrwEwHKb3hi-Tr"]
---

# Ollama

An open-source tool for running large language models (LLMs) locally on your own infrastructure. Ollama supports models like Llama 3, Mistral, and others, enabling on-premises AI without sending data to cloud APIs.

## Role in OpenMetadata

OpenMetadata's **AI Assistant** feature integrates with Ollama to provide local LLM-powered suggestions for:
- Data quality test generation (e.g., "Column A should not be null")
- Column and table descriptions
- Schema analysis

This integration allows organizations to leverage AI for metadata enrichment and quality test suggestions while keeping all data on-premises — a key differentiator from DataHub and other catalog tools.