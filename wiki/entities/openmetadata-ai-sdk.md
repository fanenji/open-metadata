---
type: entity
title: OpenMetadata AI SDK
tags: [sdk, ai, metadata, python, typescript, java, automation]
related: [openmetadata, model-context-protocol-mcp, collate-ai-studio, langchain, semantic-context-layer]
sources: ["ai-sdk Bring Semantics to your AI Agents via the OpenMetadata & Collate AI SDK.md", "Announcing OpenMetadata 1.12-20260506.md"]
updated: 2026-05-06
created: 2026-02-26
---
# OpenMetadata AI SDK

The **OpenMetadata AI SDK** is a multi-language software development kit designed to provide AI agents, custom applications, and automated workflows with programmatic access to OpenMetadata's semantic layer and knowledge graph. It allows developers to embed metadata intelligence—including lineage, quality metrics, and ownership—directly into their tools, moving beyond raw schema reading to understand the true "meaning" of data.

## Key Capabilities

- **Semantic Intelligence**: Provides access to the unified metadata graph via a simple API, enabling **Semantic Search** (finding assets by business meaning) and eliminating the need for manual reconstruction of complex relationships.
- **Lineage Traversal**: Enables agents to understand upstream and downstream impacts through the metadata graph.
- **Active Governance & Automation**: Facilitates the automation of governance tasks and "Catalog Mutations" (where agents can update descriptions, tags, and glossary terms) by bringing metadata context to where developers work.
- **Integration with AI Agents**: Enables custom chatbots and agents (e.g., in Slack, GitHub, or n8n) to leverage the metadata graph for intelligent decision-making.

## Implementation Paths

1. **Custom Development (MCP)**: Exposes OpenMetadata as an [[model-context-protocol-mcp]] server, allowing integration with frameworks like [[langchain]].
2. **Dynamic Agents**: Leverages [[collate-ai-studio]] to invoke pre-configured, purpose-built agents.

## Supported Languages

- **Python**: Package name `data-ai-sdk`.
- **TypeScript**: Package name `@openmetadata/ai-sdk`.
- **Java**: Package name `org.open-metadata:ai-sdk`.