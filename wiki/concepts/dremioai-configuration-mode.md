type: concept
title: DremioAI Configuration Mode
created: 2026-02-13
updated: 2026-02-13
tags: [dremio, configuration, mcp]
related: [dremio-mcp-server, model-context-protocol]
sources: ["Come installare il server mcp di Dremio.md"]
---
# DremioAI Configuration Mode

**DremioAI Configuration** is a specific operational profile within the [[dremio-mcp-server]] used to define the connection parameters between the MCP server and the Dremio engine.

This configuration includes:
- **URI Endpoint**: The network address of the Dremiente instance.
- **Authentication**: The [[personal-access-token]] (PAT) required for access.

By separating the `dremioai` profile from the AI client profile (e.g., `claude`), the server allows for modular configuration of the data source and the interface.
