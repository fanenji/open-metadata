---
type: concept
title: Low-Cardinality Column Handling
created: 2026-04-29
updated: 2026-04-29
tags: [text-to-sql, sql-generation, schema, llm]
related: [pinterest-text-to-sql-architecture, text2sql-patterns]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# Low-Cardinality Column Handling

Low-Cardinality Column Handling is a technique for improving the precision of LLM-generated SQL queries by incorporating the unique values of low-cardinality columns into the table schema provided to the LLM.

## Problem

When generating SQL queries, LLMs may produce WHERE clauses with incorrect filter values. For example, a query for "how many active users are on the 'web' platform" might generate `WHERE platform = 'web'` instead of the correct `WHERE platform = 'WEB'`.

## Solution

Unique values of low-cardinality columns that are frequently used for filtering are processed and incorporated into the table schema. This allows the LLM to generate precise SQL queries with correct filter values.

## Context

This technique was used in Pinterest's Text-to-SQL implementation as part of the table schema preparation step, alongside column pruning to manage context window limits.