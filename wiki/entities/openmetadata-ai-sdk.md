---
type: entity
title: "OpenMetadata AI SDK"
created: 2026-07-07
updated: 2026-07-07
tags: [openmetadata, ai, sdk, mcp, api]
related: [openmetadata, mcp-server, knowledge-graph, unified-metadata-graph, agentic-ai]
sources: ["Announcing OpenMetadata 1.12 1.md"]
---
# OpenMetadata AI SDK

The **OpenMetadata AI SDK** ([GitHub](https://github.com/open-metadata/metadata-ai-sdk)) is a programmatic interface to OpenMetadata's semantic layer, introduced in OpenMetadata 1.12. It provides access to the platform's [[unified-metadata-graph|Unified Metadata Graph]] via the embedded [[mcp-server|MCP Server]], enabling developers to embed metadata intelligence into any application or workflow.

## Capabilities

- **Access to the Unified Metadata Graph**: query lineage, quality metrics, ownership, and business meaning through a simple API — no need to reconstruct the knowledge graph independently
- **Workflow Integration**: embed OpenMetadata intelligence into AI agents, chatbots, CI/CD pipelines, and tools like Slack, GitHub, or n8n
- **MCP-based Architecture**: leverages the Model Context Protocol for standardized tool-based interactions

## Use Cases

- Build custom chatbots that answer metadata questions (e.g., "what's the lineage of this table?")
- Automate governance workflows: auto-tag assets, trigger quality checks, generate documentation
- Integrate metadata intelligence into existing AI systems without building a separate knowledge graph

## Relationship to MCP Server

The AI SDK is built on top of OpenMetadata's [[mcp-server]], which was introduced in version 1.9. While the MCP Server provides the low-level tooling (metadata operations, lineage, quality), the AI SDK provides a higher-level programmatic interface designed for application developers.

## Version History

| Version | Release | Changes |
|---------|---------|---------|
| 1.0 | OpenMetadata 1.12 (Feb 2026) | Initial release with knowledge graph access |

## See Also

- [[openmetadata]] — OpenMetadata platform overview
- [[mcp-server]] — Model Context Protocol server integration
- [[agentic-ai]] — AI agent concepts in OpenMetadata
- [[knowledge-graph]] — Knowledge graph layer