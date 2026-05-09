---
type: entity
title: Mistral-Small-4
created: 2026-03-19
updated: 2026-03-19
tags: [llm, model, mistral, moe, data-quality]
related: [llm-model-selection-for-dq, openmetadata-ai-assistant, ollama-integration-pattern, qwen3.5-122b-a10b]
sources: ["Suggested Data Quality Tools.md"]
---
# Mistral-Small-4

Mistral-Small-4 is a Mixture-of-Experts (MoE) language model by Mistral AI, recommended for [[openmetadata]] data quality suggestion tasks.

## Specifications

| Spec | Value |
|------|-------|
| Total parameters | 119B |
| Active parameters/token | 6B (8B with embeddings) |
| Architecture | MoE, 128 experts total, 4 active per token |
| Context window | 256k tokens |
| Reasoning | Configurable (fast ↔ deep) |
| Multimodal | Yes (text + image) |

## Use Case

Recommended as the primary model for [[openmetadata-ai-assistant]] DQ suggestions due to:
- Large context window (256k) for handling large schemas
- Configurable reasoning for adapting to latency/quality requirements
- MoE architecture providing large model knowledge with fast inference

## Deployment

Runs via Ollama for on-premise deployment. Requires significant GPU resources due to 119B total parameters, though active parameters per token are only 6B.

## Comparison

See [[llm-model-selection-for-dq]] for the full comparison with [[qwen3.5-122b-a10b]] and other models.