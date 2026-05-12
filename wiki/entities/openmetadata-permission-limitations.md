---
type: entity
title: OpenMetadata Permission Limitations
created: 2026-05-10
updated: 2026-05-10
tags: [openmetadata, permission-control, rbac, governance, limitation]
related: [openmetadata, data-catalog-tool-comparison, data-domain-governance]
sources: ["permission-control-open-metadata-openmetadata-disc-20260510.md"]
---
# OpenMetadata Permission Limitations

OpenMetadata (pre-v1.6) has a significant permission limitation: it can restrict *access* to data assets but cannot hide them from the Explore tab UI. This means unauthorized users can see the existence of tables, databases, and other assets they cannot access.

## The Limitation

- **Visibility vs. Access:** Policies can block operations (View, Edit, Delete) on data assets, but assets remain visible in the Explore tab and search results.
- **Tag-Based Policies Ineffective:** Tag-based policies (e.g., denying view of `PII.Sensitive` tagged tables) do not hide assets from the Explore tab.
- **UI Surfaces Affected:** The Explore tab is the primary surface affected. It is unclear whether lineage views, glossary pages, and other UI surfaces are also affected.

## Planned Solution

- **Search-Based RBAC:** Scheduled for OpenMetadata v1.6, this feature would hide assets from search results and the Explore tab based on user roles and permissions.
- **Status:** At the time of the discussion (July 2024), Search-based RBAC was not yet available. Verify current release status.

## Governance Impact

This limitation creates a governance gap for deployments requiring strict data confidentiality. Core requirements affected:

- **Need-to-Know Principle:** Users should not even know about data they are not authorized to see.
- **Compliance:** Regulations like GDPR and HIPAA may require hiding sensitive data from unauthorized personnel.
- **Domain Governance:** Domain-based access control may be undermined if users can see assets from other domains.

## Evaluation Criterion

When evaluating data catalog tools, "Visibility control (hide assets vs. restrict access)" should be a key criterion. Compare with [[datahub]] and [[amundsen]] for their approaches to asset visibility.