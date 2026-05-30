---
type: concept
title: Bot Authentication
created: 2026-05-14
updated: 2026-05-14
tags: [authentication, bots, jwt, ssl, ingestion, security]
related: [hybrid-rbac-abac-model, roles-and-policies, google-oauth, ingestion-framework]
sources: ["advanced-guide-for-roles-and-policies---openmetada-20260514.md"]
---
# Bot Authentication

Bot Authentication is the mechanism by which automated applications (bots) authenticate and are authorized within the OpenMetadata security framework. This is distinct from human user authentication, which relies on SSO providers.

## How Bot Authentication Works

1. **Pre-Generated JWT Token:** Automated applications, such as the ingestion connector, are equipped with a pre-generated JWT token. This token is generated based on SSL certificates configured in OpenMetadata.
2. **Identity Establishment:** When a bot interacts with OpenMetadata server APIs, it presents its JWT token. OpenMetadata validates the token using its configured SSL certificates, thereby establishing the bot's identity.
3. **Authorization:** Once authenticated, the bot's identity is evaluated by the [[hybrid-rbac-abac-model|Hybrid RBAC-ABAC Model]] to determine what actions it can perform on which resources.

## Comparison with User Authentication

| Aspect | Human User | Bot |
|---|---|---|
| Authentication Method | SSO provider (Azure AD, Google, Okta, etc.) | Pre-generated JWT token via SSL certificates |
| Token Issuance | JWT issued upon successful SSO login | JWT pre-generated and configured |
| UI Access | Accesses OpenMetadata UI | Interacts only with server APIs |

## Role in the Authorization Framework

Bot authentication is the first factor in the three-factor authorization framework: **Who is the User**. The bot's identity, once established, is combined with the target resource's [[resource-attributes]] and the requested operation to make access decisions.

This mechanism is critical for ingestion pipelines, which run as automated processes and need to interact with OpenMetadata APIs to write metadata, lineage, and data quality results.