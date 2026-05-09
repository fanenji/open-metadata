---
type: entity
title: Local LLM for OpenMetadata Extension
created: 2026-04-08
updated: 2026-04-08
tags: [openmetadata, vs-code, llm, data-discovery]
related: [markus-begerow, openmetadata, ollama, openmetadata-bot-authentication, data-discovery-tools, custom-connector-openmetadata]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# Local LLM for OpenMetadata Extension

A Visual Studio Code extension by [[Markus Begerow]] that enables AI-powered data discovery directly in the IDE by connecting to an [[openmetadata]] catalog. The extension supports three LLM provider options: OpenAI, [[ollama]] (local), and custom OpenAI-compatible endpoints.

## Key Features

- **Multiple LLM Providers**: Switch between OpenAI, Ollama, and custom endpoints without code changes.
- **Privacy-by-Design**: Use local models with Ollama for fully offline, private data analysis.
- **Natural Language Search**: Query the data catalog using conversational language.
- **Interactive Data Lineage**: Visualize upstream and downstream table relationships.
- **Column Details**: Explore table schemas with expandable column information.

## Architecture

The extension uses a [[Unified LLM Service]] orchestration layer (`UnifiedLLMService.ts`) that abstracts across providers. The [[OpenMetadata Service]] handles API communication, and the [[Lineage Service]] manages lineage visualization. The frontend is built with React (`App.tsx`).

## Setup

Requires a running OpenMetadata server (localhost:8585), an LLM provider, and a bot token with the **Data Consumer** role. Configuration is done via VS Code settings JSON.

## Current Status

Version 1.0.0 with 246 installs. Planned features include column-level lineage, data quality monitoring, and multi-turn conversations.