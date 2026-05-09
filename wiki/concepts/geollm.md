---
type: concept
title: GeoLLM
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, llm, machine-learning, openstreetmap]
related: [llm-for-geospatial-prediction, openstreetmap-data-model, geospatial-analytics-with-dbt, cloud-native-geospatial-workflow, h3-geospatial-indexing]
sources: ["GeoLLM Extracting Geospatial Knowledge from Large Language Models.md"]
---
# GeoLLM

GeoLLM is a novel method for extracting geospatial knowledge from large language models (LLMs) by combining geographic coordinate prompts with auxiliary map data from OpenStreetMap. Developed by researchers at Stanford University, the method demonstrates that LLMs compress remarkable spatial information from internet text corpora, enabling accurate predictions of population density and economic livelihoods from location alone (with map augmentation).

## Key Findings

- **70% improvement** in performance (Pearson's r²) over nearest-neighbor baselines
- Performance equal to or exceeding satellite-based benchmarks
- GPT-3.5 outperforms Llama 2 by 19% and RoBERTa by 51%
- LLMs are remarkably sample-efficient, requiring few training examples
- Robust across the globe

## Methodology

The method addresses the limitation that naively querying LLMs with geographic coordinates alone is ineffective. By augmenting coordinate prompts with auxiliary map data from OpenStreetMap, GeoLLM can effectively extract the spatial knowledge embedded in LLMs during pretraining.

## Implications for Data Engineering

GeoLLM opens a new paradigm for geospatial machine learning by demonstrating that LLMs can serve as a rich, sample-efficient source of geospatial information. This is directly relevant to data platform decisions about covariate selection, potentially reducing reliance on expensive satellite imagery for certain prediction tasks. The method could complement existing geospatial data pipelines documented in this wiki, such as [[geospatial-analytics-with-dbt]] and [[cloud-native-geospatial-workflow]].

## Open Questions

- How would GeoLLM perform with more recent LLMs (GPT-4, Claude 3, Gemini)?
- What are the latency and cost implications of using LLM queries for geospatial prediction at scale?
- Could GeoLLM be integrated into a dbt pipeline as a custom geospatial covariate source?