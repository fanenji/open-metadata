---
type: source
title: Model Suggestions for llm.py
created: 2026-05-07
updated: 2026-05-07
tags: [llm, model-selection, ollama, dbt, documentation-generation]
related: [llm-py-model-selection, qwen3-5-27b, ollama-model-deployment, dbt-osmosis-llm-module, dbt-llm-documentation-generation]
sources: ["Model Suggestions for llm.py.md"]
---
# Model Suggestions for llm.py

This document provides a comprehensive model selection guide for the `llm.py` module, which performs two categories of tasks: structured JSON generation (model spec, staging spec, semantic analysis) and free-text generation (column/table descriptions, NL→SQL). The analysis is based on scanning the Ollama endpoint at `http://10.11.9.76:11434/v1`, which hosts 14 models.

## Key Findings

- **Best all-round model**: `qwen3.5:27b` (Q4_K_M recommended) — a dense next-generation model with hybrid Gated DeltaNet + Gated Attention + sparse MoE architecture. It excels at both structured JSON (IFEval 95% in thinking mode) and free-text documentation. Context window of 262K tokens is ideal for large dbt repositories.
- **Thinking mode**: Enabled by default on qwen3.5:27b. Improves accuracy for structured JSON (temperature 0.3) but adds latency for free-text tasks (temperature 0.5–0.7). Can be disabled via `/no_think` in the system prompt.
- **Best quality alternative**: `devstral-small-2:24b-instruct-2512-fp16` — Mistral's coding model at 24B in full fp16 precision, ideal for structured JSON and staging model specs but slower due to fp16.
- **Best speed/quality ratio**: `qwen2.5-coder:14b-instruct-q4_K_M` — fast and reliable for SQL and JSON output.
- **Models to avoid**: Several models are explicitly excluded for reasons including being embedding-only, OCR-specialized, Chinese-oriented, too small, or base (non-instruct) models.

## Task-Specific Configuration

| Task Type | Temperature | Thinking Mode | Recommended Model |
|---|---|---|---|
| Structured JSON generation | 0.3 | Enabled | qwen3.5:27b |
| Free-text generation | 0.5–0.7 | Disabled | qwen3.5:27b |

## Full Ranking

The document provides a ranked list of 7 viable models (ranks 3–9) with detailed notes on strengths and weaknesses, plus a list of 7 models to avoid. The ranking is based on benchmark scores (IFEval), architectural analysis, and practical considerations for dbt-related LLM tasks.

## Operational Notes

- Quantization: Q4_K_M recommended for qwen3.5:27b and qwen2.5-coder:14b, balancing quality and VRAM usage (~15 GB vs ~5 GB for MoE alternatives).
- The exact Ollama tag for qwen3.5:27b needs verification.
- The recommendation is based on benchmarks and architectural analysis, not empirical testing on the user's specific dbt repository.