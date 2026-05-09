type: entity
title: Power BI Modeling MCP Server
created: 2026-04-29
updated: 2026-04-29
tags: [power-bi, mcp, microsoft, ai-assisted-development]
related: [model-context-protocol, opencode, local-llm-for-bi-development, dbt-mcp-server]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
---
# Power BI Modeling MCP Server

Microsoft's official Model Context Protocol (MCP) server that exposes Power BI semantic model operations to AI agents. It enables AI-assisted development of Power BI semantic models, including DAX generation, measure analysis, relationship inspection, and documentation.

## Key Features

- **Read-only mode** (`--readonly`): Inspect semantic models without modification
- **Read-write mode** (`--readwrite`): Modify models with user confirmation via the MCP Elicitation protocol
- **Skip confirmation** (`--skipconfirmation`): For experienced users who want to bypass prompts
- **Standalone executable**: Distributed as a VSIX extension but can be extracted and run independently

## Installation

The server is distributed as a VSIX file from the Visual Studio Marketplace. To use it standalone:
1. Download the VSIX from [aka.ms/powerbi-modeling-mcp-vscode](https://aka.ms/powerbi-modeling-mcp-vscode)
2. Rename `.vsix` to `.zip` and extract
3. The executable is at `extension\server\powerbi-modeling-mcp.exe`

## Usage with OpenCode

Configured in OpenCode's `opencode.json` as an MCP server:

```json
"mcp": {
  "powerbi-modeling": {
    "type": "local",
    "command": [
      "C:\\MCPServers\\PowerBIModelingMCP\\extension\\server\\powerbi-modeling-mcp.exe",
      "--start",
      "--readonly"
    ],
    "enabled": true
  }
}
```

## Practical Workflows

- Model structure overview and relationship analysis
- DAX measure generation and review
- Documentation generation in markdown
- Naming convention audits
- Inactive relationship analysis

## Limitations

- Windows-only (depends on Power BI Desktop)
- Requires Power BI Desktop running with a PBIX file loaded
- First connection requires user approval via the Elicitation protocol

## See Also

- [[model-context-protocol]] — The protocol this server implements
- [[opencode]] — The AI agent that orchestrates this server
- [[local-llm-for-bi-development]] — The architecture pattern this enables
- [[dbt-mcp-server]] — A parallel MCP server for dbt projects