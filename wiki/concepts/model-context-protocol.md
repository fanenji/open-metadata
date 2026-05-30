---
type: concept
title: Model Context Protocol
created: 2026-05-14
updated: 2026-05-14
tags: [mcp, ai, standards, integration, protocol]
related: [mcp-server, openmetadata, unified-metadata-graph]
sources: ["mcp-server---openmetadata-documentation-20260514.md"]
---
# Model Context Protocol

The Model Context Protocol (MCP) is an emerging open standard, spearheaded by Anthropic and embraced by many industry leaders, that helps AI systems interact with external tools and data in a uniform, secure way. MCP works as a "universal translator" between AI assistants (or any LLM-driven application) and the myriad of systems where data and knowledge reside.

## Core Concept

Instead of building one-off integrations or brittle scripts for each data source, MCP provides a common interface. In technical terms, MCP lets systems expose their capabilities — the data they hold and the actions they can perform — in a machine-readable schema that AI models can understand.

Through MCP, a data platform can advertise:

- **Tools**: Functions an AI can call (e.g., `lookup_customer_by_email`)
- **Resources**: Datasets or knowledge bases an AI can query
- **Prompt Templates**: Guided interaction patterns

An AI assistant connected via MCP can then securely retrieve information or trigger actions by invoking these standardized functions, with proper authorization.

## Significance for Organizations

MCP promises to bridge the gap between powerful AI reasoning and real-world data context. With a single, consistent protocol, an AI assistant can maintain awareness of business-specific context as it moves between different tools and datasets. Just as HTTP standardized how clients talk to servers, MCP is standardizing how AI models connect with data sources — a simpler, more scalable way to give AI access to the knowledge it needs to produce relevant, accurate results.

## MCP in OpenMetadata

OpenMetadata implements MCP through its [[mcp-server|MCP Server]], a built-in application that exposes the [[unified-metadata-graph]] to AI assistants. This allows AI tools to query live organizational metadata — definitions, lineage, ownership — through natural language, with access governed by existing [[roles-and-policies]].