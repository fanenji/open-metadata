---
type: concept
title: First-Shot Acceptance Rate
created: 2026-04-29
updated: 2026-04-29
tags: [text-to-sql, metrics, productivity, evaluation]
related: [pinterest-text-to-sql-architecture, text2sql-patterns, llm-sql-generation-evaluation]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# First-Shot Acceptance Rate

First-Shot Acceptance Rate is a key productivity metric for Text-to-SQL systems, measuring the percentage of generated SQL queries that are accepted by users without modification.

## Pinterest's Results

- Initial rate: 20%
- Improved rate: >40% (as implementation improved and users became more familiar with the feature)

## Interpretation

A 40% first-shot acceptance rate may seem low, but Pinterest observed a 35% improvement in task completion speed. This suggests that the value of Text-to-SQL comes primarily from accelerating the iterative refinement process rather than from one-shot accuracy. Most queries require multiple human-AI iterations before finalization.

## Relationship to Other Metrics

The first-shot acceptance rate complements other metrics like task completion speed improvement and provides a more nuanced view of Text-to-SQL performance than benchmark accuracy alone.