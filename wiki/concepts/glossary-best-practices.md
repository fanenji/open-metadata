---
type: concept
title: Glossary Best Practices
created: 2026-05-14
updated: 2026-05-14
tags: [glossary, best-practices, data-governance, classification]
related: [glossary-terms, classification-tags, tiers, tag-based-access-control, glossary-hierarchy, tag-based-policy-design, glossary-import-export]
sources: ["best-practices-for-glossary-official-documentation-20260514.md"]
---
# Glossary Best Practices

This page consolidates the eight best practices for glossary management in OpenMetadata, as documented in the official guide. These practices are designed to help organizations scale their data governance efforts by combining semantic meaning with data type definitions.

## The Eight Practices

### 1. Use Hierarchical Relationships
Instead of a flat list of glossary terms, use a parent-child (hierarchical) structure. This provides context for classification and policy enforcement. Limit the hierarchy to **three levels** for manageability. For example, a flat term "Phone Number" lacks context, but a hierarchy like `Contact Info → Phone Number → User Phone Number` distinguishes PII-sensitive data from non-sensitive data (e.g., Business Phone Number). See [[glossary-hierarchy]] for detailed patterns.

### 2. Add Classification Tags to Glossary Terms
Attach [[classification-tags]] (e.g., `PII.Sensitive`) to glossary terms. This defines both the semantic meaning and the type of data in a single step. When the glossary term is applied to a data asset, the associated tags are automatically assigned, enabling scalable governance. This pattern empowers users who understand both data and regulatory requirements to define terms that auto-classify assets.

### 3. Make Use of Tier Classification
Use [[tiers]] (Tier 1–5) to define the importance of data to the organization. Focus on Tier 1 data for highest impact, and identify Tier 5 data to declutter. See the [[tiers]] page for details.

### 4. Use Classifications to Simplify Policies
Group data assets using classification tags (e.g., `sensitive`, `restrictive`, `public`, `internal`) and create a single policy at the tag level instead of managing multiple per-resource policies. For example, attach a `Sensitive` tag to all relevant tables and create one policy matching that tag. See [[tag-based-policy-design]] for detailed guidance.

### 5. Use Display Name to Improve Names
When glossary terms are inherited from source systems, rename them with user-friendly display names. For example, change `dep-prod` to `Product Department` and `c_id` to `Customer ID`. This improves searchability and data discovery.

### 6. Use Glossary Import/Export
For bulk edits (updating descriptions, ownership, reviewer, status), export the glossary to CSV, make edits, and import it back. See [[glossary-import-export]] for details.

### 7. Don't Delete Glossary Terms; Rename Them
Deleting a glossary term removes all tagging effort on data assets. Instead, rename the term to fix typos or update names. OpenMetadata supports renaming glossary terms natively.

### 8. Group Similar Concepts Together
Build semantic relationships between related terms to help users understand data through concepts. Grouping related terms clarifies their overall relationship.

## Key Principles

- **Scalability:** Combine semantic meaning (glossary terms) with data type definitions (classification tags) to automate governance at scale.
- **Preservation:** Prefer renaming over deleting to protect existing tagging investments.
- **Searchability:** Optimize display names for user search patterns.
- **Policy Simplification:** Use tag-level policies to reduce administrative overhead.