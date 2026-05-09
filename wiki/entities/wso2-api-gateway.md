---
type: entity
title: WSO2 API Gateway
created: 2026-05-07
updated: 2026-05-07
tags: [api-gateway, interoperability, api-management]
related: [ckan-portal, pdnd-interoperability, dremio, dremio-vds-pds]
sources: ["Sintesi Architettura (Claude).md"]
---
# WSO2 API Gateway

WSO2 is the API management platform used for interoperability with external systems and the Italian National Digital Data Platform (PDND) in the Regione Liguria Data Platform.

## Role in Architecture

WSO2 provides the API endpoint layer for external consumption of platform data. It manages authentication, rate limiting, and API lifecycle for REST endpoints that expose data from [[dremio]]'s virtualization layer and the [[ckan-portal]] open data catalog.

## Key Features

- **API Management**: Full lifecycle management of APIs (design, publish, version, retire)
- **Authentication**: OAuth2, OpenID Connect, and API key-based access control
- **Rate Limiting**: Throttling and quota management for API consumers
- **Interoperability**: Integration with [[pdnd-interoperability|PDND]] for national-level data exchange
- **Analytics**: Usage monitoring and reporting

## Related Standards

- [[dcat-ap-agid-compliance]]: Metadata standards for open data
- [[pdnd-interoperability]]: Italian National Digital Data Platform integration