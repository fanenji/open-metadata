---
type: concept
title: Data Asset Ownership
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, governance, ownership, teams, users]
related: [owner-propagation, teams-and-users, team-types, data-steward-role, roles-and-policies]
sources: ["how-to-assign-or-change-data-ownership---openmetad-20260514.md"]
---

# Data Asset Ownership

In OpenMetadata, a **data asset owner** is a Team or User responsible for a data asset (e.g., Database, Database Schema, Table). Owners have full operational access to the asset, including the ability to edit descriptions, tags, glossary terms, and other metadata.

## Key Principles

- **Admin-only assignment:** Only Admin users can assign or change data ownership.
- **Team ownership is preferred:** OpenMetadata recommends assigning ownership to a Team rather than an individual User, because team ownership provides broader context and enables collaboration among all team members.
- **Only Groups can own assets:** Only teams of the type 'Groups' are eligible to own data assets.
- **Owner propagation:** Ownership propagates top-down through the Database → Schema → Table hierarchy (see [[owner-propagation]]).

## Assigning Ownership

1. Navigate to the data asset in the UI.
2. Click the edit icon next to the **Owner** field.
3. Select a Team (preferred) or a User as the owner.

## Changing Ownership

If the asset already has an owner, click the edit icon next to the Owner field and select a new Team or User. If no owner is selected and a parent asset (Database or Schema) has an owner, the parent's owner is auto-assigned via propagation.

## Relationship to Authorization

Ownership grants full operational access, which is a key component of the [[hybrid-rbac-abac-model]]. Owners can perform all operations on the asset, including editing descriptions, tags, and glossary terms.
