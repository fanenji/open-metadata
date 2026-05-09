---
type: entity
title: Qwen3.5-122B-A10B
created: 2026-03-19
updated: 2026-03-19
tags: [llm, model, qwen, moe, documentation]
related: [llm-model-selection-for-dq, dbt-osmosis, dbt-osmosis-benchmarking, mistral-small-4]
sources: ["Suggested Data Quality Tools.md"]
---
# Qwen3.5-122B-A10B

Qwen3.5-122B-A10B is a Mixture-of-Experts (MoE) language model by Alibaba's Qwen team, recommended for [[dbt-osmosis]] documentation generation tasks.

## Specifications

| Spec | Value |
|------|-------|
| Total parameters | 122B |
| Active parameters/token | ~10B |
| Architecture | MoE |
| Context window | ~32k tokens |

## Use Case

Recommended as the primary model for [[dbt-osmosis]] documentation generation due to:
- Higher active parameters (~10B) for stronger structured JSON and SQL generation
- MoE architecture providing large model knowledge with fast inference

## Deployment

Runs via Ollama for on-premise deployment. Requires significant GPU resources.

## Comparison

See [[llm-model-selection-for-dq]] for the full comparison with [[mistral-small-4]] and other models. The recommended split is Qwen3.5-122B-A10B for dbt-osmosis and Mistral-Small-4 for OpenMetadata DQ suggestions.