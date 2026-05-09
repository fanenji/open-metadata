---
type: source
title: "GeoLLM: Extracting Geospatial Knowledge from Large Language Models"
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, llm, machine-learning, openstreetmap]
related: [geollm, llm-for-geospatial-prediction, openstreetmap-data-model, geospatial-analytics-with-dbt, cloud-native-geospatial-workflow]
sources: ["GeoLLM Extracting Geospatial Knowledge from Large Language Models.md"]
authors: [Rohin Manvi, Samar Khanna, Gengchen Mai, Marshall Burke, David Lobell, Stefano Ermon]
year: 2023
url: "https://arxiv.org/abs/2310.06213"
venue: arXiv
---
# GeoLLM: Extracting Geospatial Knowledge from Large Language Models

This paper explores whether the vast amounts of knowledge found in Internet language corpora, now compressed within large language models (LLMs), can be leveraged for geospatial prediction tasks. The authors demonstrate that LLMs embed remarkable spatial information about locations, but naively querying LLMs using geographic coordinates alone is ineffective in predicting key indicators like population density.

The paper presents **GeoLLM**, a novel method that can effectively extract geospatial knowledge from LLMs with auxiliary map data from OpenStreetMap. The method is demonstrated across multiple tasks including the measurement of population density and economic livelihoods.

## Key Findings

- **70% improvement** in performance (measured using Pearson's r²) relative to baselines using nearest neighbors or direct prompt information
- Performance equal to or exceeding satellite-based benchmarks in the literature
- GPT-3.5 outperforms Llama 2 by 19% and RoBERTa by 51%
- LLMs are remarkably sample-efficient, rich in geospatial information, and robust across the globe
- GeoLLM shows promise in mitigating the limitations of existing geospatial covariates and complementing them well

## Methodology

The method combines geographic coordinate prompts with auxiliary map data from OpenStreetMap to extract geospatial knowledge from LLMs. This approach addresses the limitation that naively querying LLMs with coordinates alone fails to produce accurate predictions.

## Implications

The paper suggests that LLMs can serve as a rich, sample-efficient source of geospatial information, potentially reducing reliance on expensive satellite imagery for certain prediction tasks. This opens a new paradigm for geospatial machine learning that is directly relevant to data platform decisions about covariate selection.

Code is available at: [https://rohinmanvi.github.io/GeoLLM](https://rohinmanvi.github.io/GeoLLM)