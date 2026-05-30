---
type: concept
title: Crowd-Sourced Metadata
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, metadata-governance, collaboration]
related: [data-asset-versioning, openmetadata-collaboration, roles-and-policies, data-asset-ownership]
sources: ["data-asset-versioning-openmetadata-version-control-20260514.md"]
---

# Crowd-Sourced Metadata

Crowd-sourced metadata is a collaborative governance model in OpenMetadata where administrators delegate the ability to edit certain metadata fields to a broader set of users across the organization. This makes metadata management a collective responsibility rather than a task limited to a small group of data stewards or owners.

## How It Works

- Admins grant access to more users to change fields such as descriptions, tags, and ownership.
- The [[data-asset-versioning]] system provides the audit trail and reversion capability that makes this delegation safe: any change can be reviewed and reverted if necessary.
- This model encourages broader collaboration between data consumers and producers.

## Relationship to Other Concepts

- [[data-asset-versioning]] — Versioning is the foundational mechanism that enables crowd-sourced metadata by providing change tracking and reversion.
- [[openmetadata-collaboration]] — Crowd-sourced metadata is a specific collaborative practice within the broader collaboration feature set.
- [[roles-and-policies]] — Access control policies determine which users can edit which fields, implementing the delegation model.
- [[data-asset-ownership]] — Owners can review and revert changes made by other users.

## Notes

- The official documentation introduces this concept briefly but does not provide detailed implementation steps or best practices.
- This concept is closely related to the [[tag-request-workflow]] and [[conversations-around-classification]] features, which also enable collaborative metadata management.