---
type: concept
title: AI Agent Governance
created: 2026-05-08
updated: 2026-05-08
tags: [governance, ai, mcp, security, access-control]
related: [model-context-protocol, mcp-security-best-practices, mcp-attack-surface, data-domain-governance, federated-computational-governance, data-incident-management, data-lakehouse]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# AI Agent Governance

AI Agent Governance is the framework of policies, controls, and practices for governing AI agents that access data platforms, including those using the [[model-context-protocol]] (MCP).

## Core Principles

### Shared Responsibility
MCP security is distributed across:
1. **Protocol implementer** — provides secure defaults and authentication mechanisms
2. **Infrastructure team** — configures network segmentation, firewalls, and monitoring
3. **Data platform team** — enforces governance boundaries and access controls

### Least Privilege for Agents
- Grant MCP agents the minimum permissions required for their function
- Implement tool-level access control within MCP servers
- Avoid persistent privileges across workspaces and tools

### Identity and Access Management
- Integrate MCP authentication with enterprise identity providers (e.g., Keycloak)
- Use OAuth 2.1 with PKCE for public clients
- Enforce RBAC and FGAC consistently for both human users and AI agents

## Key Challenges

### Shadow Access
As teams connect MCP servers to more sources, undocumented access paths emerge, challenging data discovery and governance. This undermines [[data-domain-governance]] and [[federated-computational-governance]] which assume controlled, governed access.

### Human Approval Workflows
For destructive or high-risk operations (e.g., deploying to production), implement challenge-response mechanisms requiring interactive human approval. This pattern is still nascent in most implementations.

### Audit and Incident Response
- Maintain tamper-proof audit logs of all agent interactions
- Develop [[data-incident-management]] procedures specific to AI system compromises
- Use audit logs to identify poisoning or injection vectors

## Relationship to Existing Governance

AI Agent Governance extends the wiki's existing governance concepts:
- [[data-domain-governance]] — domain ownership must now account for agent access
- [[federated-computational-governance]] — global standards must include agent permissions
- [[data-contract-platform]] — contracts must now specify agent permissions alongside data quality
- [[data-lakehouse]] — governance boundaries must apply equally to human and AI consumers

## Related Pages
- [[mcp-security-best-practices]] — Technical hardening strategies
- [[mcp-attack-surface]] — Threat landscape
- [[dremio-mcp-server-security]] — Concrete case study
- [[data-incident-management]] — Incident response for AI compromises