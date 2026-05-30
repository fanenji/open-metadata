---
type: source
title: "PowerBI Connector | OpenMetadata Integration Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, connector, dashboard, ingestion, lineage, oauth]
related: [powerbi-connector, openmetadata-connectors, data-lineage, metadata-ingestion-workflow, service-connection]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi"
---
# PowerBI Connector | OpenMetadata Integration Documentation

Official documentation for the PowerBI connector in OpenMetadata v1.12.x. This source covers the complete setup and configuration of the PowerBI dashboard connector, including requirements, authentication, API mode selection, metadata ingestion, and lineage configuration.

## Key Points

- **Authentication**: Only OAuth 2.0 Service Principal authentication is supported, using Azure AD application credentials (Client ID, Client Secret, Tenant ID).
- **License Requirement**: A PowerBI Pro license is mandatory for API access.
- **API Modes**: Users must choose between Admin APIs (full workspace coverage, unrestricted lineage via Scan Result API) and Non-Admin APIs (limited to assigned workspaces, lineage restricted to Push Datasets only).
- **Lineage**: Dashboard lineage from database tables requires adding the corresponding database service name during configuration.
- **Limitations**: PowerBI dataflows are not supported. Usage ingestion is not supported because the Power BI Usage API does not support Service Principal authentication.

## Connections to Wiki

This source documents a specific connector within the [[openmetadata-connectors]] library. It provides a concrete example of [[data-lineage|dashboard lineage]] configuration and follows the standard [[metadata-ingestion-workflow]] for creating [[service-connection|service connections]].
