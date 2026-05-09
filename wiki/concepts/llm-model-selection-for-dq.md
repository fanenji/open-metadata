---
type: concept
title: LLM Model Selection for Data Quality Suggestions
created: 2026-03-19
updated: 2026-03-19
tags: [llm, model-selection, data-quality, openmetadata, ollama]
related: [openmetadata-ai-assistant, ollama-integration-pattern, mistral-small-4, qwen3.5-122b-a10b, dbt-osmosis-benchmarking, dbt-osmosis]
sources: ["Suggested Data Quality Tools.md"]
---
# LLM Model Selection for Data Quality Suggestions

This concept documents the task-specific LLM model selection for data quality (DQ) suggestion tasks, as distinct from documentation generation tasks like those in [[dbt-osmosis]].

## Task Characteristics

The DQ suggestion task maps to the **structured output/reasoning** category:
- Input: table schemas and metadata
- Output: structured test suggestions (e.g., "Column A should not be null")
- Requires: schema reasoning + domain understanding
- Does not require: pure SQL generation (unlike dbt-osmosis)

## Ollama-Compatible Rankings

Since [[openmetadata]] connects directly to Ollama (not via `llm.py`), only Ollama-compatible models are directly applicable.

### Small Models (14B–24B)

| Rank | Model | Notes |
|------|-------|-------|
| 1 | `devstral-small-2:24b-instruct-2512-fp16` | Best quality, slower (fp16) |
| 2 | `qwen2.5-coder:14b-instruct-q4_K_M` | Best speed/quality ratio |
| 3 | `deepseek-coder-v2:16b-lite-instruct-q4_K_M` | Solid alternative |

### Large Models (70B–123B)

| Model | Params | Architecture | Notes |
|-------|--------|-------------|-------|
| **Mistral-Small-4** | 119B total, 6B active | MoE (128 experts, 4 active) | 256k context, configurable reasoning, recommended for DQ |
| **Qwen3.5-122B-A10B** | 122B total, ~10B active | MoE | Recommended for dbt-osmosis |
| **Qwen3-72B** | 72B | Dense | Strong instruction following |
| **Llama 3.3 70B** | 70B | Dense | Reliable all-rounder |
| **Mistral-Large-2** | 123B | Dense | Excellent but slower |

## Recommended Split

- **OpenMetadata DQ suggestions** → [[mistral-small-4]]: 256k context handles large schemas, configurable reasoning for fast vs deep suggestions
- **dbt-osmosis documentation** → [[qwen3.5-122b-a10b]]: higher active params, stronger for structured JSON + SQL generation

## Practical Considerations

- **GPU requirements**: Large models (70B+) require significant GPU memory — verify hardware before deployment
- **MoE advantage**: Mixture-of-Experts models (Mistral-Small-4, Qwen3.5-122B-A10B) offer large model knowledge with fast inference (only a subset of parameters activate per token)
- **Configurable reasoning**: Mistral-Small-4 supports fast ↔ deep reasoning modes, adaptable to different latency/quality requirements
- **OpenMetadata compatibility**: Not all models may work equally well with OpenMetadata's Ollama integration — testing recommended