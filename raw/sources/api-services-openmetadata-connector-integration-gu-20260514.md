---
type: clip
title: "API Services | OpenMetadata Connector Integration Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/api"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# API Services | OpenMetadata Connector Integration Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/api

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAPIAPI Services | OpenMetadata Connector Integration GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIOverviewRESTDatabaseDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageAPI ServicesOverviewSupported FeaturesUse CasesBest PracticesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​API Services

​Overview

The OpenMetadata API service facilitates metadata ingestion from RESTful APIs that expose OpenAPI (Swagger) specifications. This connector is particularly useful for integrating custom services or third-party tools that are not natively supported by OpenMetadata.

This is the supported list of connectors for API Services:

REST PROD

​Supported Features

Metadata Ingestion: Extracts metadata from services exposing OpenAPI JSON schemas.

Custom Integration: Allows integration with bespoke systems through standardized API definitions.

Flexible Deployment: Supports both UI-based and CLI-based ingestion workflows.

​Use Cases

Custom Application Integration: Ingest metadata from proprietary applications exposing OpenAPI specifications.

Third-Party Tools: Integrate with external tools and platforms that provide RESTful APIs.

Extended Metadata Management: Enhance metadata coverage by incorporating services beyond the default connectors.

​Best Practices

Schema Validation: Ensure the OpenAPI JSON schema is valid and accessible.

Authentication Management: Securely store and manage authentication tokens required for API access.

Regular Updates: Periodically update the OpenAPI JSON schema URL if the API definitions change.

If you have a request for a new connector, don’t hesitate to reach out in Slack or

open a feature request in our GitHub repo.Was this page helpful?YesNoSuggest editsRaise issueConnectors | OpenMetadata Docs for Seamless Data IntegrationPreviousREST API Connector | OpenMetadata Integration DocumentationNext⌘I
