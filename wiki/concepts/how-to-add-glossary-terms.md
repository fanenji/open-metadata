---
type: concept
title: How to Add Glossary Terms
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, tags, how-to, procedure]
related: [glossary-tags, glossary-terms, classification-tags, how-to-add-tags, tag-inheritance-for-masking]
sources: ["how-to-add-glossary-terms-official-documentation---20260514.md"]
---

# How to Add Glossary Terms

This page documents the procedure for applying Glossary Terms to data assets in OpenMetadata v1.12.x.

## Prerequisites

- A data asset (Table, Topic, Dashboard, etc.) must exist in OpenMetadata.
- The Glossary Term must already be defined in the Glossary.

## Procedure

1. **Navigate to the data asset:** From the Explore page, select a data asset.
2. **Open the Glossary Term editor:** Click on the edit icon or the **+ Add** button for Glossary Term on the data asset page.
3. **Search and select the term:** Search for the relevant Glossary Term by typing or scroll to select from the options provided.
4. **Save:** Click on the checkmark to save the changes.

## Viewing Applied Terms

All associated glossary terms are visible in the right panel of the data asset page.

## Tag Propagation

If [[classification-tags|Tags]] are associated with a Glossary Term, applying that term to a data asset will **automatically apply** the associated tags to that asset. For example, if the glossary term 'Account' has a `PII.Sensitive` tag, adding 'Account' to a data asset will also add `PII.Sensitive` to that asset.

This is an alternative path to achieving the same result as manually adding tags via the [[how-to-add-tags]] workflow.

## Related Procedures

- [[how-to-add-tags]] — Manual tag addition workflow
- [[how-to-request-for-tags]] — Collaborative tag request workflow
- [[how-to-assign-or-change-data-ownership]] — Assigning ownership to data assets