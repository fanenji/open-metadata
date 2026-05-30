---
type: source
title: "OpenMetadata Community Meeting Oct 2023: Release 1.2.0"
created: 2026-05-14
updated: 2026-05-14
tags: [community-meeting, release-1.2.0, data-mesh, domains, data-products, glossary-approval, personas, metadata-applications, cost-analysis, knowledge-center]
related: [data-mesh-openmetadata, glossary-approval-workflow, metadata-applications-framework, cost-analysis, knowledge-center, chrome-extension, collate-inc, persona, pluggable-panels, glossary-tags, data-lineage, openmetadata-features, data-insights-application-troubleshooting, unified-metadata-graph]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
authors: ["OpenMetadata"]
year: 2023
url: "https://www.youtube.com/watch?v=Nh2xLAwY2-A"
venue: "YouTube"
---
# OpenMetadata Community Meeting Oct 2023: Release 1.2.0

The OpenMetadata Community Meeting held on October 19, 2023, presented the 1.2.0 release. This source covers the announcement and live demonstrations of major new features including Domains & Data Products, Glossary Approval Workflow, Cost Analysis, Knowledge Center, Personas & Customizable Landing Page, Metadata Applications, Search Indexes, Stored Procedures, and performance improvements.

## Key Highlights

- **Domains & Data Products**: Introduction of data mesh organizational principles with domain boundaries, domain inheritance, domain-only view, and data products as consumable logical groupings of data assets.
- **Glossary Approval Workflow**: Governance mechanism requiring designated reviewers to approve glossary terms before they move from draft to approved state; admins cannot override.
- **Cost Analysis**: SaaS-only feature showing used vs. unused assets by count, size, and storage cost for active data estate management.
- **Knowledge Center**: SaaS-only full-page article system with rich markdown editor, entity references, and quick links for organizational data documentation.
- **Personas & Customizable Landing Page**: User role profiles with pluggable panels enabling tailored UI experiences; multi-persona switching and default persona selection.
- **Metadata Applications**: Pluggable application framework with marketplace for installing, configuring, and scheduling automation apps that run within the OpenMetadata server.
- **Search Indexes & Stored Procedures**: New entity types ingestible from ElasticSearch/OpenSearch and databases; stored procedures appear as edges in lineage graphs with code display.
- **Chrome Extension**: Updated to support all entity types with inline metadata display, activity feed, and task notifications.
- **Community Growth**: 10 new contributors, ~3,000 GitHub stars, 4,000+ Slack members, ~75 PRs merged per week.

## Data Mesh Philosophy

The presenter explicitly states: "data mesh is not an architectural principle, it's an organizational principle." OpenMetadata's implementation focuses on enabling organizational structure (domains, distributed ownership) rather than prescribing infrastructure changes. Key design decisions include the ability to turn off domains/data products entirely for small organizations, domain inheritance to reduce tagging burden, and planned support for data products independent of domains.