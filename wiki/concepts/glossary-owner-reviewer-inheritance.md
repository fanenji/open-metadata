---
type: concept
title: Glossary Owner and Reviewer Inheritance
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, governance, inheritance, bulk-import]
related: [glossary-setup, glossary-terms, how-to-add-glossary-terms, data-asset-ownership]
sources: ["how-to-setup-a-glossary-official-documentation---o-20260514.md"]
---
# Glossary Owner and Reviewer Inheritance

When bulk importing glossary terms via CSV, the Owner and Reviewers set at the glossary level are automatically inherited by all imported terms. This simplifies governance at scale by ensuring consistent ownership and review assignment across all terms in a glossary.

## Inheritance Behavior

- **Owner:** The glossary-level Owner (Team or User) is applied to every term created via CSV bulk import.
- **Reviewers:** All glossary-level Reviewers are applied to every term created via CSV bulk import.
- **Manual Term Creation:** When adding a term manually, the glossary-level Reviewer details are pre-populated in the form.
- **Post-Import Changes:** Inherited Owner and Reviewer details can be changed later on individual terms.

## Benefits

- **Consistency:** Ensures all terms in a glossary have the same governance baseline.
- **Efficiency:** Eliminates the need to set Owner and Reviewers for each term individually during bulk import.
- **Scalability:** Makes bulk import practical for large glossaries with hundreds or thousands of terms.

## Related Concepts

- [[glossary-setup]] — How to create a glossary and set Owner and Reviewers.
- [[glossary-terms]] — Individual terms within a glossary.
- [[how-to-add-glossary-terms]] — Procedure for adding terms to a glossary.
- [[data-asset-ownership]] — Ownership assignment for data assets.