---
type: concept
title: MCP Security Best Practices
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, best-practices, hardening, ai-governance]
related: [model-context-protocol, mcp-attack-surface, dremio-mcp-server-security, ai-agent-governance, data-incident-management]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# MCP Security Best Practices

Consolidated hardening strategies for deploying [[model-context-protocol]] (MCP) servers in production environments.

## Authentication and Authorization
- **OAuth 2.1 with PKCE**: Mandated standard for HTTP-based MCP. PKCE is non-negotiable for public clients (IDE extensions, CLI tools).
- **Client ID Metadata (CIMD)**: Use the "pull" verification flow from the November 2025 spec update.
- **Token Validation**: Rigorously validate tokens (signature, expiry, issuer, audience, scopes) to prevent replay attacks and scope escalation.
- **RBAC Integration**: Integrate with an identity provider (e.g., Keycloak) to enforce granular permissions at the tool level.

## Network Architecture and Segmentation
- **Network Isolation**: Deploy MCP servers in segmented network zones, isolated from general corporate networks.
- **Private Connectivity**: Use AWS PrivateLink or Google Cloud Private Service Connect to keep traffic off the public internet.
- **Firewalls and IP Whitelisting**: Configure firewalls for necessary traffic only. IP whitelisting adds a critical layer of control with minimal performance impact (~0.1ms).

## Credential and Secrets Management
- **Centralized Secrets**: Use centralized credential management systems. Never rely on plaintext environment variables or local configuration files.
- **Secure Configuration Storage**: Treat MCP configuration files (e.g., `claude_desktop_config.json`) as highly sensitive artifacts with strict access controls and encryption.

## Monitoring, Auditing, and Incident Response
- **Comprehensive Logging**: Log all MCP interactions, including authentication attempts, tool invocations, and data access patterns.
- **Audit Trails**: Retain audit logs in a tamper-proof environment for compliance and forensics.
- **Alerting**: Deploy real-time monitoring with intelligent alerting for unauthorized access attempts or anomalous tool usage.
- **Incident Response**: Develop and test [[data-incident-management]] procedures specific to AI system compromises.

## Resource Management and Input Validation
- **Rate Limiting**: Implement rate limiting and resource constraints to prevent abuse.
- **Input Validation**: Harden all MCP tool inputs against injection attacks. Sanitize parameters interpreted by downstream systems (Shell, SQL, etc.).
- **Human Approval Workflows**: For destructive or high-risk operations, implement a challenge-response mechanism requiring interactive human approval.

## Shared Responsibility Model

MCP security is a shared responsibility between:
1. **Protocol implementer** — provides secure defaults and authentication mechanisms
2. **Infrastructure team** — configures network segmentation, firewalls, and monitoring
3. **Data platform team** — enforces governance boundaries and access controls

## Related Pages
- [[mcp-attack-surface]] — The threat landscape
- [[dremio-mcp-server-security]] — Concrete case study
- [[ai-agent-governance]] — Broader governance framework