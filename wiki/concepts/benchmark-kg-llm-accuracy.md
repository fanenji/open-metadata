---
type: concept
title: Benchmark: KG vs LLM Accuracy
created: 2026-05-06
updated: 2026-05-06
tags: ["benchmark", "ai", "sql", "sparql", "accuracy"]
related: ["knowledge-graph", "semantic-context-layer", "data-virtualization-layer", "ai-driven-data-quality", "gpt-4", "text-to-sparql-for-enterprise"]
sources: ["Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases.md", "Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases-20260506.md"]
---
# Benchmark: KG vs LLM Accuracy

This concept refers to the empirical study comparing the performance of LLMs (specifically GPT-4) when querying databases directly via SQL versus querying via a Knowledge Graph (KG) using SPARQL.

## Key Metrics and Results
The benchmark evaluates accuracy across four quadrants based on **Question Complexity** (Reporting vs. KPIs) and **Schema Complexity** (Number of tables/joins).

| Quadrant | w/o KG (SQL) | w/ KG (SPARQL) | Improvement |
|---|---|---|---|
| **All Questions** | 16.7% | 54.2% | 37.5% |
| **Low Question/Low Schema** | 25.5% | 71.1% | 45.6% |
| **High Question/Low Schema** | 37.4% | 66.9% | 29.5% |
| **Low Question/High Schema** | 0% | 35.7% | 35.7% |
| **High Question/High Schema** | 0% | 38.5% | 38.5% |

## The "Complexity Wall"
A critical finding is that when schema complexity exceeds 4 tables, the SQL-based approach suffers a total collapse in accuracy (**0%**), while the KG-based approach maintains a functional level of accuracy.
