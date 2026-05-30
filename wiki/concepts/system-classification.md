---
type: concept
title: System Classification
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, system-tags, openmetadata]
related: [classification-tags, tiers, tag-based-access-control]
sources: ["how-to-classify-data-assets-official-documentation-20260514.md"]
---
# System Classification

System Classification refers to the pre-built classification tags provided by OpenMetadata out of the box. These tags offer a standard governance vocabulary that reduces setup effort and ensures consistency across organizations using the platform.

## Purpose

- **Reduce setup effort**: Organizations don't need to create common governance tags from scratch.
- **Standard vocabulary**: Provides consistent terminology for common data governance concepts.
- **Foundation for policies**: System tags can be immediately referenced in [[tag-based-access-control|Tag-Based Access Control]] policies.

## Relationship to Classification Tags

System Classification is a subset of [[classification-tags|Classification Tags]]. They appear alongside user-defined tags in the tagging interface and on the Classification page (Govern > Classification). They function identically to user-defined tags for access control and discovery purposes.

## Open Questions

- What is the complete catalog of System Classification tags?
- What categories do they cover (e.g., PII, retention, confidentiality)?
- Can System Classification tags be modified or deleted, or are they immutable?
- How do System Classification tags relate to the PII auto-classification workflow?