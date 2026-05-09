---
type: entity
title: Dremio Cloud Edition (Next Generation)
created: 2026-05-09
updated: 2026-05-09
tags: [dremio, cloud, managed-service, production-readiness]
related: [dremio, dremio-mcp-server, model-context-protocol, ai-agent-integration-risk-framework]
sources: ["research-the-source-does-not-clarify-whether-the-dremio-mcp-2026-05-09.md"]
---

# Dremio Cloud Edition (Next Generation)

Dremio Cloud (Next Generation) is the managed cloud service edition of the [[dremio]] data lakehouse platform. It is distinct from the self-managed (open source) edition in terms of support, SLAs, and feature availability.

## Key Characteristics

- **Managed Service:** Infrastructure, governance, and troubleshooting are handled by Dremio.
- **MCP Server Hosting:** The [[dremio-mcp-server]] is available as a hosted managed service for Cloud customers, with OAuth-based integration.
- **Support Model:** Covered by Dremio Support Policies, unlike the self-managed OSS version.
- **Feature Matrix:** The Dremio Cloud edition feature matrix lists the MCP Server as "OSS and Dremio-hosted" with a recommendation for the hosted version. However, the GA/Preview status of the MCP Server feature is ambiguous.

## Production Readiness

The Cloud-hosted MCP server is conditionally production-ready. It reduces operational burden and aligns with Dremio platform SLAs, but it is brand new. Launch materials describe it as "just the beginning", indicating ongoing maturation. Enterprise customers should validate GA status and specific SLAs directly with Dremio.

## Related

- [[dremio]] — The underlying data lakehouse platform.
- [[dremio-mcp-server]] — The MCP server component, available in both self-managed and cloud-hosted variants.
- [[model-context-protocol]] — The protocol standard the server implements.