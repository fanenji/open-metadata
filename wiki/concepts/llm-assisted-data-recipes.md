---
type: concept
title: LLM-Assisted Data Recipes
created: 2026-05-06
updated: 2026-05-06
tags: [llm, data-analysis, architecture, data-recipes]
related: [matthew-harris, chat-with-data-patterns, llm-data-analysis-cost-optimization, llm-sql-generation-evaluation, text2sql-patterns, dbt-mcp-server]
sources: ["Reframing LLM 'Chat with Data' Introducing LLM-Assisted Data Recipes.md"]
---
# LLM-Assisted Data Recipes

A methodology proposed by [[Matthew Harris]] for conversational data analysis that addresses the limitations of existing [[chat-with-data-patterns]]. Data Recipes are reusable, human-reviewed code snippets (with data) generated conversationally via LLM, stored in a library for deterministic, transparent data analysis.

## Two-Stream Architecture

The core innovation splits the workflow into two streams:

1. **Recipes Assistant (Stream 1)**: Low-volume, high-cost stream using powerful LLM agents to generate code snippets (recipes) via a conversational interface. Includes a human review stage where generated code and results are verified before being committed to memory.

2. **Data Analysis Assistant (Stream 2)**: High-volume, low-cost stream for end-users. Checks memory for facts or skills (recipes). No code generation on the fly — uses less powerful LLMs, is more stable and secure, and incurs lower costs.

## Memory Hierarchy

The system implements a hierarchy of memory distinguishing:
- **Facts**: Cached answers to specific questions (e.g., "What's the population of Mali?")
- **Skills**: Generalized reusable recipes (e.g., "How to get the population of any country")

Facts can be promoted to skills via LLM reranking and transformation. This extends the LATM (LLMs As Tool Makers) architecture from Cai et al. (2023).

## Asynchronous Data Refresh

Recipes can be preemptively executed on schedules to pre-populate the cache, improving response times and enabling out-of-hours aggregation of API data. This mitigates the limitation of aggregate queries using API data.

## Benefits

- **Transparent**: Recipes are visible and human-reviewed
- **Deterministic**: Code produces same results each time
- **Performant**: Memory with asynchronous refresh improves response times
- **Inexpensive**: Two-stream architecture uses lower-cost LLMs for high-volume stream
- **Secure**: End-users do not trigger code generation on the fly

## Limitations

- New requests not in the recipe library require a delay for recipe creation
- Asynchronous refresh may become costly for large data volumes
- Not suitable for rapidly changing data requiring immediate results
- Still limited by data quality and availability
