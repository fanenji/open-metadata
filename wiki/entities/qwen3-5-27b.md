---
type: entity
title: qwen3.5:27b
created: 2026-05-07
updated: 2026-05-07
tags: [llm, model, ollama, text2sql, documentation-generation]
related: [llm-py-model-selection, ollama-model-deployment, dbt-osmosis-llm-module, dbt-llm-documentation-generation, duckdb-nsql-7b]
sources: ["Model Suggestions for llm.py.md"]
---
# qwen3.5:27b

A dense next-generation language model with a hybrid architecture combining Gated DeltaNet, Gated Attention, and sparse Mixture of Experts (MoE). It is the recommended primary model for all tasks in the [[llm-py-model-selection]] framework, running on the local [[ollama-model-deployment]] infrastructure.

## Key Specifications

- **Parameters**: 27B (dense hybrid architecture)
- **Architecture**: Gated DeltaNet + Gated Attention + sparse MoE
- **Context Window**: 262K tokens
- **Quantization**: Q4_K_M recommended (balances quality and VRAM at ~15 GB)
- **Benchmark**: IFEval 95% in thinking mode

## Capabilities

- **Structured JSON generation**: Excellent for model spec, staging spec, and semantic analysis tasks. Thinking mode improves accuracy.
- **Free-text generation**: Strong for column/table descriptions and NL→SQL tasks. Thinking mode can be disabled to reduce latency.
- **Large context handling**: 262K token context window is ideal for large dbt repositories.

## Configuration

```bash
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://10.11.9.76:11434/v1
OLLAMA_API_KEY=ollama
OLLAMA_MODEL=qwen3.5:27b
```

### Thinking Mode Management

- **Structured JSON (temperature 0.3)**: Keep thinking mode enabled for maximum accuracy.
- **Free-text / NL docs (temperature 0.5–0.7)**: Disable thinking mode by adding `/no_think` to the system prompt to reduce latency.

## Comparison with Alternatives

- **vs qwen3-coder-30b**: qwen3-coder-30B has only 3.3B active parameters (sparse MoE), making it faster and lighter (~5 GB VRAM) but weaker on free-text NL tasks. Qwen3.5-27B is slower (~15 GB VRAM in Q4) but covers all llm.py requirements with superior quality.
- **vs devstral-small-2:24b-instruct-2512-fp16**: devstral-small-2 is a coding-focused alternative in full fp16 precision, offering higher quality for structured JSON but slower performance.
- **vs qwen2.5-coder:14b-instruct-q4_K_M**: The 14B coder offers better speed/quality ratio for SQL and JSON output but lower overall capability.

## Limitations

- The recommendation is based on benchmarks and architectural analysis, not empirical testing on the user's specific dbt repository.
- The exact Ollama tag needs verification.
- Requires ~15 GB VRAM in Q4_K_M quantization.