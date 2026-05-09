---
type: concept
title: dbt-osmosis Benchmarking
created: 2026-04-29
updated: 2026-04-29
tags: [dbt-osmosis, llm, benchmarking, testing]
related: [dbt-osmosis, dbt-osmosis-llm-module, dbt-osmosis-custom-prompt-guide, dbt-llm-documentation-generation]
sources: ["dbt-osmosis synthetize.md"]
---
# dbt-osmosis Benchmarking

A systematic approach to testing and comparing different LLM models and prompt configurations for use with [[dbt-osmosis]]'s `yaml refactor --synthesize` command. Benchmarking is critical for selecting the optimal model and settings for automated documentation generation.

## Purpose

- Evaluate quality of generated table and column descriptions across different LLM models.
- Compare prompt configurations for detail level, language, and accuracy.
- Measure throughput and latency for different batch sizes.
- Identify the optimal trade-off between quality and processing speed.

## Key Variables

- **LLM Model** — different models (e.g., Llama, Mistral, GPT) produce varying quality.
- **Batch Size** — number of models processed per request; smaller batches yield better descriptions.
- **Prompt Template** — structure and wording of the prompt sent to the LLM.
- **Language** — English vs. Italian (or other locales).
- **Detail Level** — concise vs. verbose descriptions.

## Methodology

The planned benchmarking approach involves:
1. Running `dbt-osmosis yaml refactor --synthesize` with different configurations.
2. Collecting generated descriptions and metadata.
3. Producing a summary table comparing quality, latency, and throughput.
4. Evaluating results against a rubric (accuracy, completeness, relevance).

## Open Questions

- What is the optimal batch size for balancing quality and throughput?
- Which LLM model provides the best documentation quality for this use case?
- How should custom prompts be structured for Italian language descriptions?
- Should dedicated models be used for different documentation tasks (e.g., table descriptions vs. column descriptions)?