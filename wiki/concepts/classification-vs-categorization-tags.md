---
type: concept
title: Classification vs. Categorization Tags
created: 2026-05-14
updated: 2026-05-14
tags: [classification, tags, data-governance, openmetadata]
related: [classification-tags, mutually-exclusive-tags, system-classification, glossary-terms, tag-based-access-control]
sources: ["overview-of-classification-official-documentation--20260514.md"]
---
# Classification vs. Categorization Tags

OpenMetadata supports two distinct types of tags: **Classification tags** and **Categorization tags**. The key difference lies in mutual exclusivity.

## Classification Tags (Mutually Exclusive)

Classification tags are **mutually exclusive** within a given classification group. A data asset can belong to only one class in a hierarchy. For example:

- Data can be either **Public** or **Private**, but not both.
- Data can be either **Sensitive** or **Non-sensitive**, but not both.
- Data can be either **PII Sensitive** or **PII Non-Sensitive**, but not both.

This mutual exclusivity is enforced by the [[mutually-exclusive-tags]] configuration option on a Classification.

## Categorization Tags (Not Mutually Exclusive)

Categorization tags are **not mutually exclusive**. A data asset can belong to multiple categories simultaneously. For example, the same table can have **Usage**, **Financial**, **Reporting**, and **Compliance** tags applied to it.

## Practical Implications

- **Classification tags** are ideal for governance policies where a data asset must be in exactly one state (e.g., access control based on sensitivity level).
- **Categorization tags** are ideal for discovery and filtering, where multiple descriptive labels add value.

## Relationship to Glossary Terms

[[glossary-terms]] define the *semantics* or *meaning* of data, while Classification tags define the *type* of data. Both can be applied to the same asset for complementary governance.