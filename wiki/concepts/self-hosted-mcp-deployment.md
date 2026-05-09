type: concept
title: Self-hosted MCP Deployment
created: 2026-02-13
updated: 2026-02-13
tags: [mcp, architecture, infrastructure]
related: [model-context-protocol, dremio-mcp-server, data-sovereignty-strategy]
sources: ["Come installare il server mcp di Dremio.md"]
---
# Self-hosted MCP Deployment

**Self-hosted MCP Deployment** refers to the architecture where the Model Context Protocol (MCP) server is hosted within a private or controlled infrastructure (such as Docker or Kubernetes) rather than relying on a managed third-party service.

This pattern is critical for the **Data Sovereignty Strategy** of the platform, as it ensures that the connection between the AI agent and the data engine (like [[dremiente]]) remains within the organization's security perimeter.

### Key Characteristics
- **Security**: Credentials like [[personal-access-token]] never leave the internal network.
- **Control**: Full control over the execution environment using tools like [[uv]] and [[kubernetes]].
- **Integration**: Allows for specialized modes like `FOR_DATA_PATTERNS` to be tuned to local data schemas.
