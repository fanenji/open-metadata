---
type: entity
title: Gemini CLI
created: 2026-04-05
updated: 2026-04-05
tags: [ai, cli, tool, agent]
related: [mcp-toolbox, model-context-protocol]
sources: ["Building a Semantic Intelligence Layer for the AI Data Stack.md"]
---
# Gemini CLI

**Gemini CLI** is the command-line interface used to interact with **MCP Servers** and execute agentic workflows. It serves as the primary interface for developers to trigger complex, multi-step data operations using natural language prompts.

By configuring the `settings.json` to include various MCP servers (such as **OpenMetadata** and **MCP Toolbox**), users can instruct the CLI to:
- Trace lineage across different data services.
- Synchronize metadata between catalogs and BI tools.
- Perform automated data engineering tasks like creating tables and inserting statistics.

---END BI---

---FILE: wiki/concepts/semantic-intelligence-layer.md---
---
type: concept
title: Semantic Intelligence Layer
created: 2026-04-05
updated: 2026-04-05
tags: [ai, data-engineering, architecture]
related: [semantic-context-layer, openmetadata, mcp-toolbox, ai-ready-data]
sources: ["Building a Semantic Intelligence Layer for the AI Data Stack.md"]
---
# Semantic Intelligence Layer

A **Semantic Intelligence Layer** is an architectural layer situated atop the data stack that provides AI agents with the "meaning" (definitions, lineage, and constraints) behind raw data.

### The Problem: The Semantic Gap
In traditional data stacks, humans can resolve ambiguity through discussion (e.g., deciding which "passenger" count is correct). However, AI agents lack this ability and will execute incorrect logic if definitions are inconsistent.

### The Solution
By combining a semantic catalog (like **Open
Metadata**) with an action-oriented toolset (like **MCP Toolbox**), organizations can create a layer that:
- **Standardizes Meaning**: Ensures that "passengers" or "revenue" are defined identically across all tools.
- **Enables Agentic Action**: Provides the context necessary for agents to perform tasks like **Automated Tag Synchronization**.
- **Ensures Trust**: Allows agents to operate within established authorization and governance frameworks.
