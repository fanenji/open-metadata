---
type: concept
title: llm.py Model Selection
created: 2026-05-07
updated: 2026-05-07
tags: [llm, model-selection, task-categorization, configuration, dbt]
related: [qwen3-5-27b, ollama-model-deployment, dbt-osmosis-llm-module, dbt-llm-documentation-generation, llm-sql-generation-evaluation]
sources: ["Model Suggestions for llm.py.md"]
---
# llm.py Model Selection

A framework for selecting and configuring language models for the `llm.py` module, which performs two distinct task categories with different requirements. This framework provides concrete model recommendations, temperature settings, and thinking mode configuration for dbt-related LLM tasks.

## Task Categories

### 1. Structured JSON Generation
- **Tasks**: Model spec, staging spec, semantic analysis
- **Requirements**: High instruction-following accuracy
- **Temperature**: 0.3
- **Thinking Mode**: Enabled (improves accuracy)

### 2. Free-Text Generation
- **Tasks**: Column/table descriptions, NL→SQL
- **Requirements**: Good SQL/dbt context understanding
- **Temperature**: 0.5–0.7
- **Thinking Mode**: Disabled (reduces latency)

## Recommended Model Hierarchy

| Priority | Model | Use Case |
|---|---|---|
| Primary | `qwen3.5:27b` (Q4_K_M) | All tasks — best all-round |
| Coding-focused | `devstral-small-2:24b-instruct-2512-fp16` | Structured JSON, staging spec |
| Speed/quality | `qwen2.5-coder:14b-instruct-q4_K_M` | SQL, JSON output |
| Solid alternative | `deepseek-coder-v2:16b-lite-instruct-q4_K_M` | SQL, staging transforms |

## Configuration Principles

1. **Task-specific temperature**: Structured JSON at 0.3, free-text at 0.5–0.7.
2. **Thinking mode toggle**: Enable for structured tasks, disable for free-text to manage latency.
3. **Quantization**: Q4_K_M recommended for balancing quality and VRAM.
4. **Single model strategy**: qwen3.5:27b covers all tasks, avoiding model switching overhead.

## Connection to Existing Patterns

This framework directly supports the [[dbt-osmosis-llm-module]] workflow by providing concrete model recommendations and configuration guidance. It also extends the [[dbt-llm-documentation-generation]] pattern with operational details about model selection and task-specific configuration. The task categorization aligns with the [[llm-sql-generation-evaluation]] framework's distinction between execution match and semantic match evaluation approaches.

## Open Questions

- Has qwen3.5:27b been empirically tested on the user's specific dbt repository and task mix?
- Is the Ollama endpoint stable and performant enough for production use?
- What is the exact Ollama tag for qwen3.5:27b?