---
type: source
title: "Source: how-i-built-a-self-improving-llm-wiki-with-hermes-agent-and-why-im-not-using.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["how-i-built-a-self-improving-llm-wiki-with-hermes-agent-and-why-im-not-using.md"]
tags: []
related: []
---

# Source: how-i-built-a-self-improving-llm-wiki-with-hermes-agent-and-why-im-not-using.md

# Analysis: "How I Built a Self-Improving LLM Wiki with Hermes Agent"

## Key Entities

- **Hermes Agent** (NousResearch) — Central entity. Open-source self-improving AI agent with persistent memory, multi-platform gateways (Telegram, Discord, etc.), and tool/terminal access. **Does not exist in wiki.**
- **Andrej Karpathy** — Creator of the LLM Wiki pattern (gist). Peripheral but foundational. **Does not exist in wiki.**
- **Hetzner** — VPS provider (2 vCPU, 4 GB RAM). Peripheral infrastructure. **Does not exist in wiki.**
- **Telegram** — Primary user interface via bot. Peripheral but important for workflow. **Does not exist in wiki.**
- **Obsidian** — Contrast entity. The author's previous PKM tool, now replaced. **Does not exist in wiki.**
- **LLM Wiki** — The system being built. Central concept. **Does not exist in wiki.**
- **Caddy** — Web server used for static site hosting. Peripheral. **Does not exist in wiki.**

## Key Concepts

- **LLM Wiki Pattern** (Karpathy) — Architecture with three layers: raw sources (immutable), wiki (LLM-generated pages), schema (config). Three operations: Ingest, Query, Lint. **Does not exist in wiki.**
- **Self-Improving Agent** — Agent that remembers user preferences, suggests schema improvements, and gradually improves knowledge base maintenance. **Does not exist in wiki.**
- **Persistent Memory** — Hermes Agent's ability to remember across sessions, not just current chat. **Does not exist in wiki.**
- **Multi-Surface Access** — Single agent accessible via Telegram, web, CLI simultaneously. **Does not exist in wiki.**
- **Compounding Knowledge** — Knowledge base that improves over time rather than accumulating dead notes. **Does not exist in wiki.**
- **Maintenance Debt** — The problem of manual wiki upkeep (cross-references, summaries, index pages) becoming a second job. **Does not exist in wiki.**

## Main Arguments & Findings

1. **Core claim**: An LLM-maintained wiki is superior to manual PKM tools like Obsidian because it eliminates maintenance debt and compounds knowledge.
2. **Evidence**: Author's personal experience — abandoned multiple Obsidian wikis due to maintenance burden; Hermes Agent successfully maintains the wiki autonomously.
3. **Evidence strength**: Anecdotal/personal. No quantitative metrics, no comparison with alternatives, no long-term reliability data.

## Connections to Existing Wiki

- **Strong connection** to [[context-store]] — Both are versioned, queryable stores of structured knowledge. The LLM Wiki is a simpler, agent-maintained version of a context store.
- **Strong connection** to [[contextualize-pipeline]] — The Ingest operation (source → wiki pages) mirrors the contextualize pipeline's function of inferring and storing semantic context.
- **Moderate connection** to [[ECL-framework]] — The LLM Wiki's three-layer architecture (sources, wiki, schema) parallels ECL's Extract, Contextualize, Link framework.
- **Moderate connection** to [[embedded-metadata]] — The wiki captures 
