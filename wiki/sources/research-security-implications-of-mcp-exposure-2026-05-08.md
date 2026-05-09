type: source
title: "Research: Security Implications of MCP Exposure"
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, ai-governance, dremio, model-context-protocol]
related: [model-context-protocol, dremio-mcp-server, dbt-mcp-server, data-lakehouse, data-incident-management, context-propagation, mcp-security-best-practices, mcp-attack-surface, dremio-mcp-server-security, ai-agent-governance]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Research: Security Implications of MCP Exposure

## Overview

This synthesis examines the documented security implications of exposing [[model-context-protocol]] (MCP) servers to networks. It reviews the attack surface through recent research from multiple security vendors (Knostic, Trend Micro, Backslash Security, Checkmarx, Palo Alto Networks, Upwind, Truefoundry, Descope, Red Hat, Onehouse, InsightFinder), analyzes the specific case of the [[dremio-mcp-server]], and outlines hardening strategies for production deployments.

## Key Findings

- **Widespread network exposure without authentication**: Knostic found 100% of ~2,000 verified servers lacked auth; Trend Micro confirmed 492 instances.
- **Overscoping** is the most pervasive default risk, enabling OS command injection and path traversal.
- **Credential management** is systematically poor — plaintext storage in config files and environment variables.
- **The Dremio MCP server** has a strong native security model (OAuth 2.0, RBAC, FGAC, audit logs) but real-world misconfigurations create critical gaps.
- **LLM-specific threats** (prompt injection, context poisoning) are not addressed by traditional security frameworks.

## Connections

This source directly extends the wiki's coverage of [[model-context-protocol]] with a security dimension, provides a case study for [[dremio-mcp-server]], and introduces new concepts including [[mcp-attack-surface]], [[mcp-security-best-practices]], [[dremio-mcp-server-security]], and [[ai-agent-governance]].

## References

1. [MCP Security Issues and Best Practices You Need to Know](https://www.knostic.ai/blog/mcp-security) — knostic.ai
2. [MCP Server Security Best Practices to Prevent Risk](https://www.descope.com/blog/post/mcp-server-security-best-practices) — descope.com
3. [Securing MCP Servers for Enterprise Use: Beyond HTTPS Protocol](https://medium.com/dbasolved/securing-mcp-servers-for-enterprise-use-beyond-https-protocol-bdcd731e0801) — medium.com
4. [How to Harden Your MCP Server - InsightFinder AI](https://insightfinder.com/blog/mcp-server-security-guide/) — insightfinder.com
5. [MCP Security Risks & Best Practices in 2026 - Truefoundry](https://www.truefoundry.com/blog/mcp-security-risks-bestpractices) — truefoundry.com
6. [MCP Authorization Error - Dremio](https://community.dremio.com/t/mcp-authorization-error/13262) — community.dremio.com
7. [MCP Server Data Exploration with Dremio's Agentic Lakehouse](https://www.dremio.com/blog/dremio-mcp-server-now-hosted-in-dremios-next-generation-cloud/) — dremio.com
8. [Agentic AI with Dremio | Dremio](https://www.dremio.com/agenticai/) — dremio.com
9. [MCP Authentication & Authorization Pain Points](https://medium.com/@mustafaturan/mcp-authentication-authorization-pain-points-5506e63dd799) — medium.com
10. [MCP security: Implementing robust authentication and authorization](https://www.redhat.com/en/blog/mcp-security-implementing-robust-authentication-and-authorization) — redhat.com
11. [Update on Exposed MCP Servers: The Threat Widens to the Cloud | Trend Micro (TR)](https://www.trendmicro.com/vinfo/tr/security/news/vulnerabilities-and-exploits/update-on-exposed-mcp-servers-the-threat-widens-to-the-cloud) — trendmicro.com
12. [MCP Security Exposed: What You Need to Know Now | Palo Alto Networks](https://live.paloaltonetworks.com/t5/community-blogs/mcp-security-exposed-what-you-need-to-know-now/ba-p/1227143) — live.paloaltonetworks.com
13. [11 Emerging AI Security Risks with MCP (Model Context Protocol) - Checkmarx](https://checkmarx.com/zero-post/11-emerging-ai-security-risks-with-mcp-model-context-protocol/) — checkmarx.com
14. [Securing Your Data Lakehouse: Best Practices for Data Encryption, Access Control, and Compliance](https://www.onehouse.ai/blog/securing-your-data-lakehouse-best-practices-for-data-encryption-access-control-and-compliance) — onehouse.ai
15. [Unpacking the Security Risks of Model Context Protocol (MCP) Servers - Upwind](https://www.upwind.io/feed/unpacking-the-security-risks-of-model-context-protocol-mcp-servers) — upwind.io