---
type: source
title: Local LLM for OpenMetadata - Visual Studio Marketplace
created: 2026-04-08
updated: 2026-04-08
tags: [openmetadata, vs-code, llm, data-discovery, privacy]
related: [local-llm-openmetadata-extension, ollama, openmetadata-bot-authentication, openmetadata, data-discovery-tools, custom-connector-openmetadata]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
authors: [Markus Begerow]
year: 2025
url: "https://marketplace.visualstudio.com/items?itemName=MarkusBegerow.local-llm-chat-vscode-openmetadata"
venue: "Visual Studio Marketplace"
---
# Local LLM for OpenMetadata - Visual Studio Marketplace

A VS Code extension by [[Markus Begerow]] that enables AI-powered data discovery directly in the IDE by connecting to an [[openmetadata]] catalog. The extension supports three LLM provider options: OpenAI, [[ollama]] (local), and custom OpenAI-compatible endpoints (e.g., LM Studio, LocalAI, vLLM, Text Generation WebUI).

## Key Features

- **Multiple LLM Providers**: Switch between OpenAI, Ollama, and custom endpoints without code changes via the [[Unified LLM Service]] orchestration layer.
- **Privacy-by-Design**: Use local models with Ollama for fully offline, private data analysis — no metadata leaves the user's machine.
- **Natural Language Search**: Query the data catalog using conversational language (e.g., "show me customer tables").
- **Interactive Data Lineage**: Visualize upstream and downstream table relationships in an interactive graph.
- **Column Details**: Explore table schemas with expandable column information and AI-powered insights.

## Architecture

The extension uses a [[Unified LLM Service]] (`UnifiedLLMService.ts`) that orchestrates between OpenAI, Ollama, and custom endpoints, providing a unified interface for all LLM operations. The [[OpenMetadata Service]] (`OpenMetadataService.ts`) handles API communication with the OpenMetadata server, while the [[Lineage Service]] (`LineageService.ts`) manages data lineage visualization.

## Setup Requirements

1. A running OpenMetadata server (default: `http://localhost:8585`), typically deployed via the OpenMetadata Docker setup.
2. An LLM provider: OpenAI API key, Ollama installation with a pulled model, or any OpenAI-compatible endpoint.
3. A bot token from OpenMetadata (Settings → Bots → Add Bot → Generate Token) with the **Data Consumer** role assigned.

## Configuration

The extension is configured via VS Code settings JSON. Key settings include:

- `openmetadataExplorer.llm.provider`: `"openai"`, `"ollama"`, or `"custom"`
- `openmetadataExplorer.openmetadataUrl`: OpenMetadata server URL
- `openmetadataExplorer.openmetadataAuthToken`: Bot JWT token
- Provider-specific settings for API keys, endpoints, and model names

## LLM Provider Comparison

| Feature | OpenAI | Ollama | Custom |
|---------|--------|--------|--------|
| Speed | Fast (cloud) | Medium-Fast (local) | Varies |
| Privacy | Cloud-based | 100% Local | Depends |
| Cost | Pay-per-use | Free | Varies |
| Setup | API key only | Install + model | Varies |
| Offline | No | Yes | Depends |
| Quality | Excellent | Good | Varies |

## Current Status

Version 1.0.0 with 246 installs. Planned features include column-level lineage, data quality monitoring integration, advanced search filters, streaming responses, and multi-turn conversations.

## Connections to Wiki

- Strengthens [[openmetadata]] with a practical IDE-integrated interaction tool.
- Extends [[data-discovery-tools]] by demonstrating IDE-integrated discovery as an alternative to web-based catalogs.
- Related to [[custom-connector-openmetadata]] as a complementary pattern (chat interface vs. connector).
- Demonstrates [[openmetadata-bot-authentication]] pattern for programmatic access.