---
type: source
title: How to Setup a Glossary | Official Documentation - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, governance, documentation]
related: [glossary-setup, glossary-terms, glossary-mutually-exclusive, glossary-owner-reviewer-inheritance, how-to-add-glossary-terms, classification-tags, data-asset-ownership]
sources: ["how-to-setup-a-glossary-official-documentation---o-20260514.md"]
---
# How to Setup a Glossary | Official Documentation - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for manually creating a glossary. It covers the step-by-step procedure for navigating to Govern > Glossary, clicking + Add, and configuring the glossary with Name, Description, Display Name, Tags, the Mutually Exclusive flag, Owner, and Reviewers. It also documents the inheritance behavior where glossary-level Owner and Reviewers are automatically applied to all terms during CSV bulk import.

## Key Points

- **Manual Creation:** The glossary is created via Govern > Glossary > + Add.
- **Required Fields:** Name and Description are mandatory.
- **Mutually Exclusive Flag:** When enabled, only one term from that glossary can be assigned to a single data asset (e.g., PII-Sensitive vs. PII-NonSensitive).
- **Owner and Reviewers:** Owner can be a Team or User; multiple Reviewers can be added.
- **Inheritance During Bulk Import:** If Owner and Reviewers are set at the glossary level, they are inherited by all terms when bulk uploading via CSV.
- **Manual Term Creation:** When adding a term manually, the glossary-level Reviewer details are pre-populated.

## Related Wiki Pages

- [[glossary-setup]] — Detailed concept page for the glossary creation process.
- [[glossary-terms]] — Individual terms within a glossary.
- [[glossary-mutually-exclusive]] — The Mutually Exclusive flag concept and use cases.
- [[glossary-owner-reviewer-inheritance]] — Inheritance behavior during CSV bulk import.
- [[how-to-add-glossary-terms]] — Procedure for adding terms to a glossary.
- [[classification-tags]] — Tags that can be added to a glossary.
- [[data-asset-ownership]] — Ownership assignment for data assets.