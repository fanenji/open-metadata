---
type: entity
title: Metadata Versioning
created: 2026-05-14
updated: 2026-05-14
tags: [metadata, versioning, data-discovery, openmetadata]
related: [data-discovery, data-lineage, advanced-search]
sources: ["how-to-discover-assets-of-interest---openmetadata--20260514.md"]
---

# Metadata Versioning

Metadata Versioning in OpenMetadata tracks the evolution of data assets over time. By viewing version history alongside [[data-lineage]], users can discover how assets have changed, who made changes, and what transformations have been applied.

## Role in Data Discovery

Metadata Versioning is one of the five core discovery strategies documented in the [[data-discovery]] guide. It enables users to:

- Track changes to asset schemas, descriptions, tags, and ownership.
- Understand the historical context of a data asset.
- Identify when and how an asset was modified.

## Relationship to Other Features

- **[[data-lineage]]**: Lineage shows the flow of data between assets; versioning shows how individual assets have changed over time.
- **[[advanced-search]]**: Versioning metadata may be searchable via advanced search parameters.

## Open Questions

- Is version history accessible through the UI for all asset types?
- Can users compare specific versions side-by-side?
- Are versioning events captured in the [[change-events-system]]?