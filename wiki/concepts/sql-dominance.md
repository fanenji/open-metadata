---
type: concept
title: SQL Dominance
created: 2026-05-07
updated: 2026-05-07
tags: [sql, transformation, modern-data-stack, trend]
related: [elt-pattern, dbt-cloud, text2sql-patterns, llm-sql-generation-evaluation]
sources: ["The Modern Data Stack in 2025 What Actually Won.md"]
---
# SQL Dominance

SQL dominance is the finding that 94% of transformation logic is pure SQL (vs Python/Scala/Java), reversing predictions that Python would dominate data transformation.

## Why SQL Won

- Declarative (easier to understand and maintain)
- Accessible to analysts (not just engineers)
- Warehouse engines optimized for SQL
- [[dbt-cloud|dbt]] made SQL transformations elegant

## Where Python Still Matters

- Complex ML feature engineering
- Custom business logic (non-SQL-native)
- API calls and external integrations
- Streaming transformations

## Implications

SQL remains the foundational skill for data practitioners. The source notes that 94% of job postings require SQL. The dominance of SQL reinforces the [[elt-pattern]] and the central role of dbt in the modern data stack. The source predicts that AI-generated SQL will become common (40%+ of queries AI-assisted by 2027), which connects to [[text2sql-patterns]] and [[llm-sql-generation-evaluation]].
