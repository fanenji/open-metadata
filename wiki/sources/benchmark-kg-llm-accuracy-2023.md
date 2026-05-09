---
type: source
title: "A Benchmark to Understand the Role of Knowledge Graphs on LLM Accuracy for Question Answering on Enterprise SQL Databases"
created: 2026-05-06
updated: 2026-05-06
tags: [knowledge-graph, llm, sql, sparql, benchmark, ai]
related: [benchmark-kg-llm-accuracy, semantic-context-layer, gpt-4, data-world]
authors: [Juan F. Sequeda, Dean Allamang, Bryron Jacob]
year: 2023
url: "https://arxiv.org/abs/2311.07509v1"
venue: "arXiv:2311.07509v1 [cs.AI]"
sources: ["Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases-20260506.md"]
---
# A Benchmark to Understand the Role of Knowledge Graphs on LLM Accuracy for Question Answering on Enterprise SQL Databases

This technical report by **data.world** researchers investigates the impact of Knowledge Graphs (KGs) on the accuracy of Large Language Models (LLMs) when performing Text-to-SQL tasks on complex enterprise schemas.

## Key Findings
- **The Context Gap**: Standard Text-to-SQL approaches (direct SQL generation) achieve only **16.7%** accuracy on enterprise-grade schemas.
- **KG Superiority**: Using a Knowledge Graph layer (via SPARQL) increases accuracy to **54.2%**, a 3x improvement.
- **The Complexity Wall**: When schema complexity exceeds 4 tables, SQL-based accuracy drops to **0%**, whereas the KG approach maintains functional accuracy (approx. 35-38%).
- **Failure Modes**: 
    - **SQL Errors**: Characterized by **hallucinations** (inventing columns, values, or joins).
    - **SPARQL Errors**: Characterized by **path inconsistency** (incorrect relationship paths or directions in the ontology).

## Methodology
The study uses the **OMG Property and Casualty (P&C) Data Model** as a benchmark enterprise schema and evaluates **GPT-4** using zero-shot prompting across four quadrants of question and schema complexity.
