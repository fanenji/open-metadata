---
type: source
title: "Reframing LLM 'Chat with Data': Introducing LLM-Assisted Data Recipes"
created: 2026-05-06
updated: 2026-05-06
tags: [llm, data-analysis, architecture, data-recipes]
related: [llm-assisted-data-recipes, matthew-harris, chat-with-data-patterns, llm-data-analysis-cost-optimization, llm-sql-generation-evaluation, text2sql-patterns]
sources: ["Reframing LLM 'Chat with Data' Introducing LLM-Assisted Data Recipes.md"]
authors: [matthew-harris]
year: 2024
url: "https://towardsdatascience.com/reframing-llm-chat-with-data-introducing-llm-assisted-data-recipes-f4096ac8c44b/"
venue: "Towards Data Science"
---
# Reframing LLM 'Chat with Data': Introducing LLM-Assisted Data Recipes

This article by [[Matthew Harris]] proposes the **LLM-Assisted Data Recipes** methodology as an alternative to existing "Chat with Data" patterns. It identifies key limitations of current approaches — token limits, high costs, slowness, instability, and lack of transparency — and introduces a two-stream architecture that separates recipe creation (powerful LLMs + human review) from recipe execution (cheap, deterministic, no code generation). The article also presents a memory hierarchy distinguishing facts (cached answers) from skills (generalized reusable recipes), and an asynchronous data refresh mechanism for improved performance. The source is a conceptual proposal with architectural reasoning but no empirical benchmarks.
