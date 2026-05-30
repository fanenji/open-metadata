---
type: source
title: "Source: powerbi-connector-openmetadata-integration-documen-20260514-2.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["powerbi-connector-openmetadata-integration-documen-20260514-2.md"]
tags: []
related: []
---

# Source: powerbi-connector-openmetadata-integration-documen-20260514-2.md

## Analysis of Source Document: PowerBI Connector | OpenMetadata Integration Documentation

### Key Entities

- **PowerBI (Microsoft Power BI)** — Type: Product/Platform. Role: Central. The source system from which metadata is ingested. Already exists in the wiki as [[powerbi-connector]].
- **OpenMetadata** — Type: Platform. Role: Central. The target system receiving the metadata. Already exists in the wiki as [[openmetadata]].
- **Azure AD (Azure Active Directory)** — Type: Platform. Role: Peripheral. Required for authentication and app registration. Not explicitly in the wiki index but implied by existing connector pages.
- **Service Principal** — Type: Authentication Method. Role: Central. The only supported authentication type (OAuth 2.0 Service Principal). Not explicitly in the wiki index.
- **PowerBI Admin APIs** — Type: API Set. Role: Central. Used when "Use Admin APIs" is enabled; fetches metadata from all workspaces. Not in the wiki index.
- **PowerBI Non-Admin APIs** — Type: API Set. Role: Central. Used when "Use Admin APIs" is disabled; limited to assigned workspaces and push datasets only. Not in the wiki index.
- **PowerBI Scan Result API** — Type: API. Role: Peripheral. Used by Admin APIs for lineage data; has no limitations. Not in the wiki index.
- **PowerBI Get Dataset Tables API** — Type: API. Role: Peripheral. Used by Non-Admin APIs for lineage; only works for push datasets. Not in the wiki index.
- **Hybrid Ingestion Runner** — Type: Component. Role: Peripheral. Mentioned in the context of secret management for sensitive credential fields. Not in the wiki index.

### Key Concepts

- **Admin vs. Non-Admin API Mode** — Definition: A toggle determining whether PowerBI Admin APIs (access all workspaces, full lineage) or Non-Admin APIs (limited to assigned workspaces, lineage only for push datasets) are used. Why it matters: Directly impacts the scope of metadata ingestion and lineage completeness. Likely already exists in the wiki as part of [[powerbi-connector]].
- **Push Dataset** — Definition: A dataset that is pushed into PowerBI programmatically rather than connected to a live data source. Why it matters: Only push datasets support lineage when using Non-Admin APIs. Not in the wiki index.
- **Service Principal Authentication** — Definition: Azure AD application authentication using Client ID, Client Secret, and Tenant ID. Why it matters: The only supported authentication type for the PowerBI connector. Not in the wiki index.
- **Soft Deletion (Mark Deleted Dashboards)** — Definition: A toggle that flags dashboards as deleted if they are no longer present in the source system. Why it matters: Preserves lineage and historical metadata. Already exists in the wiki as [[soft-deletion]].
- **Dashboard Filter Pattern** — Definition: Regex-based inclusion/exclusion rules for dashboards during ingestion. Why it matters: Controls ingestion scope. Already exists in the wiki as [[filter-patterns]].
- **Project Filter Pattern** — Definiti
