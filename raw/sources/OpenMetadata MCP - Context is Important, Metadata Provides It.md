---
type: note
topic: data-platform
created: 2026-02-17
tags:
  - openmetadata
  - mcp
  - tools

---


# OMD + MCP + LLM

https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e

  
Metadata platforms like OpenMetadata, combined with MCP servers, provide the missing **context** that makes AI agents and LLMs truly useful and safe in enterprise settings by exposing a unified, governed view of organizational data to AI tools.[](https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e)​

### Problem: AI Without Context

The article argues that data scientists, AI agents, and LLMs often fail not because models are weak, but because they lack organizational context about customers, systems, and permissions. Simply connecting an LLM directly to a CRM or other raw systems leads to hallucinations, incomplete views of accounts, and access-control issues, especially in use cases like churn prediction for a sales team.[](https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e)​

### Role of Model Context Protocol (MCP)

MCP standardizes how AI systems connect to tools and data sources through MCP servers, so any application can expose functionality once and any AI agent can consume it in a uniform way. This includes standard expectations for authentication, data exchange, and function calling, making it easier to plug tools into multiple AI agents without bespoke integrations.[](https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e)​

### Why Metadata Platforms Matter


The article’s key point is that MCP alone only solves connectivity; it does not solve the quality or completeness of context. Metadata platforms aggregate schemas, datasets, lineage, owners, usage, quality tests, dashboards, and ML models into a unified knowledge graph that becomes a single source of truth across all data systems and departments over time.[](https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e)​

### OpenMetadata + MCP for AI


OpenMetadata is presented as an open-source unified metadata platform that automatically discovers and catalogs data, maintains real-time lineage, and enforces governance at scale. By exposing OpenMetadata’s knowledge graph through its MCP server, AI agents can become organizationally-aware assistants that both read appropriate data for analysis and write back changes to continuously improve the knowledge graph.[](https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e)​

### Workshop and Author Focus


The article promotes a hands-on ODSC West 2025 tutorial using OpenMetadata, MCP servers, and the Goose open-source AI agent to build extendable, fully open-source AI systems using metadata proactively. The author, Nick Acosta (Developer Advocate at Collate and OpenMetadata community advocate), will walk through use cases, architecture, and how to embed MCP into open-source metadata platforms.[](https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e)​

Context is Important, Metadata Provides It | by ODSC - Open Data Science | Medium


---

# INSTALLAZIONE

## CLAUDE CODE

Configurazione in
- ~/.claude/settings.json
- ~/Library/Application\ Support/Claude/claude_desktop_config.json

```other
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
        "AUTH_HEADER": "Bearer [REDACTED]"
      }
    }
  }
}
```

## OPENCODE

**test opencode con devstral local**

test mcp openmetadata (vedi config in claude code)

/Users/stefano/.config/opencode/opencode.json

```other
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-local-mcp-server": {
      "type": "local",
      // Or ["bun", "x", "my-mcp-command"]
      "command": ["npx", "-y", "my-mcp-command"],
      "enabled": true,
      "environment": {
        "MY_ENV_VAR": "my_env_var_value",
      },
    },
  },
}
```
