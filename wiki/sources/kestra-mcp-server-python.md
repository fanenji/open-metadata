---
type: source
title: "Kestra Python MCP Server"
created: 2026-04-29
updated: 2026-04-29
tags: [kestra, mcp, model-context-protocol, workflow-orchestration, ai-agents]
related: [kestra, model-context-protocol, kestra-mcp-server, mcp-server-for-workflow-orchestration, dbt-mcp-server, dremio-mcp-server]
sources: ["kestra-mcp-server-python.md"]
---
# Kestra Python MCP Server

The official Python MCP server for [[kestra]], enabling AI agents to interact with Kestra workflows via natural language through the [[model-context-protocol]].

## Overview

The Kestra Python MCP Server provides a bridge between AI-powered IDEs and chat interfaces (Cursor, Windsurf, VS Code, Claude Desktop) and the Kestra workflow orchestration platform. It exposes Kestra's API as a set of MCP tools that AI agents can invoke to manage flows, executions, logs, and other orchestration resources.

## Deployment

The primary deployment method is via Docker, using the image `ghcr.io/kestra-io/mcp-server-python:latest`. Configuration is done through environment variables passed to the container.

### OSS Configuration

For open-source Kestra installations, authentication uses username and password:

```json
{
  "mcpServers": {
    "kestra": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm", "--pull", "always",
        "-e", "KESTRA_BASE_URL",
        "-e", "KESTRA_TENANT_ID",
        "-e", "KESTRA_MCP_DISABLED_TOOLS",
        "-e", "KESTRA_MCP_LOG_LEVEL",
        "-e", "KESTRA_USERNAME",
        "-e", "KESTRA_PASSWORD",
        "ghcr.io/kestra-io/mcp-server-python:latest"
      ],
      "env": {
        "KESTRA_BASE_URL": "http://host.docker.internal:8080/api/v1",
        "KESTRA_TENANT_ID": "main",
        "KESTRA_MCP_DISABLED_TOOLS": "ee",
        "KESTRA_MCP_LOG_LEVEL": "ERROR",
        "KESTRA_USERNAME": "admin@kestra.io",
        "KESTRA_PASSWORD": "your_password"
      }
    }
  }
}
```

### Enterprise Configuration

For Kestra Enterprise Edition or Cloud, authentication uses an API token:

```json
{
  "mcpServers": {
    "kestra": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm", "--pull", "always",
        "-e", "KESTRA_BASE_URL",
        "-e", "KESTRA_API_TOKEN",
        "-e", "KESTRA_TENANT_ID",
        "-e", "KESTRA_MCP_LOG_LEVEL",
        "ghcr.io/kestra-io/mcp-server-python:latest"
      ],
      "env": {
        "KESTRA_BASE_URL": "http://host.docker.internal:8080/api/v1",
        "KESTRA_API_TOKEN": "<your_kestra_api_token>",
        "KESTRA_TENANT_ID": "main",
        "KESTRA_MCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

### Networking Notes

- On macOS and Windows, `host.docker.internal` allows the container to access services on the host machine.
- On Linux, host network mode or a custom Docker bridge is required.

## Available Tools

The MCP server exposes the following tool groups:

- **backfill** — Trigger backfill operations
- **ee** — Enterprise Edition tools (only available in EE/Cloud)
- **execution** — Manage and inspect executions
- **files** — Handle namespace files
- **flow** — Manage flows (list, create, update, delete)
- **kv** — Key-value store operations
- **logs** — Retrieve execution logs
- **namespace** — Manage namespaces
- **replay** — Replay executions
- **restart** — Restart executions
- **resume** — Resume paused executions

## Configuration Options

- `KESTRA_MCP_DISABLED_TOOLS` — Comma-separated list of tools to disable (e.g., `ee` or `files`)
- `KESTRA_MCP_LOG_LEVEL` — Logging verbosity: `ERROR` (default), `WARNING`, `INFO`, `DEBUG`

## Local Development

For extending the server with custom tools, use `uv` for local development:

```bash
uv venv --python 3.13
uv pip install -r requirements.txt
```

## Transport

The server uses `stdio` transport, communicating via JSON-RPC messages over standard input/output streams. AI IDEs launch the MCP server as a subprocess automatically.

## Related Pages

- [[kestra]] — The workflow orchestration platform
- [[model-context-protocol]] — The protocol standard
- [[mcp-server-for-workflow-orchestration]] — Broader pattern for AI-orchestration interfaces
- [[dbt-mcp-server]] — Comparable MCP server for dbt
- [[dremio-mcp-server]] — Comparable MCP server for Dremio