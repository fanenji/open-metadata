---
type: entity
title: Personal Access Token
created: 2026-05-14
updated: 2026-05-15
tags: ["openmetadata", "authentication", "api", "security", "jwt", "mcp"]
related: ["token-expiration", "token-revocation", "bot-authentication", "mcp-server", "cli-ingestion-with-basic-auth", "how-to-create-a-personal-access-token-official-doc-20260514", "hybrid-rbac-abac-model", "google-oauth"]
sources: ["how-to-create-a-personal-access-token-official-doc-20260514.md", "Embedding an MCP Server into OpenMetadata.md"]
---

# Personal Access Token

A **Personal Access Token (PAT)** is a JWT-based authentication token that embeds a user's identity and permissions, providing a secure mechanism for authenticating API requests to OpenMetadata. PATs carry the full RBAC/ABAC context of the user, so all actions performed with the token are attributed to that user and subject to their policies, roles, and inherited permissions. PATs are the primary authentication method for the [[mcp-server]] and are also used as an alternative to JWT tokens for CLI-based ingestion (see [[cli-ingestion-with-basic-auth]]).

## Key Properties

- **Identity-preserving:** The token carries the user's identity, so all actions performed with it are attributed to that user.
- **Permission-aware:** All RBAC/ABAC policies, roles, and inherited permissions associated with the user are enforced on PAT-authenticated calls.
- **Configurable expiration:** Token expiration is set when generating the token, with periods ranging from 1 hour to 60 days.
- **Generated via user profile:** Users create PATs from their profile settings under the Access Token tab.

## Creation

PATs are generated through the OpenMetadata UI via a 6-step workflow:

1. **Log in** to the OpenMetadata UI.
2. **Access your profile** by clicking the profile icon in the top-right corner and selecting *View Profile*.
3. **Open the Access Tokens tab** in your profile page.
4. **Generate a new token** by clicking *Generate New Token*.
5. **Set token expiration** by choosing one of the available periods: 1 hour, 1 day, 7 days, 30 days, or 60 days.
6. **Copy your token** — the token is displayed only once after generation. Copy and securely store it immediately.

## Expiration

PATs have a configurable time-to-live. Available expiration periods are:

| Period   | Use Case                                           |
|----------|----------------------------------------------------|
| 1 hour   | Short-lived automation tasks, testing              |
| 1 day    | Daily batch jobs, development sessions             |
| 7 days   | Weekly reporting, short-term integrations          |
| 30 days  | Monthly maintenance, moderate-term automation      |
| 60 days  | Long-term development, stable integrations         |

See [[token-expiration]] for a detailed discussion of expiration strategies and best practices.

## Revocation

PATs can be revoked at any time via the UI by selecting *Revoke Token* in the Access Tokens tab. Revocation immediately invalidates the token, preventing further API requests using that token. See [[token-revocation]] for implications and best practices.

## Usage

Include the PAT in the `Authorization` header of API requests:

```
Authorization: Bearer <your_personal_access_token>
```

## Use Cases

- **MCP Server authentication** — LLM clients (Claude Desktop, Goose, ChatGPT) connect to the embedded MCP server using a PAT, ensuring AI interactions respect the user's access controls.
- **CLI-based ingestion** — Used in pipeline workflow configs for automated metadata ingestion, as an alternative to JWT tokens.
- **API automation** — Scripts and tools that interact with OpenMetadata's REST APIs programmatically.

## Relationship to Other Auth Mechanisms

- **[[bot-authentication|Bot Tokens]]**: Both are JWT-based, but bot tokens are scoped to service accounts for automated pipelines (ingestion connectors) and are pre-generated based on SSL certificates, while PATs are user-specific and carry the full RBAC/ABAC context of a human user.
- **[[mcp-server]]**: PATs are the primary authentication mechanism for the MCP Server, enabling AI assistants to access the OpenMetadata knowledge graph with user identity preserved.
- **[[cli-ingestion-with-basic-auth]]**: PATs serve as an alternative to JWT tokens for CLI-based ingestion authentication, configured via the `securityConfig` YAML block.

## Open Questions

- What is the token's internal JWT structure (claims, signing mechanism)?
- Can PATs be scoped to specific permissions or resources?
- Is there a maximum number of active PATs per user?
- What happens to active API sessions when a token is revoked?
- Are there audit logs for PAT creation/revocation events?