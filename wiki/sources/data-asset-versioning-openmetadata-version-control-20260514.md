---
type: source
title: "Data Asset Versioning Openmetadata Version Control 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "Data Asset Versioning | OpenMetadata Version Control Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, versioning, data-assets, metadata-governance]
related: [data-asset-versioning, crowd-sourced-metadata, openmetadata-collaboration, audit-logs, change-events-system, data-asset-ownership, classification-tags, glossary-terms]
sources: ["data-asset-versioning-openmetadata-version-control-20260514.md"]
---

# Data Asset Versioning | OpenMetadata Version Control Guide

**Source:** https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/versions

This official OpenMetadata documentation page describes the versioning system for all data assets. It explains the `major.minor` version format (starting at 0.1), the rules for backward-compatible (minor) and backward-incompatible (major) changes, the Version History UI, and the benefits for debugging, reversion, and collaborative governance through crowd-sourced metadata.

## Key Points

- All data assets have a version number in `major.minor` format, starting at `0.1`.
- Backward-compatible changes (description, tags, ownership) increment the minor version by `+0.1`.
- Backward-incompatible changes (e.g., column deletion) increment the major version by `+1.0`.
- Version history is accessible via the Versions icon on any data asset.
- Data owners and admins can review and revert changes.
- Versioning supports a crowd-sourced metadata model where admins delegate editing to more users.

## Connections

- [[data-asset-versioning]] — Dedicated concept page for the versioning system.
- [[crowd-sourced-metadata]] — Collaborative governance model enabled by versioning.
- [[openmetadata-collaboration]] — Broader collaboration features; versioning is a foundation.
- [[audit-logs]] — Complementary mechanism: audit logs track *who* did *what*; versioning tracks *what changed*.
- [[change-events-system]] — Related: change events capture real-time notifications; versioning provides persistent history.
- [[data-asset-ownership]] — Ownership changes trigger minor version increments.
- [[classification-tags]] — Tag changes trigger minor version increments.
- [[glossary-terms]] — Glossary term changes trigger minor version increments.