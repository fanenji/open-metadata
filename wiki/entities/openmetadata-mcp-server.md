---
type: entity
title: OpenMetadata MCP Server
created: 2026-02-17
updated: 2026-05-07
tags:
  - openmetadata
  - mcp
  - ai
  - knowledge-graph
  - agentic-ai
  - metadata
  - governance
  - model-context-protocol
  - data-catalog
  - ai-agents
related:
  - openmetadata
  - model-context-protocol
  - openmetadata-application-framework
  - personal-access-token-openmetadata
  - dremio-mcp-server
  - dbt-mcp-server
  - openmetadata-personal-access-token
  - collate
  - mcp-enterprise-implementation-patterns
  - openmetadata-dbt-ingestion
  - openmetadata-local-development
  - ai-agent-metadata-feedback-loop
sources:
  - "Introducing the Model Context Protocol (MCP) in OpenMetadata.md"
  - "Embedding an MCP Server into OpenMetadata - Summary.md"
  - "Embedding an MCP Server into OpenMetadata.md"
  - "OPENMETADATA - NOTE.md"
  - "OpenMetadata MCP - Context is Important"
  - "Metadata Provides It.md"
---
# OpenMetadata MCP Server

The OpenMetadata MCP Server is an embedded [[model-context-protocol]] (MCP) server that runs as an application within the [[openmetadata]] platform, exposing its unified knowledge graph to AI agents. It enables AI assistants to become organizationally‑aware by providing access to schemas, datasets, lineage, owners, usage, quality tests, dashboards, and ML models through a standardized interface. Built using the [[openmetadata-application-framework]], it integrates directly into the OpenMetadata server process, exposing MCP APIs alongside existing REST APIs on the same host and port. Rather than requiring users to run a separate MCP server locally, the MCP server can be enabled as a pluggable application module. It exposes the platform’s Unified Knowledge Graph — including physical metadata, lineage, quality scores, usage patterns, and governance context — to AI agents and other MCP clients via the MCP standard, enabling governed, real‑time access to organizational metadata. AI coding tools such as Claude Code and OpenCode can use this endpoint to query metadata, lineage, and governance information directly from the catalog. AI agents can not only read this context but also write improvements back, creating a feedback loop that continuously enriches the metadata knowledge graph.

## Architecture

The MCP server is implemented as a pluggable application module within the OpenMetadata Application Framework. When enabled, it exposes `/mcp/*` endpoints alongside the existing `/api/*` endpoints on the same host and port. No separate server deployment is required. Installing the MCP application activates the endpoint within the existing server process.

```
OpenMetadata Server
├── Core REST APIs
├── Application Framework
│   ├── Data Insights (built‑in)
│   ├── Search Indexing (built‑in)
│   └── MCP Server Application  ← embedded
│       └── exposes /mcp/* endpoints
```

### Embedded Deployment Benefits

The embedded design addresses three key challenges of standalone MCP deployments:

1. **Scalability** – No need for each user to run a local MCP server.
2. **Deployment Simplicity** – No additional infrastructure component.
3. **Authentication/Authorization** – Leverages OpenMetadata’s existing security model.

This implementation serves as a reference example for productionizing MCP in enterprise environments.

### Context Optimization

The server is designed to return only the necessary information to LLMs, avoiding context window bloat. It internally scans the Unified Knowledge Graph and returns minimal, relevant data, reducing token consumption while preserving the needed context.

## Security Model

The MCP server inherits OpenMetadata’s security framework:

- **Authentication**: Uses Personal Access Tokens ([[personal-access-token-openmetadata|PAT]]) or bot JWT tokens. Users generate a token from their OpenMetadata profile page; the token carries the user’s identity and is passed as a Bearer token in the `Authorization` header when configuring an MCP client. Optionally, an auth server URL (same as the MCP endpoint) can be used for OAuth2‑style token exchange.
- **Authorization**: Applies the same RBAC/ABAC policies as the UI and API. All permissions, roles, and data restrictions are enforced for every MCP call, preventing privilege escalation through the AI layer. Identity injection ensures each request is executed on behalf of the user.
- **Audit**: All sequences of actions performed via MCP are logged.

## Client Configuration

To connect an AI agent to the OpenMetadata MCP Server, the user must configure an MCP client with the appropriate credentials and endpoint URL. The server endpoint is typically `https://<openmetadata-instance>/mcp`. The following are configuration examples for popular tools.

### Claude Code / Claude Desktop

Configure the MCP server in `~/.claude/settings.json` or `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "openmetadata": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://openmetadata-test.dataliguria.it/mcp",
        "--auth-server-url=https://openmetadata-test.dataliguria.it/mcp",
        "--client-id=openmetadata",
        "--verbose",
        "--clean",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <your_personal_access_token>"
      }
    }
  }
}
```

The `mcp-remote` package acts as a proxy, forwarding standard MCP client communication to the remote OpenMetadata MCP endpoint while injecting the authentication header.

### OpenCode

Configure the server in `~/.config/opencode/opencode.json`:

```json
{
  "mcp": {
    "openmetadata": {
      "type": "local",
      "command": ["npx", "-y", "mcp-remote", "https://<instance>/mcp", "--header", "Authorization:Bearer <token>"],
      "enabled": true
    }
  }
}
```

Other MCP‑compatible clients (such as Goose, ChatGPT, or custom integrations) can connect in a similar way, providing the appropriate MCP server URL and authentication token.

## Capabilities and Tools

The MCP server exposes tools that leverage the full knowledge graph. The tools fall into two main categories:

- **Read Context** — Search, metadata retrieval, lineage traversal, quality scores, glossary and classification retrieval.
- **Write Back** — Patch operations, governance actions (bulk ownership, tagging, classification), metadata enrichment.

At launch in OpenMetadata v1.8.8 (May 2025), the server provided basic tools for search, read, and patch operations, with additional capabilities planned for future releases.

### Available Tools

- **Search** – Find tables, dashboards, pipelines, and other assets by name, tag, or description.
- **Metadata Retrieval** – Fetch schema, descriptions, columns, tags, data quality results, and detailed asset information.
- **Patch** – Update metadata, such as assigning ownership or modifying descriptions.
- **Lineage Traversal** – Discover related tables via column-level lineage (e.g., orders → sales → dashboard).
- **Quality‑Aware Recommendations** – Surface data quality tiers, test pass rates, and test results to guide table selection.
- **Governance Actions** – Bulk ownership assignment, tagging, classification via API PATCH calls.
- **Query Analysis** – Fetch associated SQL queries, join patterns, and usage history.
- **Glossary and Classification Retrieval** – Access business glossary terms and classification tags defined in the catalog.

Through the write‑back tools, AI agents can create a feedback loop by automatically tagging, documenting, and classifying data assets, continuously enriching the knowledge graph.

## Use Cases and Workflows

### Organizationally‑Aware AI Assistants

LLMs connected to the catalog via MCP can understand data relationships, ownership, and governance before answering questions or performing analysis, reducing hallucinations and ensuring context‑aware responses.

### Conversational Metadata Access

Natural language queries about data definitions, lineage, ownership, and quality — answered directly from the knowledge graph.

### Governance Automation

AI agents can scan for missing owners, classifications, or policy violations and apply corrections in bulk.

### Lineage Tracing

On‑demand impact analysis and root cause investigation using full column‑level lineage.

### Metadata Write‑Back / Enrichment

AI agents can automatically create quality tests, generate descriptions, update glossary terms, and classify assets, forming a [[ai-agent-metadata-feedback-loop]].

### Churn Prediction with Context

An LLM connected to a CRM via MCP can use metadata to understand complete account views, access controls, and data quality, avoiding incomplete analysis and producing more reliable churn predictions.

### Example Workflows

#### Data Analyst – Dashboard Generation

The LLM searches for customer tables, evaluates quality scores to recommend `dim_customers` over `raw_customers`, analyzes columns and associated queries, and generates a working customer retention dashboard (HTML/Python).

#### Data Steward – Bulk Ownership Assignment

The LLM finds unowned customer‑related assets, fetches the Data Team entity, and PATCHes ownership for all matching tables, reporting a summary of changes.

## Comparison with Other MCP Servers

| Aspect | OpenMetadata MCP Server | [[dremio-mcp-server]] | [[dbt-mcp-server]] |
|--------|------------------------|----------------------|---------------------|
| Architecture | Embedded (inside server) | External (separate process) | External (separate process) |
| Authentication | PAT‑based RBAC / JWT | API key | dbt Cloud token |
| Knowledge Exposed | Full knowledge graph (schemas, lineage, quality, ownership, dashboards, ML models, glossaries) | Query engine (direct data querying) | dbt project metadata (models, tests, runs, artifacts) |
| Deployment | Single service, no separate server needed | Requires separate server | Requires separate server |
| Write‑Back | Yes (Patch tools enable metadata enrichment, ownership assignment, etc.) | No | No (read‑only) |
| Maturity | Shipping in OpenMetadata v1.8+ (initial v1.8.8 with basic tools; advanced tools planned) | Available | Production (official dbt Labs) |

The OpenMetadata MCP Server focuses on metadata context rather than direct data querying. See [[mcp-enterprise-implementation-patterns]] for a deeper comparative analysis of enterprise MCP deployment patterns.

## Availability and Dependencies

The MCP server was initially developed in a workshop context and has since been merged into the OpenMetadata codebase (May 2025), shipping as an application in OpenMetadata v1.8 (open source). The initial release (v1.8.8) included basic search, read, and patch tools, with more tools planned for future releases.

The knowledge graph exposed by the server is populated by ingestion workflows. In particular, the [[openmetadata-dbt-ingestion]] connector is used to ingest dbt project metadata (models, tests, sources) into the catalog, making it available through the MCP server. The server complements other MCP endpoints like the [[dremio-mcp-server]] for direct data querying.

## See Also

- [[model-context-protocol]]
- [[openmetadata-application-framework]]
- [[personal-access-token-openmetadata]]
- [[openmetadata-personal-access-token]]
- [[collate]]
- [[mcp-enterprise-implementation-patterns]]
- [[openmetadata-dbt-ingestion]]
- [[openmetadata-local-development]]
- [[ai-agent-metadata-feedback-loop]]