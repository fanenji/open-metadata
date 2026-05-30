---
type: source
title: "How to Create a Personal Access Token | Official Documentation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, authentication, api, security]
related: [personal-access-token, token-expiration, token-revocation, bot-authentication, mcp-server, cli-ingestion-with-basic-auth]
sources: ["how-to-create-a-personal-access-token-official-doc-20260514.md"]
---

# How to Create a Personal Access Token | Official Documentation - OpenMetadata Documentation

**Source:** [OpenMetadata Documentation v1.12.x](https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/personal-access-token)

## Summary

This official documentation page provides a step-by-step procedural guide for creating Personal Access Tokens (PATs) in OpenMetadata v1.12.x. PATs are JWT-based authentication tokens that allow users to securely authenticate and interact with the OpenMetadata API. The guide covers prerequisites, a 6-step creation workflow, token expiration options (1 hour to 60 days), revocation capability, and usage instructions for API requests.

## Key Points

- PATs provide a secure, user-specific authentication mechanism for the OpenMetadata API.
- The creation workflow is a straightforward 6-step UI process: Login → Profile → Access Tokens tab → Generate New Token → Set expiration → Copy token.
- Expiration options: 1 hour, 1 day, 7 days, 30 days, 60 days.
- Tokens can be revoked at any time via the UI.
- The token is displayed only once after generation — users must copy and securely store it immediately.
- Usage requires including the token in the `Authorization` header as `Authorization: Bearer <token>`.

## Relevance to Wiki

This source provides the official procedural documentation for [[personal-access-token]] creation, strengthening that entity page with concrete steps. It also introduces the concepts of [[token-expiration]] and [[token-revocation]], which are not yet documented as dedicated concept pages. The source is directly related to [[bot-authentication]] (both are token-based auth mechanisms), [[mcp-server]] (PATs are the primary auth mechanism for MCP Server), and [[cli-ingestion-with-basic-auth]] (PATs are an alternative to JWT tokens for CLI authentication).

## Open Questions

- What is the token's internal structure (JWT claims, signing mechanism)?
- Can PATs be scoped to specific permissions or resources?
- Is there a maximum number of active PATs per user?
- What happens to active API sessions when a token is revoked?
- Are there audit logs for PAT creation/revocation events?