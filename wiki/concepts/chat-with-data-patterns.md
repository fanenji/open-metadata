---
type: concept
title: Chat with Data Patterns
created: 2026-05-06
updated: 2026-05-06
tags: [llm, data-analysis, patterns]
related: [llm-assisted-data-recipes, llm-sql-generation-evaluation, text2sql-patterns, llm-data-analysis-cost-optimization]
sources: ["Reframing LLM 'Chat with Data' Introducing LLM-Assisted Data Recipes.md"]
---
# Chat with Data Patterns

Existing patterns where Large Language Models (LLMs) enable users to ask questions in natural language about data. The LLM generates calls to retrieve data and summarizes the output for the user.

## Common Approaches

1. **Generating Database Queries**: The LLM converts natural language to SQL or Cypher queries. Supports aggregation across large volumes of data but requires data to already be in a queryable database.

2. **Generating API Queries**: The LLM converts natural language to API calls. Opens up public datasets but many APIs do not support aggregate queries, requiring extraction of large amounts of raw data.

## Key Limitations

- **Token Limits**: Passing raw data through LLMs for summarization does not scale to real-world data volumes
- **High Costs**: Iterative code generation and debugging with powerful models burns through tokens
- **Slowness**: Multiple LLM calls create poor user experience
- **Instability**: Code generation can fail, agents can get lost in debugging loops
- **Lack of Transparency**: Generated code and results are not easily scrutinized
- **Hallucination Risk**: LLM summarization of data can produce incorrect results

These limitations motivate the [[llm-assisted-data-recipes]] methodology as an alternative architecture.
