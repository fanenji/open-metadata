---
type: concept
title: Metadata Versioning
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, versioning, metadata, audit]
related: [openmetadata, openmetadata-architecture, data-contract-versioning-strategy, data-lakehouse-versioning-strategies]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# Metadata Versioning

Metadata Versioning is a feature of [[OpenMetadata]] where every change to every asset is tracked and versioned. When someone updates a description, adds a tag, changes an owner, or adds a column, OpenMetadata:

1. Creates a new version of the entity.
2. Records what changed, who changed it, and when.
3. Lets you view and diff any two versions.
4. Lets you restore a previous version if needed.

This is invaluable for:
- Auditing who changed what and when.
- Understanding why a dataset looks different from yesterday.
- Rollback when a mistake is made.

This concept is related to [[data-contract-versioning-strategy]] and [[data-lakehouse-versioning-strategies]], which address versioning at the data contract and data lakehouse levels respectively.