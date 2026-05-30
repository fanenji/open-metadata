---
type: concept
title: Mutually Exclusive Glossary Terms
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, data-governance, classification, mutually-exclusive]
related: [glossary-terms, classification-tags, tag-based-access-control]
sources: ["what-is-a-glossary-term-official-documentation---o-20260514.md"]
---
# Mutually Exclusive Glossary Terms

The **Mutually Exclusive** configuration in OpenMetadata prevents assigning multiple terms from the same glossary or glossary term to a single data asset. This is critical for compliance use cases where only one classification from a set is valid for a given asset.

## Use Case

For example, an asset can either be 'PII-Sensitive' or 'PII-NonSensitive' — it cannot be both. By enabling the Mutually Exclusive configuration on a glossary or glossary term, users are prevented from assigning multiple child terms from that glossary/term to the same data asset.

## Configuration

Mutually Exclusive can be enabled at two levels:

- **Glossary level** — When enabled, no two terms from the same glossary can be assigned to the same asset.
- **Glossary Term level** — When enabled on a parent term, no two child terms of that parent can be assigned to the same asset.

## Behavior

- When Mutually Exclusive is enabled, the UI will prevent selecting multiple terms from the same mutually exclusive group for a single asset.
- This configuration is set during glossary or term creation and cannot be changed later (or requires careful consideration).

## Relationship to Tag-Based Access Control

The Mutually Exclusive configuration interacts with [[tag-based-access-control]] because tags propagated from mutually exclusive terms carry the same exclusivity constraint. For example, if 'PII-Sensitive' and 'PII-NonSensitive' are mutually exclusive, an asset tagged with 'PII-Sensitive' cannot also be tagged with 'PII-NonSensitive', which affects how ABAC policies evaluate tag-based conditions.

## Related Pages

- [[glossary-terms]] — Core entity that supports mutually exclusive configuration.
- [[classification-tags]] — Tags that propagate from glossary terms.
- [[tag-based-access-control]] — How tags are used in ABAC policy evaluation.