---
type: source
title: "Embedding an MCP Server into OpenMetadata - Summary"
created: 2026-04-04
updated: 2026-04-29
tags: [openmetadata, mcp, ai, knowledge-graph, tools, agentic-ai]
related: [openmetadata, model-context-protocol, openmetadata-mcp-server, openmetadata-application-framework, personal-access-token-openmetadata, data-catalog-tool-comparison, data-observability-three-pillars]
sources: ["Embedding an MCP Server into OpenMetadata - Summary.md"]
---
# Embedding an MCP Server into OpenMetadata — Summary

**Speakers:** Shihara & Mohe, Collate  
**Event:** OpenMetadata Community Meetup, May 21, 2025  
**Video:** https://www.youtube.com/watch?v=AuYBaXC8-M4  

This talk presents Collate's solution for embedding an MCP (Model Context Protocol) server directly into the OpenMetadata server process as an OpenMetadata Application. The solution addresses three key challenges of traditional MCP deployments: per-user local server setup, deployment complexity, and authentication/authorization bypass. By using Personal Access Tokens (PATs) to carry user identity, the embedded MCP server enforces existing RBAC policies on every AI-driven call. The talk demonstrates agentic workflows including automated dashboard generation and bulk ownership assignment, leveraging OpenMetadata's Unified Knowledge Graph to surface not just schema but lineage, quality scores, usage patterns, and governance context.

## Key Takeaways

- **Problem:** Per-user local MCP servers are not scalable and bypass RBAC.
- **Solution:** MCP embedded as an OpenMetadata Application — single deployment, all users benefit.
- **Auth:** Personal Access Tokens carry user identity and enforce existing permissions.
- **Power:** Full knowledge graph exposed: lineage, quality, usage, governance — not just schema.
- **Agentic AI:** LLMs can take actions (bulk ownership, schema discovery, dashboard generation).
- **Version:** Available in OpenMetadata v1.8, open source.
