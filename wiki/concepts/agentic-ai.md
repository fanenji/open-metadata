---
type: concept
title: "Agentic Ai"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Agentic AI
created: 2026-05-14
updated: 2026-05-14
tags: [ai, automation, mcp, llm]
related: [mcp-server, unified-metadata-graph, model-context-protocol, application-framework]
sources: ["Embedding an MCP Server into OpenMetadata.md"]
---

# Agentic AI

Agentic AI refers to AI models that can take actions on behalf of users, using contextual knowledge to make decisions and perform tasks autonomously. In the context of OpenMetadata, agentic AI is enabled by exposing the [[unified-metadata-graph|unified knowledge graph]] to LLMs through the embedded [[mcp-server|MCP server]].

## How OpenMetadata Enables Agentic AI

1. **Context provision:** The unified knowledge graph provides LLMs with rich context — schemas, lineage, data quality results, profiling, ownership, semantic tags, and user interactions.
2. **Standardized interface:** The [[model-context-protocol|Model Context Protocol]] provides a uniform way for LLMs to query and interact with this context.
3. **Identity-preserving actions:** [[personal-access-token|Personal Access Tokens]] ensure that AI actions inherit the user's RBAC/ABAC permissions, so the AI cannot bypass access controls.
4. **Action capability:** Beyond querying, the MCP server exposes tools that allow LLMs to update metadata — for example, assigning ownership or updating descriptions.

## Example Scenarios

- **Data analyst** asks an LLM to find relevant customer tables; the AI uses MCP to search the knowledge graph, evaluate data quality, and recommend the best table.
- **Data steward** asks an LLM to find all unowned customer assets and assign them to the Data Team; the AI performs the search and bulk-updates ownership.