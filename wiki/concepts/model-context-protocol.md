---
type: concept
title: Model Context Protocol (MCP)
created: 2026-05-06
updated: 2026-05-07
tags: [ai, standards, interoperability, mcp, ai-integration, protocol, data-access, metadata, governance]
related: [openmetadata, semantic-context-layer, dremio-mcp-server, dremio, claude, openmetadata-mcp-server, dbt-mcp-server, mcp-enterprise-implementation-patterns]
sources: [announcing-openmetadata-1-13-20260506.md, Come installare il server mcp di Dremio-20260507.md, Introducing the Model Context Protocol (MCP) in OpenMetadata.md, dbt-labsdbt-mcp A MCP (Model Context Protocol) server for interacting with dbt..md]
---
# Model Context Protocol (MCP)

The **Model Context Protocol (MCP)** is an open standard, spearheaded by Anthropic, that standardizes how AI agents, Large Language Models (LLMs), and AI clients (such as [[claude]]) interact with external tools, data sources, and servers. It provides a uniform, secure interface for AI-driven data access, allowing natural language queries and analysis without requiring direct database connections. MCP bridges AI clients with data lakehouse platforms and supports multiple operational modes such as data querying and performance monitoring. In the data platform context, MCP enables AI agents to query and analyze data from systems like [[dremio]] through self-hosted servers (e.g., [[dremio-mcp-server]]). It is a key enabler of the "Agentic Enterprise" vision, where AI agents can autonomously explore and interact with organizational data.

## How MCP Works

MCP lets systems expose their capabilities in a machine-readable schema that AI models can understand. Systems can advertise:

- **Tools**: Functions an AI can call (e.g., `lookup_customer_by_email`)
- **Resources**: Datasets or knowledge bases an AI can query
- **Prompt templates**: Guides for interactions

An AI assistant connected via MCP can securely retrieve information or trigger actions by invoking these standardized functions, with proper authorization.

## Enterprise Implementations

Three enterprise MCP implementations are documented in this wiki:

1. **[[openmetadata-mcp-server]]**: An embedded MCP server within [[OpenMetadata]] that exposes the Unified Knowledge Graph with full RBAC and audit. AI agents can leverage the platform's **Knowledge Graph** and **Semantic Context Layer** to retrieve structured, business-accurate information.

2. **[[dremio-mcp-server]]**: A self-hosted MCP server for [[dremio]] that enables AI clients to query and analyze data stored in the lakehouse, supporting natural language interactions and performance monitoring. Jobs executed via MCP are visible in the Dremio console, filtered as "External Tools".

3. **[[dbt-mcp-server]]**: The official dbt Labs MCP server for AI agent interaction with dbt projects, allowing agents to query and transform dbt metadata.

See [[mcp-enterprise-implementation-patterns]] for a comparative analysis.

## Significance

MCP promises to bridge the gap between powerful AI reasoning and real-world data context. Just as HTTP standardized how clients talk to servers, MCP is standardizing how AI models connect with data sources. For organizations, this means AI assistants can maintain awareness of business-specific context as they move between different tools and datasets.