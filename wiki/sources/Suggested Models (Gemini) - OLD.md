---
type: source
title: Suggested Models (Gemini) - OLD
created: 2026-01-15
updated: 2026-01-15
tags: [data-quality, llm, model-selection, ollama]
related: [llm-model-selection-for-data-quality, qwen-2-5-coder, ollama, openmetadata, llm-sql-generation-evaluation]
sources: ["Suggested Models (Gemini) - OLD.md"]
---
# Suggested Models (Gemini) - OLD

This source provides a practical guide for selecting open-source Large Language Models (LLMs) for local data quality test generation, specifically for use with Ollama and OpenMetadata. It ranks models based on their SQL proficiency, reasoning capabilities, and hardware requirements.

## Key Recommendations

- **Top Recommendation (GPU):** Qwen 2.5 Coder (14B or 32B) for the best balance of SQL expertise and schema reasoning.
- **Top Recommendation (CPU):** Qwen 2.5 Coder (3B) for its specialized code training and low resource footprint.
- **Safe Standard:** Llama 3.1 (8B or 70B) for general-purpose reasoning and broad ecosystem support.
- **Specialist:** DeepSeek-Coder V2 for state-of-the-art coding performance, though with higher complexity and latency.

## Hardware Guidance

The source provides a tiered hardware guide based on GPU VRAM:
- **< 16GB VRAM:** Llama 3.1 8B or Qwen 2.5 Coder 7B.
- **24GB VRAM:** Qwen 2.5 Coder 14B or Mistral Nemo 12B.
- **48GB - 80GB VRAM:** Qwen 2.5 Coder 32B.

For CPU-only deployments, models under 4B parameters are recommended, with Qwen 2.5 Coder 3B being the top choice.

## Key Concepts

- **LLM-based Data Quality Test Generation:** Using LLMs to automatically suggest data quality tests (e.g., SQL checks, dbt tests) based on schema and column names.
- **SQL Proficiency vs. Reasoning Capabilities:** The trade-off between a model's ability to write correct SQL syntax and its ability to understand business context and infer what to test.
- **Model Quantization:** Compressing model weights to fit in limited VRAM, enabling larger models on consumer hardware.
- **Mixture-of-Experts (MoE):** An architecture where only a subset of parameters is active per inference, offering efficiency but potentially higher latency.

## Caveats

- The source assumes Ollama as the deployment runtime.
- The top recommendation (Qwen) is from Alibaba, which may raise security concerns in some enterprise environments.
- The analysis is based on community consensus and general model benchmarks, not rigorous testing on the specific task of data quality test generation.