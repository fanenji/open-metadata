---
type: entity
title: OpenMetadata Local LLM Integration
created: 2026-02-13
updated: 2026-02-13
tags: [openmetadata, llm, ollama, data-quality, ai-assistant]
related: [openmetadata, openmetadata-data-quality, ollama, qwen-2-5-coder, llama-3-1, mistral-codestral, deepseek-coder-v2, llm-model-selection-for-data-quality]
sources: ["OpenMetadata for data quality.md"]
---
# OpenMetadata Local LLM Integration

OpenMetadata's AI Assistant feature that connects to a local **Ollama** instance to scan table schemas and metadata, then suggests descriptions and data quality tests without any data leaving the infrastructure.

## How It Works

1. Deploy **Ollama** on-premise with a chosen model (e.g., Qwen 2.5 Coder, Llama 3.1).
2. Configure OpenMetadata to connect to the Ollama API endpoint.
3. OpenMetadata scans table schemas and sends them to the local LLM.
4. The LLM suggests data quality tests (e.g., "Column A should not be null", "Column B values should be between 1-100").
5. Users confirm or modify these tests in the OpenMetadata UI.
6. OpenMetadata schedules and runs the tests against connected query engines (Trino, DuckDB, etc.).

## Key Features

- **On-Premise Only:** No data leaves the infrastructure.
- **Schema-Aware:** The LLM receives column names, types, and descriptions to infer appropriate tests.
- **Interactive:** Users can accept, reject, or modify suggestions in the UI.
- **Extensible:** Supports any model available through Ollama.

## Recommended Models

See [[llm-model-selection-for-data-quality]] for a detailed comparison.

- **Qwen 2.5 Coder (14B/32B):** Best for SQL proficiency and reasoning.
- **Llama 3.1 (8B/70B):** Safe enterprise standard, strong at understanding business context.
- **Mistral Codestral (22B) / Nemo (12B):** Efficient code-specialized models.
- **DeepSeek-Coder V2 (16B Lite):** State-of-the-art coding, but heavier on VRAM.

## Hardware Requirements

| VRAM | Recommended Models |
|------|-------------------|
| <16 GB | Llama 3.1 8B, Qwen 2.5 Coder 7B |
| 24 GB | Qwen 2.5 Coder 14B, Mistral Nemo 12B |
| 48-80 GB | Qwen 2.5 Coder 32B |

## Related

- [[openmetadata-data-quality]] — The data quality module that uses these suggestions.
- [[dbt-osmosis-llm-module]] — Similar pattern of LLM-assisted documentation generation.
- [[llm-sql-generation-evaluation]] — Evaluation approaches for LLM SQL generation.