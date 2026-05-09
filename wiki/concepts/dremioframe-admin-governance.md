---
type: concept
title: DremioFrame Administration & Governance
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, governance, administration, security, python]
related: [dremioframe, data-masking-techniques, data-domain-governance, dremioframe-orchestration]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame Administration & Governance

DremioFrame Administration & Governance provides programmatic management of Dremio resources and governance policies within the [[dremioframe|DremioFrame]] library. It covers catalog management, reflections, UDFs, security, and governance features.

## Key Features

- **Catalog Management**: List, create, and manage catalog entries
- **Reflections Management**: Create and manage Dremio reflections for query acceleration
- **User Defined Functions (UDFs)**: Create and manage UDFs (relevant for [[dremio-geospatial-limitations]] and geospatial UDFs)
- **Security Best Practices**: Security configuration guidance
- **Security Patterns**: Common security patterns for Dremio
- **Governance: Masking & Row Access**: Configure data masking and row-level access policies (see [[data-masking-techniques]])
- **Governance: Tags**: Apply and manage tags for data classification
- **Governance: Lineage**: Track and manage data lineage
- **Governance: Privileges**: Manage user and role privileges
- **Space & Folder Management**: Organize data into spaces and folders
- **Batch Operations**: Perform administrative operations in batch
- **Lineage Tracking**: Detailed lineage tracking capabilities

## Related

- [[dremioframe]] — The parent library
- [[data-masking-techniques]] — Masking techniques configurable via DremioFrame
- [[data-domain-governance]] — Domain governance patterns
- [[dremioframe-orchestration]] — Orchestration integration for governance tasks