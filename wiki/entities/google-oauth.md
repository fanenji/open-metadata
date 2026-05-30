---
type: entity
title: Google OAuth
created: 2026-05-14
updated: 2026-05-14
tags: [authentication, oauth, security, openmetadata]
related: [openmetadata, openmetadata-code-layout]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# Google OAuth

Google OAuth is the default authentication provider used by OpenMetadata. All incoming API requests are authenticated by validating JWT tokens against the Google OAuth provider.

## Role in OpenMetadata

- **Authentication**: Validates JWT tokens on every incoming request to verify user identity.
- **Configuration**: Authentication settings are defined in `conf/openmetadata.yaml`.
- **Authorization**: Works alongside the Authorizer component, which handles access control decisions after authentication succeeds.

## Context

Google OAuth is referenced in the [[openmetadata-code-layout|code layout documentation]] as the primary authentication mechanism. In production deployments, OpenMetadata can also integrate with other identity providers (such as Keycloak, Azure AD, Okta) through its extensible authentication framework, but Google OAuth serves as the default implementation in the open-source codebase.