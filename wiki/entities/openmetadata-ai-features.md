---
type: entity
title: OpenMetadata AI Features
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, ai, semantic-search, text-to-sql, auto-description]
related: [openmetadata, openmetadata-python-sdk, text2sql-patterns, llm-sql-generation-evaluation]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata AI Features

OpenMetadata has been shipping AI capabilities that go beyond search.

## Semantic Search

Natural language queries against the catalog — "find customer tables updated this week" — return ranked, relevant results using vector embeddings rather than keyword matching.

## Auto-Description Generation

OpenMetadata can use AI to generate draft descriptions for tables and columns based on:
- Column names and types
- Sample data
- Existing documentation in similar assets

This dramatically reduces the documentation burden on engineers.

## Text-to-SQL

Ask a plain English question and OpenMetadata generates SQL to answer it against your connected warehouse — directly inside the platform.

**Example:** "What's the total revenue from US customers in Q1 2025?" → OpenMetadata converts this to SQL, runs it (read-only), and returns the result inline.