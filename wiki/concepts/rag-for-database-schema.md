---
type: concept
title: RAG for Database Schema
created: 2026-05-07
updated: 2026-05-07
tags: [rag, text2sql, schema, retrieval, genbi]
related: [genbi-architecture, semantic-layer-for-text2sql, golden-queries-few-shot, text2sql-patterns, context-store]
sources: ["Text-to-SQL is Finally Production-Ready Building a Semantic Layer for GenBI.md"]
---
# RAG for Database Schema

Applying Retrieval-Augmented Generation (RAG) patterns to database schema metadata instead of raw data. This technique solves the core problem of context overload in LLM SQL generation.

## The Problem

If you dump the DDL for 200 tables into an LLM's context window, you introduce immense noise. When a user asks about "revenue," the LLM must scan thousands of tokens of schema definitions to figure out which column maps to that concept. Without guidance, the LLM guesses based on general training data, not specific business logic.

## The Solution

Instead of feeding the LLM *everything*, build a pipeline that:
1. Takes the user's natural language query
2. **Retrieves** only the most relevant table and column definitions from a semantic store
3. **Augments** a focused prompt with just that narrow context
4. **Generates** the SQL

## Implementation Pattern

The schema metadata is converted into embeddable documents (rich text descriptions of tables and columns), embedded using a model like `text-embedding-3-small`, and stored in a vector database (e.g., ChromaDB). When a user asks a question, the top-K most relevant schema documents are retrieved and injected into the LLM prompt as context.

## Relationship to Existing Wiki

This technique extends [[text2sql-patterns]] by providing a concrete retrieval mechanism. It is complementary to [[duckdb-nsql-7b]] (fine-tuned approach) and [[semantic-sql-testing-benchmark]] (evaluation approach). The schema vector store is a specialized [[context-store]].