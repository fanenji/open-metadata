---
type: source
title: "Source: run-the-superset-connector-externally---openmetada-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["run-the-superset-connector-externally---openmetada-20260514.md"]
tags: []
related: []
---

# Source: run-the-superset-connector-externally---openmetada-20260514.md

## Key Entities

- **Superset (Apache Superset)** — Type: Product/Platform. Central entity; the data source being connected to OpenMetadata. Already exists in wiki as [[superset-connector]].
- **OpenMetadata** — Type: Platform. Central entity; the metadata system receiving the ingested data. Already exists in wiki as [[openmetadata]].
- **MySQL** — Type: Product/Database. Peripheral; one of two supported backend databases for Superset connection (when SSO is enabled). Already exists in wiki as [[mysql-8x]].
- **PostgreSQL** — Type: Product/Database. Peripheral; one of two supported backend databases for Superset connection (when SSO is enabled). Already exists in wiki as [[postgresql-connector]].
- **Ingestion Framework** — Type: Tool/System. Peripheral; the mechanism for running connectors externally. Already exists in wiki as [[ingestion-framework]].
- **Metadata CLI** — Type: Tool. Peripheral; the command-line tool used to run the YAML-based ingestion. Already exists in wiki as [[metadata-cli]].
- **JWT Token** — Type: Concept/Auth Mechanism. Peripheral; authentication method for the OpenMetadata server connection. Already exists in wiki as [[personal-access-token]].
- **Airflow** — Type: Platform. Peripheral; referenced as the default orchestrator for UI-based ingestion. Already exists in wiki as [[airflow-storage-requirements]].

## Key Concepts

- **API Connection Mode** — Definition: Default authentication mode using Superset's REST API to fetch metadata. Why it matters: Only supports basic/ldap authentication; SSO-enabled Superset instances cannot use this mode. Likely already exists in wiki (part of [[superset-connector]]).
- **Database Connection Mode** — Definition: Alternative authentication mode that connects directly to Superset's backend database (MySQL or PostgreSQL) to extract metadata. Why it matters: Required when SSO is enabled on Superset; bypasses API authentication limitations. Likely already exists in wiki.
- **Filter Patterns** — Definition: Regex-based inclusion/exclusion rules for dashboards, charts, data models, and projects. Why it matters: Controls ingestion scope and reduces unnecessary metadata extraction. Already exists in wiki as [[filter-patterns]].
- **Override Metadata** — Definition: Toggle controlling whether fetched metadata overwrites existing metadata in OpenMetadata for fields like description, tags, owner, and displayName. Why it matters: Critical for data governance workflows; prevents accidental overwrites. Likely new to wiki.
- **Override Lineage** — Definition: Toggle controlling whether existing lineage is overwritten during ingestion. Why it matters: Prevents lineage corruption during re-ingestion. Likely new to wiki.
- **Store Service Connection** — Definition: Toggle controlling whether sensitive connection information is stored in the database (encrypted via Fernet Key) or used only at runtime. Why it matters: Security consideration; affects credential management and Secrets Manager integration
