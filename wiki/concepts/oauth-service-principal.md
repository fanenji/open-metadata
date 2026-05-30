---
type: concept
title: OAuth 2.0 Service Principal Authentication
created: 2026-05-14
updated: 2026-05-14
tags: [oauth, authentication, azure, service-principal, powerbi]
related: [powerbi-connector, google-oauth, bot-authentication]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# OAuth 2.0 Service Principal Authentication

OAuth 2.0 Service Principal authentication is an Azure AD application-based authentication method used by the [[powerbi-connector|PowerBI Connector]] to access PowerBI APIs. It is the **only supported authentication type** for the PowerBI connector.

## How It Works

Instead of authenticating as a user, a Service Principal authenticates as an application identity. This involves:

1. **Registering an application** in Azure AD
2. **Granting API permissions** to the application
3. **Using application credentials** (Client ID, Client Secret, Tenant ID) to obtain access tokens

## Required Credentials

- **Client ID** — The unique identifier for the Azure AD application
- **Client Secret** — A secret key generated for the application
- **Tenant ID** — The Azure AD tenant identifier
- **Scopes** — The API permissions required (e.g., `Dashboard.Read.All`, `Dataset.Read.All`)

## Configuration Requirements

- "Allow public client flows" must be enabled in the Azure Authentication configuration.
- Tenant-related permissions must **not** be granted to the app (this can cause authorization failures).
- Admin consent must be granted for the required API permissions.

## Relationship to Other Authentication Methods

Unlike [[google-oauth|Google OAuth]], which authenticates human users via JWT tokens for the OpenMetadata UI, Service Principal authentication is designed for automated, application-to-application communication. It is conceptually similar to [[bot-authentication]], where ingestion connectors authenticate using pre-generated credentials rather than user-based SSO.
