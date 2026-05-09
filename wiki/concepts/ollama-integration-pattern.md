---
type: concept
title: Ollama Integration Pattern for OpenMetadata
created: 2026-03-19
updated: 2026-03-19
tags: [openmetadata, ollama, llm, data-quality, integration]
related: [openmetadata, openmetadata-ai-assistant, llm-model-selection-for-dq, mistral-small-4, qwen3.5-122b-a10b]
sources: ["Suggested Data Quality Tools.md"]
---
# Ollama Integration Pattern for OpenMetadata

The Ollama Integration Pattern describes how [[openmetadata]] connects to local LLMs via Ollama to power its AI Assistant for data quality test suggestions. This pattern enables on-premise, private LLM inference without data leaving the infrastructure.

## Architecture

1. **Ollama server** runs on-premise, hosting one or more LLM models
2. **OpenMetadata** connects to the Ollama server via its UI settings (no custom middleware or `llm.py` required)
3. The AI Assistant sends schema metadata to the LLM, which returns suggested quality tests
4. Users review and confirm suggestions in the OpenMetadata UI

## Configuration

- OpenMetadata's UI settings specify the Ollama endpoint URL and model name
- Only Ollama-compatible models are directly supported (LM Studio requires custom base URL support)
- Recommended models: [[mistral-small-4]] for DQ suggestions, [[qwen3.5-122b-a10b]] for documentation generation

## Advantages

- **Zero new components**: OpenMetadata is already in the stack; Ollama is the only addition
- **Privacy**: All data stays on-premise
- **Simplicity**: No custom Python scripts or middleware needed
- **Flexibility**: Models can be swapped via Ollama without changing OpenMetadata configuration

## Limitations

- OpenMetadata's Ollama integration may not support all models equally — version constraints apply
- Large models (70B+) require significant GPU resources
- The integration is designed for structured output (test suggestions), not general chat

## Related Patterns

This pattern complements the [[dbt-osmosis-benchmarking]] approach, which uses LLMs for documentation generation. The two use cases benefit from different model selections, as documented in [[llm-model-selection-for-dq]].