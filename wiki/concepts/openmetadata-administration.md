---
type: concept
title: OpenMetadata Administration
created: 2026-05-14
updated: 2026-05-14
tags: [administration, roles, policies, teams, users, alerts, custom-properties, data-insights, audit-logs, permission-debugger, persona, reindexing, cli-ingestion]
related: [openmetadata, roles-and-policies, teams-and-users, data-observability-alerts, custom-properties, openmetadata-insights, audit-logs, permission-debugger, persona-and-landing-page-customization, reindexing-search, cli-ingestion-with-basic-auth, ingestion-framework, elasticsearch-7x]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md"]
---
# OpenMetadata Administration

OpenMetadata Administration encompasses the full set of capabilities available to users with the **Administrator** role. Administrators have unrestricted access to all data assets and can perform all create, edit, and delete operations across the platform.

## Multi-Administrator Model

An organization can have **multiple Administrators**, each managing specific teams and departments independently. This decentralized model allows large organizations to distribute administrative responsibilities without compromising security or governance.

## Scope of Administration

The administrative functions in OpenMetadata cover:

### Access Control
- **[[roles-and-policies|Roles and Policies]]** — Define and enforce access controls across the organization. An advanced guide is available for complex access management scenarios.

### Organizational Structure
- **[[teams-and-users|Teams and Users]]** — Create hierarchical teams, add individual users, and streamline onboarding. Teams form the backbone of collaboration and access management.

### Platform Services
- **Services and Notifications** — Configure platform services and set up notification rules.
- **[[data-observability-alerts|Data Observability Alerts]]** — Fine-grained alerts for critical data operations such as schema changes, pipeline failures, and data quality issues. Alerts can be sent to multiple destinations.

### Metadata Extensibility
- **[[custom-properties|Custom Properties]]** — Extend data models with additional metadata fields tailored to organizational needs.

### Monitoring and Analytics
- **[[openmetadata-insights|Data Insights]]** — Monitor data health and usage analytics across the data estate.

### Maintenance and Diagnostics
- **[[reindexing-search|Reindexing Search]]** — Rebuild the search index for Elasticsearch/OpenSearch to ensure search functionality works correctly.
- **[[permission-debugger|Permission Debugger]]** — Diagnose and troubleshoot access permission issues.
- **[[audit-logs|Audit Logs]]** — Review records of platform activities for compliance and security.

### User Experience
- **[[persona-and-landing-page-customization|Persona and Landing Page Customization]]** — Tailor the user interface and experience based on user roles or preferences.

### Ingestion Alternatives
- **[[cli-ingestion-with-basic-auth|CLI Ingestion with Basic Auth]]** — Run metadata ingestion from the command line using basic authentication, useful for automation or environments without OAuth.

## Getting Started

The administration journey typically follows three steps:
1. **Ingest Data** from multiple sources using the [[ingestion-framework]].
2. **Create Teams** to establish a hierarchical organizational structure.
3. **Invite Users** to start collaborating on data.

Once basic setup is complete, administrators can proceed to advanced [[roles-and-policies|Roles and Policies]] configuration for fine-grained access management.