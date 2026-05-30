---
type: concept
title: Token Revocation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, authentication, security, tokens]
related: [personal-access-token, token-expiration, audit-logs]
sources: ["how-to-create-a-personal-access-token-official-doc-20260514.md"]
---

# Token Revocation

**Token revocation** is the ability to invalidate an authentication token before its scheduled expiration, rendering it unusable for future API requests. In OpenMetadata, Personal Access Tokens (PATs) can be revoked at any time via the UI.

## Workflow

1. Navigate to the user profile page.
2. Open the **Access Tokens** tab.
3. Locate the token to revoke and click **Revoke Token**.

Revocation is immediate. Once revoked, any API request using that token will be rejected.

## Implications

- **Active sessions**: API requests in progress at the time of revocation may complete, but new requests will fail. The exact behavior depends on the API endpoint and request lifecycle.
- **Dependent services**: Any service, script, or integration using the revoked token will lose access until a new token is generated and configured.
- **Audit trail**: It is unclear whether PAT creation and revocation events are logged in the [[audit-logs]] system. This is an open question.

## Best Practices

- **Revoke immediately** if a token is suspected to be compromised.
- **Rotate tokens proactively** before expiration to avoid service disruption.
- **Maintain a token inventory** — track which tokens are used by which services to quickly identify impacted systems during revocation.
- **Test revocation** in a non-production environment to understand the impact on dependent services.

## Relationship to Other Concepts

- [[personal-access-token]] — The entity that can be revoked.
- [[token-expiration]] — The complementary mechanism that automatically invalidates tokens after a set period.
- [[audit-logs]] — Potential source of revocation event records (open question).