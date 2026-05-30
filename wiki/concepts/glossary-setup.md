---
type: concept
title: Glossary Setup
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, governance, setup]
related: [glossary-terms, glossary-mutually-exclusive, glossary-owner-reviewer-inheritance, how-to-add-glossary-terms, classification-tags, data-asset-ownership]
sources: ["how-to-setup-a-glossary-official-documentation---o-20260514.md"]
---
# Glossary Setup

Glossary Setup is the process of creating a glossary in OpenMetadata to organize business terminology. A glossary serves as a container for [[glossary-terms]] and is the foundational step for business metadata governance.

## Manual Creation Procedure

To create a glossary manually:

1. Navigate to **Govern > Glossary**.
2. Click **+ Add** to add a new glossary.
3. Configure the glossary with the following fields:
   - **Name*** — Required. The unique identifier for the glossary.
   - **Display Name** — Optional. A human-readable name.
   - **Description*** — Required. Describes the context or domain of the glossary.
   - **Tags** — Optional. [[classification-tags]] can be added to the glossary.
   - **Mutually Exclusive** — Optional flag. See [[glossary-mutually-exclusive]].
   - **Owner** — Optional. A Team or User can be the Owner. See [[data-asset-ownership]].
   - **Reviewers** — Optional. Multiple users can be added as reviewers.

## Owner and Reviewers

- **Owner:** Either a Team or a User can be assigned as the glossary Owner. Click the Owner field to select.
- **Reviewers:** Multiple users can be added by clicking the pencil icon. If Reviewer details exist for a glossary, they are pre-populated when adding a new term manually.

## Inheritance During Bulk Import

If Owner and Reviewers are set at the glossary level, they are automatically inherited by all glossary terms when bulk uploading via CSV. These details can be changed later on individual terms. See [[glossary-owner-reviewer-inheritance]].

## Related Concepts

- [[glossary-terms]] — Individual terms within a glossary.
- [[glossary-mutually-exclusive]] — The Mutually Exclusive flag prevents assigning multiple terms from the same glossary to one data asset.
- [[how-to-add-glossary-terms]] — Procedure for adding terms to a glossary.
- [[classification-tags]] — Tags that can be added to a glossary.
- [[data-asset-ownership]] — Ownership assignment for data assets.