---
type: concept
title: Data Asset Versioning
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, versioning, metadata-governance, data-assets]
related: [crowd-sourced-metadata, openmetadata-collaboration, audit-logs, change-events-system, data-asset-ownership, classification-tags, glossary-terms, soft-deletion]
sources: ["data-asset-versioning-openmetadata-version-control-20260514.md"]
---

# Data Asset Versioning

OpenMetadata tracks the evolution of all data assets through a built-in versioning system. Every data asset — tables, topics, dashboards, pipelines, etc. — has a version number in `major.minor` format, starting at `0.1` as the initial version.

## Version Change Rules

- **Minor version change (+0.1):** Triggered by backward-compatible metadata changes. Examples include adding, updating, or removing a description, tags, or ownership.
- **Major version change (+1.0):** Triggered by backward-incompatible structural changes. The primary example is the deletion of a column in a table.

## Version History UI

Users can view the complete version history of any data asset by clicking the **Versions** icon on the asset's detail page. This displays the evolution of metadata over time, showing what changed at each version.

## Benefits

- **Debugging:** Correlate metadata changes to data issues by reviewing recent version history.
- **Reversion:** Data owners and admins can review changes and revert to a previous version if necessary.
- **Collaborative Governance:** Versioning provides the audit trail that enables crowd-sourced metadata editing, where admins delegate metadata field changes to a broader set of users.

## Relationship to Other Concepts

- [[audit-logs]] — Audit logs track *who* performed *what* action; versioning tracks *what changed* in the metadata. They are complementary.
- [[change-events-system]] — Change events capture real-time notifications of metadata changes; versioning provides the persistent, queryable history.
- [[soft-deletion]] — The interaction between versioning and soft-deletion is not fully documented. It is unclear whether soft-deletion triggers a version change or how reversion interacts with soft-deleted assets.
- [[data-asset-ownership]], [[classification-tags]], [[glossary-terms]] — Changes to these fields all trigger minor version increments.

## Open Questions

- Can users revert to any previous version, or only the immediately preceding one?
- Is reversion a UI action, an API call, or both?
- How does versioning interact with [[soft-deletion]] (e.g., does soft-deletion trigger a version change)?
- Are there performance implications for high-churn assets with thousands of versions?