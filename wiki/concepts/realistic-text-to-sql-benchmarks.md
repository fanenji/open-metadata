---
type: concept
title: Realistic Text-to-SQL Benchmarks
created: 2026-04-29
updated: 2026-04-29
tags: [text-to-sql, benchmarks, evaluation, llm]
related: [llm-sql-generation-evaluation, text2sql-patterns, pinterest-text-to-sql-architecture]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# Realistic Text-to-SQL Benchmarks

Realistic Text-to-SQL Benchmarks is a call from Pinterest Engineering for benchmark datasets that better reflect real-world conditions for SQL generation tasks.

## Critique of Existing Benchmarks

Pinterest found that existing benchmarks like Spider are substantially easier than real-world problems because they:
- Use a small number of pre-specified tables.
- Use well-normalized tables with few and well-labeled columns.
- Do not require table search as part of the task.

## Proposed Improvements

Real-world benchmarks should:
- Include a larger number of denormalized tables.
- Treat table search as a core part of the problem.
- Reflect the iterative nature of human-AI collaboration.

## Implications

This critique challenges the relevance of benchmark performance for predicting real-world success. Pinterest's own production metrics (35% speed improvement, 40% acceptance rate) provide a more realistic picture of Text-to-SQL utility than benchmark scores.