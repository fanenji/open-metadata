---
type: concept
title: dbt MCP Server Setup Guide
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, mcp, setup, configuration]
related: [dbt-mcp-server, dbt-mcp-server-deployment-modes, dbt-cloud, dbt-core, model-context-protocol]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# dbt MCP Server Setup Guide

This guide covers the three deployment paths for the [[dbt-mcp-server]].

## Prerequisites

- `uv` installed (Python package manager from Astral)
- A dbt project directory
- (Optional) A [[dbt-cloud]] account for platform features

## Path A — Local MCP + dbt Platform (Recommended for Engineers)

Full CLI access + platform APIs. Ideal for actively building dbt models.

### Step 1: Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Find Your dbt Cloud Host URL

Log into dbt Cloud → Account Settings → Access URLs. Copy your Access URL (e.g., `abc123.us1.dbt.com`).

### Step 3: Configure MCP Client

**Claude Desktop:**
```json
{
  "mcpServers": {
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_HOST": "YOUR-ACCESS-URL",
        "DBT_PROJECT_DIR": "/path/to/your/dbt/project",
        "DBT_PATH": "/path/to/your/dbt/executable"
      }
    }
  }
}
```

**Claude Code (CLI):**
```bash
claude mcp add dbt \
  -e DBT_HOST=abc123.us1.dbt.com \
  -e DBT_PROJECT_DIR=/path/to/project \
  -- uvx dbt-mcp
```

**Cursor:** Settings → MCP → Add new global MCP server → paste same config into `mcp.json`.

**VS Code:** Settings → search `mcp` → Edit in settings.json → add `mcpServers` block.

### Step 4: Authenticate

First platform-connected tool invocation triggers OAuth browser flow. Credentials are stored securely.

### Step 5: Verify

Ask: "What dbt models are in my project?" The AI should call `get_all_models` and return actual model names.

## Path B — Local MCP, No dbt Cloud (dbt Core Users)

Full CLI access without cloud features:

```json
{
  "mcpServers": {
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_PROJECT_DIR": "/path/to/your/dbt/project",
        "DBT_PATH": "/path/to/your/dbt/executable"
      }
    }
  }
}
```

No `DBT_HOST` required. CLI tools + local discovery from `manifest.json` available. No Semantic Layer or Admin API.

## Path C — Remote MCP, Zero Install (Analysts and Consumers)

1. Obtain remote MCP endpoint URL from dbt Cloud account admin (Account Settings → Integrations → MCP)
2. Configure in MCP client
3. Authenticate via OAuth
4. Start querying immediately — `list_metrics`, `query_metrics`, `text_to_sql`, `get_lineage` available

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `DBT_HOST` | For platform features | dbt Cloud Access URL |
| `DBT_PROJECT_DIR` | Yes | Path to dbt project |
| `DBT_PATH` | For CLI | Path to dbt executable |
| `DISABLE_DBT_CLI` | Optional | Set `true` to disable CLI tools in production |

## Security Best Practices

- Store sensitive variables in `.env` file, reference with `--env-file /path/to/.env`
- Never hardcode tokens in `mcp.json`
- Use `DISABLE_DBT_CLI=true` in production consumption setups
- Pin `dbt-mcp` version (`uvx dbt-mcp==0.2.6`) to avoid breaking changes