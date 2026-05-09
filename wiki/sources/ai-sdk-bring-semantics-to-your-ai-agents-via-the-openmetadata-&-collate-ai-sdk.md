---
type: source
title: "ai-sdk Bring Semantics to your AI Agents via the OpenMetadata & Collat AI SDK"
created: 2026-02-26
updated: 2026-02-26
authors: [pmbrull]
year: 2026
url: "https://github.com/open-metadata/ai-sdk"
venue: "GitHub"
tags: [openmetadata, collate, ai-sdk, mcp, data-governance]
sources: ["ai-sdk Bring Semantics to your AI Agents via the OpenMetadata & Collate AI SDK.md"]
---
# ai-sdk Bring Semantics to your AI Agents via the OpenMetadata & Collate AI SDK

This source introduces the **OpenMetadata AI SDK**, a toolset designed to bridge the "semantic gap" in AI applications by providing LLMs with the rich context found in data catalogs.

## Key Features
- **Two-Path Architecture**: 
    - **MCP Tools**: For custom development using frameworks like [[model-context-protocol-mcp]] and [[langchain]].
    - **Dynamic Agents**: Ready-to-use assistants hosted in [[collate-ai-studio]].
- **Semantic Metadata Access**: Enables AI to perform semantic search, lineage traversal, and glossary/classification reading.
- **Catalog Mutations**: Allows AI agents to actively curate metadata (e.g., updating descriptions, adding lineage).
- **Multi-language Support**: Available for Python (`data-ai-sdk`), TypeScript, and Java.

## Use Cases (Cookbook)
- **MCP Impact Analysis**: Automated assessment of schema changes in CI/CD.
- **dbt Model PR Review**: Using [[github-actions]] and the SDK to review [[dbt]] changes.
- **DQ Failure Notifications**: Integrating with [[n8n]] and [[slack]] for automated data quality alerts.
- **GDPR Compliance**: Tracing PII across the catalog.