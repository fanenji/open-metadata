---
type: source
title: "Benchmark to Understand the Role of Knowledge Graphs on LLM's Accuracy for Question Answering on Enterprise SQL Databases"
created: 2024-05-22
updated: 2024-05-22
tags: [knowledge-graph, llm, sql, sparql, benchmark, ai]
related: [knowledge-graph, semantic-context-layer, data-virtualization-layer, ai-driven-data-quality]
authors: [Juan F. Sequeda, Dean Allemang, Bryon Jacob]
year: 2023
url: "https://arxiv.org/abs/2311.07509v1"
venue: "arXiv"
sources: ["Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases.md"]
---
# Benchmark to Understand the Role of Knowledge Graphs on LLM's Accuracy for Question Answering on Enterprise SQL Databases

This technical report investigates the impact of Knowledge Graphs (KGs) on the accuracy of Large Language Models (LLMs) when performing Text-to-SQL and Text-to-SPARQL tasks on complex enterprise schemas.

## Key Findings
The study demonstrates that using GPT-4 to query SQL databases directly achieves only **16.7%** accuracy on enterprise-grade questions. However, when a **Knowledge Graph** layer (comprising an ontology and R2RML mappings) is introduced, accuracy jumps to **54.2%**—a 3x improvement.

### Accuracy by Complexity Quadrant
| Quadrant | w/o KG (SQL) | w/ KG (SPARQL) |
|---|---|---|
| **All Questions** | 16.7% | 54.2% |
| **Low Question/Low Schema** | 25.5% | 71.1% |
| **High Question/Low Schema** | 37.4% | 66.9% |
| **Low Question/High Schema** | 0% | 35.7% |
| **High Question/High Schema** | 0% | 38.5% |

## Failure Modes
- **SQL Inaccuracy**: Characterized by **hallucinations** (inventing columns, values, or joins).
- **SPARQL Inaccuracy**: Characterized by **path/direction inconsistencies** (navigating the ontology incorrectly) but notably lacked class/property hallucinations.

## Conclusion
The research concludes that investing in a Knowledge Graph as a semantic context layer is essential for reliable enterprise AI, as it provides the necessary business semantics that raw SQL schemas lack.
