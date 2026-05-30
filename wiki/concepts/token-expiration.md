---
type: concept
title: Token Expiration
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, authentication, security, tokens]
related: [personal-access-token, token-revocation, bot-authentication]
sources: ["how-to-create-a-personal-access-token-official-doc-20260514.md"]
---

# Token Expiration

**Token expiration** is a security mechanism that limits the validity period of authentication tokens, reducing the window of exposure if a token is compromised. In OpenMetadata, Personal Access Tokens (PATs) have a configurable time-to-live (TTL) that can be set at creation time.

## Available Expiration Periods

OpenMetadata PATs support the following expiration periods:

| Period | Typical Use Case |
|--------|------------------|
| 1 hour | Short-lived automation tasks, CI/CD pipelines, testing |
| 1 day | Daily batch jobs, development sessions |
| 7 days | Weekly reporting, short-term integrations |
| 30 days | Monthly maintenance, moderate-term automation |
| 60 days | Long-term development, stable integrations |

## Best Practices

- **Use the shortest practical expiration** for the intended use case. Shorter-lived tokens reduce risk if a token is leaked.
- **Rotate tokens regularly** even for long-lived use cases. Consider regenerating tokens before they expire to avoid service disruption.
- **Store tokens securely** — the token is displayed only once after generation. Use a secrets manager or environment variables rather than hardcoding.
- **Revoke compromised tokens immediately** via the UI. See [[token-revocation]].

## Relationship to Other Concepts

- [[personal-access-token]] — The entity that implements token expiration.
- [[token-revocation]] — The complementary mechanism for invalidating tokens before their expiration.
- [[bot-authentication]] — Bot tokens may have different expiration policies; this is not yet documented.