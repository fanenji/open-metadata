---
type: entity
title: Qwen 2.5 Coder
created: 2026-05-07
updated: 2026-05-07
tags: [llm, model, alibaba, coding, sql]
related: [llm-model-selection-for-data-quality, ollama, openmetadata]
sources: ["Suggested Models (Gemini) - OLD.md"]
---
# Qwen 2.5 Coder

Qwen 2.5 Coder is a series of open-weight language models developed by Alibaba, specifically fine-tuned for code and SQL generation tasks. It is widely considered the current leader among open-source models for data engineering tasks, particularly for generating data quality tests.

## Model Sizes

The series is available in several sizes to suit different hardware profiles:
- **3B:** Optimized for CPU and low-resource deployments.
- **7B:** Suitable for consumer GPUs with less than 16GB VRAM.
- **14B:** Recommended for 24GB VRAM GPUs (e.g., RTX 3090/4090, A10).
- **32B:** The "sweet spot" for enterprise GPUs with 48GB-80GB VRAM (e.g., A6000, A100).
- **72B:** The flagship model, competing with GPT-4o and Claude 3.5 Sonnet for coding tasks.

## Key Strengths

- **SQL Expertise:** Fine-tuned for code and SQL, it understands complex joins and data types better than general-purpose models.
- **Large Context Window:** Supports up to 128k tokens, allowing it to process very large table schemas.
- **Reasoning:** Excellent at inferring business logic from column names (e.g., inferring that `net_revenue` should be `gross - tax`).

## Deployment

Available through Ollama via the tag `qwen2.5-coder`. It is the top recommendation for use with OpenMetadata for local data quality test generation.

## Caveats

- **Chinese Origin:** Some strict enterprise security policies may flag it due to its origin (Alibaba), though the weights are open.