---
type: concept
title: Glossary Hierarchy
created: 2026-05-14
updated: 2026-05-14
tags: [glossary, hierarchy, data-governance, classification]
related: [glossary-terms, glossary-best-practices, classification-tags, tag-based-access-control]
sources: ["best-practices-for-glossary-official-documentation-20260514.md"]
---
# Glossary Hierarchy

A hierarchical (parent-child) structure for [[glossary-terms]] provides context that a flat list cannot. This additional context aids in classification and policy enforcement.

## Three-Level Limit

The official best practice recommends limiting glossary hierarchies to **three levels**. Deeper hierarchies become difficult to manage and navigate.

## Example: Phone Number

A flat term "Phone Number" lacks context about data sensitivity. A hierarchical structure clarifies this:

- **Level 1:** Contact Info
  - **Level 2:** Phone Number
    - **Level 3:** User Phone Number (PII-Sensitive)
    - **Level 3:** Business Phone Number (Not PII-Sensitive)

This structure allows policy enforcement to distinguish between sensitive and non-sensitive data based on the glossary term's position in the hierarchy.

## Benefits

- **Context:** Provides meaning beyond a single term name.
- **Policy Enforcement:** Enables granular access control based on hierarchical position.
- **Discovery:** Users can navigate from broad categories to specific terms.
- **Scalability:** Groups similar concepts under parent terms for easier management.

## Relationship to Tags

Hierarchical glossary terms can have [[classification-tags]] attached at any level. When a term is applied to a data asset, its attached tags are auto-assigned. This allows combining semantic hierarchy with data type definitions in a single step.