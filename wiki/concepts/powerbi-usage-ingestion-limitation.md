---
type: concept
title: PowerBI Usage Ingestion Limitation
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, usage, ingestion, limitation, service-principal]
related: [powerbi-connector, oauth-service-principal, data-observability-alerts]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# PowerBI Usage Ingestion Limitation

The PowerBI Usage Ingestion Limitation is an explicitly documented constraint of the [[powerbi-connector|PowerBI Connector]]: OpenMetadata **cannot ingest PowerBI usage data**.

## Cause

The Power BI Usage API does not support [[oauth-service-principal|Service Principal authentication]]. Since Service Principal is the only authentication method supported by the PowerBI connector, usage data is fundamentally inaccessible through this integration.

## Impact

- **No Usage Metrics**: Dashboard view counts, report usage statistics, and other usage-related metadata cannot be ingested into OpenMetadata.
- **Data Observability Gap**: Features relying on usage data, such as popularity metrics and certain [[data-observability-alerts]], will not include PowerBI assets.
- **No Workaround**: This is a limitation imposed by Microsoft's API design, not an OpenMetadata connector limitation.

## Context

This limitation is specific to PowerBI. Other connectors in the [[openmetadata-connectors]] library may support usage ingestion where the source system's API permits it.
