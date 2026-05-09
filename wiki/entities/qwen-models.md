type: entity
title: Qwen Models
created: 2026-04-29
updated: 2026-04-29
tags: [llm, open-source, mixture-of-experts, local-inference]
related: [local-llm-for-bi-development, ollama, model-context-protocol]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
---
# Qwen Models

A family of open-weight large language models developed by Alibaba Cloud's Qwen team. The Qwen 3.5 and 3.6 series are particularly notable for their Mixture-of-Experts (MoE) architecture, which enables strong performance with relatively modest hardware requirements.

## Qwen 3.5–35B-A3B

- **Parameters:** 36B total, 3.3B active per token (MoE)
- **Context window:** 256K tokens native
- **Quantization:** Q4_K_M default (24GB download)
- **Release:** February 2026
- **Strengths:** Strong tool-calling support, competitive with GPT-4 class for coding and tool use
- **Hardware:** 48GB+ RAM recommended, GPU with 24GB+ VRAM optional

## Qwen 3.6–35B-A3B

- **Release:** Late April 2026
- **Focus:** Agentic coding stability improvements
- **Configuration:** Identical to Qwen 3.5 for setup purposes

## Context Window Configuration (Critical)

Ollama defaults to a 4K context window, which silently breaks tool calling for MCP-based workflows. The context must be explicitly expanded:

```bash
ollama run qwen3.5:35b-a3b
/set parameter num_ctx 32768
/save qwen3.5:35b-a3b-32k
/bye
```

## Performance Expectations

- **High-end GPU (RTX 4090, A6000):** 30–60 tokens/second
- **Apple Silicon M2/M3 Max/Ultra:** 20–40 tokens/second
- **Modern CPU only:** 3–8 tokens/second

## Smaller Variants

For lower-resource setups:
- `qwen3:8b` — 8B parameter model
- `qwen3.5:9b` — 9B parameter Qwen 3.5 variant

## See Also

- [[local-llm-for-bi-development]] — Architecture pattern using Qwen models
- [[ollama]] — The serving platform for Qwen models
- [[model-context-protocol]] — Protocol that Qwen models support via tool calling