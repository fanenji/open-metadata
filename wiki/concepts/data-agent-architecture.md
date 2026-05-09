---
type: concept
title: Data Agent Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [data-architecture, ai, agent, dbt]
related: [ai-data-stack, context-management-vs-semantic-layer, quirk-knowledge-store, dbt, jamie-quint]
sources: ["How to Build a Data Agent in 2026.md"]
---
# Data Agent Architecture

An architectural pattern for building AI data agents that automatically answer questions by investigating source code and writing SQL. This pattern was described by [[Jamie Quint]] in his guide "How to Build a Data Agent in 2026."

## Core Components

### 1. Agentic Loop
The main execution environment running on a host machine. Recommended tool: Claude Agent SDK (using Opus 4.6 for data analysis tasks).

### 2. Context Sub-Agent
Dispatched before any SQL is written. Its job is to investigate the data landscape by:
- Reading relevant dbt model files (full transformation logic, not just headers)
- Tracing upstream dependencies through the DAG
- Checking application code if annotations exist
- Returning a structured brief: tables, columns, join paths, filters, dedup rules, caveats

This sub-agent is cheap (mostly file reading) and prevents the main agent from hallucinating table structures.

### 3. Main Agent
Receives the context brief and writes SQL to answer the user's question. Uses the context brief to avoid common mistakes.

### 4. Knowledge Store
A hybrid retrieval system storing:
- **Quirks** — Durable corrections extracted from user feedback
- **Metric Definitions** — Human-authored definitions for core KPIs

Implementation: Postgres + pgvector for vector similarity, OpenAI text-embedding-3-small for embeddings, pg_textsearch for BM25 keyword search.

### 5. Self-Scoring Loop
The agent scores its own SQL on three dimensions:
- Structural correctness
- Execution reliability
- Context alignment

Uses deterministic signals plus Haiku for semantic/context checks. Builds a context-gap brief that drives recovery loops.

### 6. User Interface
- Slack integration for question submission and answers
- Admin dashboard for monitoring usage and editing knowledge store
- Notion integration for saving answers

## Data Flow

1. User asks question in Slack
2. Context sub-agent investigates dbt models and app code
3. Knowledge store retrieves relevant quirks and metric definitions
4. Main agent receives context brief + knowledge and writes SQL
5. SQL executes against query engine (Snowflake/BigQuery)
6. Self-scoring agent evaluates the result
7. If gaps found, retry with targeted prompt
8. Answer returned to user in Slack
9. User corrections extracted as new quirks into knowledge store

## Prerequisites

- Accessible dbt repository and application codebase
- Annotated dbt base models with links to application code
- Postgres database with pgvector extension
- Slack workspace with bot integration
- Admin dashboard infrastructure