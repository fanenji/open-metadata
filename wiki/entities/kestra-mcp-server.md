---
type: entity
title: Kestra Python MCP Server
created: 2026-04-29
updated: 2026-04-29
tags: [kestra, mcp, model-context-protocol, ai-agents, workflow-orchestration]
related: [kestra, model-context-protocol, mcp-server-for-workflow-orchestration, dbt-mcp-server, dremio-mcp-server]
sources: ["kestra-mcp-server-python.md"]
---
# Kestra Python MCP Server

The official [[model-context-protocol]] server for [[kestra]], enabling AI agents to interact with Kestra workflows through natural language. It exposes Kestra's API as a set of MCP tools that can be invoked from AI-powered IDEs and chat interfaces.

## Key Features

- **Docker-based deployment** — Primary distribution via `ghcr.io/kestra-io/mcp-server-python:latest`
- **Dual authentication** — Username/password for OSS, API token for Enterprise/Cloud
- **Tool groups** — backfill, execution, files, flow, kv, logs, namespace, replay, restart, resume
- **Configurable toolset** — Disable specific tools via `KESTRA_MCP_DISABLED_TOOLS`
- **stdio transport** — JSON-RPC communication over stdin/stdout

## Usage

Configure in Cursor, Windsurf, VS Code, or Claude Desktop MCP settings. The server runs as a subprocess managed by the IDE.

## Related

- [[kestra]] — The orchestration platform
- [[model-context-protocol]] — The protocol standard
- [[mcp-server-for-workflow-orchestration]] — Broader pattern