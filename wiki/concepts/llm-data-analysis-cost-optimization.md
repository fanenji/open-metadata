---
type: concept
title: LLM Data Analysis Cost Optimization
created: 2026-05-06
updated: 2026-05-06
tags: [llm, data-analysis, cost-optimization, architecture]
related: [llm-assisted-data-recipes, chat-with-data-patterns, matthew-harris]
sources: ["Reframing LLM 'Chat with Data' Introducing LLM-Assisted Data Recipes.md"]
---
# LLM Data Analysis Cost Optimization

Patterns and strategies for reducing the cost of using Large Language Models (LLMs) for data analysis workflows. The primary challenge is that powerful LLMs needed for high-quality code generation are expensive, and iterative debugging processes burn through tokens rapidly.

## Key Strategies

### Two-Stream Architecture
The [[llm-assisted-data-recipes]] methodology splits the workflow into:
- **Low-volume/high-cost stream**: Powerful LLMs + human review for recipe creation
- **High-volume/low-cost stream**: Weaker LLMs, no code generation, deterministic execution

### Memory Hierarchy
- **Facts**: Cached answers to specific questions avoid repeat LLM calls
- **Skills**: Generalized reusable recipes that can be applied to new but similar queries

### Asynchronous Data Refresh
Preemptive execution of recipes on schedules pre-populates the cache, reducing real-time LLM usage.

### Code Generation vs. Data Passing
Having the LLM generate code (e.g., Python to count records) requires far fewer tokens than passing raw data through the LLM for summarization.

## Trade-offs
- Recipe creation introduces a delay for new requests
- Asynchronous refresh may be costly for large data volumes
- Human-in-the-loop review creates a bottleneck but ensures quality and safety
