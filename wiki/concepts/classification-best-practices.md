---
type: concept
title: Classification Best Practices
created: 2026-05-14
updated: 2026-05-14
tags: [classification, best-practices, data-governance, openmetadata]
related: [classification-tags, glossary-terms, tiers, tag-based-access-control, tag-to-glossary-attachment, tag-rename-vs-delete, tag-display-name-improvement, hybrid-rbac-abac-model, spel-conditions]
sources: ["best-practices-for-classification-official-documen-20260514.md"]
---
# Classification Best Practices

This page consolidates the six best practices for using the [[classification-tags|Classification]] system in [[OpenMetadata]] effectively. These practices are derived from the official documentation and are designed to help organizations scale their data governance efforts.

## 1. Add Classification Tags to Glossary Terms

Classification tags can be attached to [[glossary-terms|Glossary Terms]] to define both the semantic meaning and the type of data in a single step. Instead of manually adding classification tags to each data asset, a glossary term can be added to define the meaning of the data, and classification tags like `PII.Sensitive` can be attached to the term. When the glossary term is applied to a data asset, the associated classification tags are automatically applied.

This pattern enables organizations to scale governance: data producers create tables and build data models, while team members who understand regulatory compliance requirements can define glossary terms with attached classification tags. Those who understand both the data and the regulatory requirements can help scale by adding glossary terms along with the classification tags.

See [[tag-to-glossary-attachment]] for detailed documentation of this pattern.

## 2. Make Use of Tier Classification

[[tiers|Tier classification]] helps define the importance of data to an organization. By focusing on Tier 1 data, organizations can create the highest impact. Identifying Tier 5 data helps declutter the existing data estate. See the [[tiers]] page for detailed guidance on the five-tier system.

## 3. Use Classifications to Simplify Policies

Along with ownership and team membership, tags are a powerful way to group data assets. A single policy can be created at the Resource level instead of managing multiple policies for various resources. Resources can be grouped using classification tags like `Sensitive`, `Restrictive`, `External`, `Raw`, `Public`, `Internal`, etc. Policies can then be created based on tags to simplify data governance.

For example, instead of creating separate policies for each table containing sensitive data, the `Sensitive` tag can be attached to all relevant data assets, and a single policy can be created to match based on the `Sensitive` tag using the `matchAnyTag()` [[spel-conditions|SpEL condition]]. This approach leverages the [[hybrid-rbac-abac-model]] and is documented in detail on the [[tag-based-access-control]] page.

## 4. Use Display Name to Improve Names

When classification tags are inherited from source systems, the names may not communicate the concept well. For example, `dep-prod` instead of `Product Department`. Users are more likely to search using common terms like `Product` or `Department`, so improving display names helps in better discovery.

In cases where abbreviations or acronyms are used, a better display name helps in data discovery. For example, `c_id` can be changed to `Customer ID`, and `CAC` can be changed to `Customer Acquisition Cost`.

See [[tag-display-name-improvement]] for detailed guidance.

## 5. Don't Delete Classification Tags; Rename Them

When classification tags have typos, users tend to delete the term. All the effort spent in tagging data assets is lost when terms are deleted. OpenMetadata supports renaming classification tags. Simply rename them instead of deleting.

See [[tag-rename-vs-delete]] for detailed guidance.

## 6. Group Similar Concepts Together

When adding terms, building a semantic relationship helps users understand data through concepts. Grouping related terms helps in understanding the various terms and their overall relationship. This practice improves the conceptual coherence of the classification system.