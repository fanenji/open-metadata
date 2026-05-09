---
type: entity
title: Ollama Model Deployment
created: 2026-05-07
updated: 2026-05-07
tags: [llm, infrastructure, deployment, ollama, model-serving]
related: [llm-py-model-selection, qwen3-5-27b, dbt-osmosis-llm-module, dbt-llm-documentation-generation]
sources: ["Model Suggestions for llm.py.md"]
---
# Ollama Model Deployment

The local LLM serving infrastructure for the Data Platform, hosted at `http://10.11.9.76:11434/v1`. This endpoint serves 14 models and is the primary inference backend for the [[llm-py-model-selection]] framework.

## Endpoint Configuration

```bash
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://10.11.9.76:11434/v1
OLLAMA_API_KEY=ollama
```

## Recommended Models

| Model | Quantization | VRAM | Best For |
|---|---|---|---|
| `qwen3.5:27b` | Q4_K_M | ~15 GB | All tasks (primary) |
| `devstral-small-2:24b-instruct-2512-fp16` | fp16 | ~48 GB | Structured JSON, coding |
| `qwen2.5-coder:14b-instruct-q4_K_M` | Q4_K_M | ~8 GB | SQL, JSON (speed/quality) |
| `deepseek-coder-v2:16b-lite-instruct-q4_K_M` | Q4_K_M | ~9 GB | SQL, staging transforms |

## Quantization Strategy

- **Q4_K_M**: Recommended for most models. Balances quality and VRAM usage.
- **fp16**: Highest quality but significantly slower and more memory-intensive. Only recommended for `devstral-small-2:24b-instruct-2512-fp16` when maximum quality is required for coding tasks.

## Models to Avoid

The following models are explicitly excluded from llm.py usage:

| Model | Reason |
|---|---|
| `text-embedding-nomic-embed-text-v1.5` | Embedding model — not generative |
| `deepseek-ocr:latest` | Specialized for OCR |
| `glm-4.7-flash:latest` | Primarily Chinese-language oriented |
| `gemma3:4b-it-fp16` | Too small (4B) for reliable structured JSON |
| `gemma2:9b` | Too small for complex instruction following |
| `qwen/qwen3-4b-thinking-2507` | 4B thinking model — slow and too small |
| `codegemma:7b-code-q4_K_M` | Base (non-instruct) model |

## Operational Notes

- The exact Ollama tag for `qwen3.5:27b` needs verification.
- The endpoint stability and performance for production use with recommended models has not been empirically validated.
- VRAM requirements are approximate and depend on concurrent request handling.