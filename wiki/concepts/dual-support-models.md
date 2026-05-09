---
type: concept
title: Dual Support Models
created: 2026-05-09
updated: 2026-05-09
tags: [production-readiness, support, governance, ai-agents]
related: [dremio-mcp-server, dremio-cloud-edition, ai-agent-integration-risk-framework, model-context-protocol]
sources: ["research-the-source-does-not-clarify-whether-the-dremio-mcp-2026-05-09.md"]
---

# Dual Support Models

The concept of Dual Support Models refers to the situation where the same software component has radically different support obligations and risk profiles depending on the deployment model (self-managed open source vs. cloud-hosted managed service).

## Key Characteristics

- **Self-Managed (OSS):** Community support only; no vendor SLAs; user bears full operational responsibility.
- **Cloud-Hosted (Managed):** Vendor-supported; covered by platform SLAs; reduced operational burden.

## Relevance to the Data Platform

The [[dremio-mcp-server]] is a prime example. Its production readiness cannot be assessed without first determining the deployment model. The same codebase is experimental in one context and conditionally production-ready in another.

## Implications

- Enterprise procurement and architecture decisions must explicitly account for the deployment model.
- Marketing materials may conflate the two models, creating a risk of misinterpretation.
- Governance and security requirements differ significantly between the two models.