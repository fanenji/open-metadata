---
type: concept
title: Metadata Versioning
created: 2026-05-14
updated: 2026-05-14
tags: [metadata, versioning, data-governance, openmetadata]
related: [data-discovery, change-events-system, data-lineage, unified-metadata-graph]
sources: ["data-discovery-openmetadata-how-to-guide---openmet-20260514.md"]
---

# Metadata Versioning

Metadata versioning is the capability to track changes to metadata over time. In OpenMetadata, versioning provides historical context for data assets, enabling users to understand how metadata has evolved and who made changes.

## Purpose

- **Historical Context** — View previous versions of metadata to understand how descriptions, tags, ownership, or schema have changed
- **Audit Trail** — Track who made changes and when, supporting compliance and governance requirements
- **Data Evolution** — Complement [[data-lineage]] to provide a complete picture of how data and its metadata have evolved over time

## Relationship to the Change Events System

Metadata versioning is closely related to the [[change-events-system]]. The change events system captures metadata changes in real-time (via ContainerResponseFilter → DB + Elasticsearch), and versioning likely leverages this event stream to create version snapshots. However, the exact relationship — whether every change event creates a new version, or versions are created on specific triggers — is not documented in the source material.

## Role in Data Discovery

In the context of [[data-discovery]], metadata versioning helps users evaluate whether a data asset is suitable for their needs by showing how it has changed over time. A table whose schema has changed frequently, for example, may be less reliable than one with stable metadata.

## Open Questions

- What is the exact relationship between metadata versioning and the [[change-events-system]]? Are versions created from the event stream, or is there a separate versioning mechanism?
- How far back does version history extend? Is there a retention policy?
- Can users compare versions side-by-side in the UI?
- Is versioning supported for all asset types, or only specific ones?

## See Also

- [[data-discovery]] — How versioning supports data discovery
- [[change-events-system]] — The event capture mechanism that may underpin versioning
- [[data-lineage]] — Complementary feature for understanding data evolution
- [[audit-logs]] — Related feature for compliance and security tracking