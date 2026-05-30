---
type: source
title: "Source: how-to-add-description-using-markdown---openmetada-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-add-description-using-markdown---openmetada-20260514.md"]
tags: []
related: []
---

# Source: how-to-add-description-using-markdown---openmetada-20260514.md

# Analysis: How to Add Description using Markdown - OpenMetadata Documentation

## Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| OpenMetadata | Platform | Central (context) | Yes |
| Data Assets | Concept | Central (target of descriptions) | Yes (implied via multiple pages) |
| Glossary Terms | Feature | Peripheral (mentioned for semantic meaning) | Yes |
| Classification Tags | Feature | Peripheral (mentioned for data classification) | Yes |
| Tiers | Feature | Peripheral (mentioned for business importance) | Yes |
| Search & Explore | Feature | Peripheral (descriptions indexed for search) | Yes (via [[reindexing-search]]) |

## Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|------------|----------------|----------|
| **Markdown Description** | Rich-text documentation for data assets using Markdown formatting | Core mechanism for adding human-readable context to metadata; descriptions are searchable | No (new concept) |
| **Description Editor** | UI tool with pencil icon for adding/editing descriptions, supporting Markdown toolbar | Primary user interface for documentation | No |
| **Legacy Markdown Deprecation** | Old Markdown syntax no longer supported; toolbar-based formatting required | Breaking change affecting user workflows | No |
| **Nested Column Documentation** | Ability to document individual columns within a table, including nested structures | Enables granular documentation | No |

## Main Arguments & Findings

- **Core claim**: Descriptions are the primary way to document data assets for consumer understanding.
- **Evidence**: Descriptions are indexed by search; they support Markdown formatting; they can be applied to nested columns.
- **Strength**: Moderate — this is procedural documentation, not empirical research. The claims are straightforward feature descriptions.

## Connections to Existing Wiki

- **Strengthens**: [[data-collaboration]] (descriptions as collaboration foundation), [[classification-tags]] (tagging columns), [[tiers]] (setting business importance), [[glossary-tags]] (semantic meaning via glossary terms)
- **Extends**: [[openmetadata-features]] (adds description editing as a specific user workflow)
- **Related but not directly linked**: [[how-to-request-for-classification-tags]] (parallel request workflow for descriptions), [[data-steward-role]] (stewards manage descriptions)

## Contradictions & Tensions

- **Internal tension**: The page mentions "Request for description" and "Start a conversation around the description" as alternative workflows but does not detail them — these are deferred to other pages.
- **No contradictions** with existing wiki content found.

## Recommendations

### Pages to Create
1. **[[markdown-description-editor]]** — Dedicated page covering the description editor UI, Markdown support details, legacy syntax deprecation, and nested column documentation.
2. **[[how-to-request-for-description]]** — Procedural guide for request
