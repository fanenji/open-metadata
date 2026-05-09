---
type: concept
title: PDND Interoperability
created: 2026-05-07
updated: 2026-05-07
tags: [interoperability, public-administration, api, national-platform]
related: [wso2-api-gateway, ckan-portal, dcat-ap-agid-compliance, dremio, data-federation-for-sensitive-data]
sources: ["Sintesi Architettura (Claude).md"]
---
# PDND Interoperability

PDND (Piattaforma Digitale Nazionale Dati) is the Italian National Digital Data Platform that enables data sharing between public administrations. The Regione Liguria Data Platform must integrate with PDND for cross-administration data exchange.

## Purpose

PDND provides a standardized infrastructure for:
- **Data Discovery**: Finding datasets available from other public administrations
- **Data Access**: Requesting and receiving data through standardized APIs
- **Interoperability**: Ensuring technical and semantic compatibility between systems

## Integration Architecture

The platform integrates with PDND through:
- **[[wso2-api-gateway]]**: Manages API exposure and consumption, handles authentication and authorization required by PDND
- **[[ckan-portal]]**: Publishes dataset metadata in formats consumable by PDND
- **[[dremio]]**: Provides the data access layer for fulfilling PDND data requests

## Related Standards

- [[dcat-ap-agid-compliance]]: Metadata standards that PDND consumes for dataset discovery
- [[data-federation-for-sensitive-data]]: Pattern for querying across separate systems without moving data, relevant for PDND integration