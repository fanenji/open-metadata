---
type: concept
title: OAuth 2.0 Service Principal Authentication
created: 2026-05-14
updated: 2026-05-14
tags: [authentication, azure-ad, oauth, security]
related: [powerbi-connector, azure-ad-service-principal, bot-authentication, service-connection]
sources: ["powerbi-connector-openmetadata-integration-documen-20260514.md"]
---

# OAuth 2.0 Service Principal Authentication

OAuth 2.0 Service Principal authentication is the authentication method used by the [[powerbi-connector|PowerBI Connector]] to access PowerBI APIs. It uses an Azure AD application identity (service principal) rather than a user account.

## Components

- **Client ID** — The application (client) ID of the Azure AD app
- **Client Secret** — A secret key generated for the Azure AD app
- **Tenant ID** — The directory (tenant) ID of the Azure AD instance
- **Scope** — The API scope URL (e.g., `https://analysis.windows.net/powerbi/api/.default`)
- **Authority URI** — The token authority URL (default `https://login.microsoftonline.com/`)

## Limitations

- PowerBI Usage API does not support Service Principal authentication, so usage ingestion is not available
- Service principal ignores default user workspaces (e.g., "My Workspace")

## Configuration

The service principal must be granted API permissions in Azure AD:
- `Dashboard.Read.All` (required)
- `Dataset.Read.All` (optional, for datamodel and lineage processing)

Additionally, the PowerBI Admin must enable "Allow service principals to use PowerBI APIs" in the PowerBI Admin console.