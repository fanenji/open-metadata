---
type: concept
title: LLM Model Selection for Data Quality
created: 2026-02-13
updated: 2026-05-07
tags: [llm, model-selection, data-quality, sql, ollama, on-premise, test-generation]
related: [openmetadata-local-llm-integration, qwen-2-5-coder, llama-3-1, mistral-codestral, deepseek-coder-v2, ollama, llm-sql-generation-evaluation, openmetadata, data-quality-dimensions, dbt-testing-patterns, dbt-osmosis-llm-module]
sources: ["OpenMetadata for data quality.md", "Suggested Models (Gemini) - OLD.md"]
---
# LLM Model Selection for Data Quality

This page provides a decision framework for selecting open-source LLMs for data quality tasks, including test suggestion, SQL generation, and schema analysis. It synthesizes model comparison, hardware guidance, and selection criteria for using LLMs to generate data quality tests locally. All models listed are available via **Ollama** and can be used with [[openmetadata-local-llm-integration]].

## Core Task

The primary task is **LLM-based Data Quality Test Generation**: using a language model to automatically suggest data quality tests (e.g., SQL checks, dbt YAML tests) based on a table's schema and column names. For example, a model should infer that a column named `email` needs a regex validation check.

## Selection Criteria

The following dimensions are important when choosing a model for data quality tasks:

1. **SQL Proficiency:** The model's ability to write correct SQL syntax, understand complex joins, and generate valid dbt YAML.
2. **Reasoning Capabilities:** The model's ability to understand business context from column names and table comments, and infer what tests are appropriate.
3. **Context Window:** Maximum schema size the model can process in a single request.
4. **Hardware Requirements:** VRAM (or RAM for CPU) needed for reasonable inference speed.
5. **Enterprise Security:** Origin and licensing considerations for on-premise deployments.

The ideal model balances both SQL proficiency and reasoning capabilities.

## Model Rankings

### GPU Deployments

#### 1. Qwen 2.5 Coder (Recommended)

| Aspect | Detail |
|--------|--------|
| **Best Sizes** | 7B, 14B, 32B |
| **SQL Proficiency** | Excellent — specifically fine-tuned for code and SQL |
| **Context Window** | Up to 128K tokens |
| **Reasoning** | Strong — infers business logic (e.g., `net_revenue = gross - tax`) |
| **Hardware** | 7B: <16GB VRAM; 14B: 24GB; 32B: 48-80GB |
| **Pros** | Best SQL performance, large context, strong reasoning |
| **Cons** | Chinese origin (Alibaba) — may raise enterprise security concerns |

#### 2. Llama 3.1 (Safe Standard)

| Aspect | Detail |
|--------|--------|
| **Best Sizes** | 8B, 70B |
| **SQL Proficiency** | Good — general purpose, slightly less specialized than Qwen Coder |
| **Context Window** | 128K tokens |
| **Reasoning** | Excellent at understanding business context from table comments |
| **Hardware** | 8B: <16GB VRAM; 70B: 48-80GB |
| **Pros** | Best English NLP, widely supported, permissive license |
| **Cons** | No middle-ground size (8B to 70B jump), strict safety alignment |

#### 3. Mistral Codestral / Nemo

| Aspect | Detail |
|--------|--------|
| **Best Sizes** | Codestral 22B, Nemo 12B |
| **SQL Proficiency** | Very good — Codestral is code-specialized |
| **Context Window** | 32K tokens |
| **Reasoning** | Good — efficient models punch above their weight |
| **Hardware** | 12B: 24GB; 22B: 24GB (quantized) or 48GB |
| **Pros** | French origin (EU), efficient architecture |
| **Cons** | 22B is awkward for 24GB VRAM without quantization |

#### 4. DeepSeek-Coder V2

| Aspect | Detail |
|--------|--------|
| **Best Sizes** | 16B Lite, 230B full |
| **SQL Proficiency** | State-of-the-art — often beats GPT-4 on coding benchmarks |
| **Context Window** | Very large (128K+) |
| **Reasoning** | Excellent for code tasks |
| **Hardware** | 16B: 24-48GB; 230B: multi-GPU |
| **Pros** | SOTA coding performance, huge context |
| **Cons** | MoE architecture slower on older hardware, VRAM hungry, Chinese origin |

### CPU-Only Deployments

For environments without a GPU, the following smaller models can be used:

| Model | Size | RAM Required | Best For | Additional Notes |
|-------|------|--------------|----------|------------------|
| **Qwen 2.5 Coder** | 3B | ~2GB | Low-resource environments | Best overall CPU option |
| **Microsoft Phi-3.5 Mini** | 3.8B | ~2.5GB | Strong reasoning for its size | Excellent reasoning capabilities |
| **Llama 3.2** | 3B | ~2GB | Structured JSON output | Good for structured outputs |
| **Gemma 2** | 2B | ~1.5GB | Ultra-light hardware | Suitable for very old hardware |

## Hardware Guidance

### GPU VRAM Tiers

| VRAM Available | Recommended Models |
|----------------|-------------------|
| <16 GB (Consumer GPU) | Llama 3.1 8B, Qwen 2.5 Coder 7B |
| 24 GB (RTX 3090/4090, A10) | Qwen 2.5 Coder 14B, Mistral Nemo 12B, Codestral 22B (4-bit) |
| 48-80 GB (A6000, A100, H100) | Qwen 2.5 Coder 32B, Llama 3.1 70B |

### CPU RAM Tiers

| RAM Available | Recommended Models |
|---------------|-------------------|
| ~1.5GB | Gemma 2 2B |
| ~2GB | Qwen 2.5 Coder 3B, Llama 3.2 3B |
| ~2.5GB | Phi-3.5 Mini 3.8B |

## Deployment Assumptions

All models are assumed to be deployed via [[Ollama]]. They are available through the Ollama library and can be run with commands such as `ollama run qwen2.5-coder`.

## Caveats

- The top recommendation (Qwen) is from Alibaba, which may raise security concerns in some enterprise environments.
- The analysis is based on community consensus and general model benchmarks, not rigorous testing on the specific task of data quality test generation.
- The hardware guidance assumes Ollama's default quantization; actual memory requirements may vary.

## Related

- [[openmetadata-local-llm-integration]] — How these models are used with OpenMetadata.
- [[llm-sql-generation-evaluation]] — Approaches to evaluating LLM SQL generation quality.
- [[dbt-osmosis-llm-module]] — Similar LLM-assisted generation for dbt documentation.