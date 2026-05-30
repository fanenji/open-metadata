---
type: concept
title: Owner Propagation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, governance, ownership, hierarchy, propagation]
related: [data-asset-ownership, teams-and-users, team-types]
sources: ["how-to-assign-or-change-data-ownership---openmetad-20260514.md"]
---

# Owner Propagation

**Owner Propagation** is a mechanism in OpenMetadata that automatically assigns ownership to child data assets based on the ownership of their parent assets. It follows a strict top-down hierarchy: **Database → Database Schema → Table**.

## How It Works

1. If a **Database** has an owner, that owner is auto-propagated as the owner of all **Database Schemas** and **Tables** under it (unless those child assets already have an explicit owner).
2. If a **Database Schema** has an owner, that owner is auto-propagated as the owner of all **Tables** under it (unless those tables already have an explicit owner).
3. Propagation **does not override** existing owners. It only fills in ownership for unowned child assets.
4. If an owner is deleted from a child asset (e.g., a Table), and a parent asset (e.g., the Database Schema or Database) has an owner, the parent's owner is **re-applied** to the child.

## Example

- Database `SalesDB` is owned by Team `Data-Engineering`.
- Database Schema `SalesDB.Public` has no explicit owner → auto-assigned to `Data-Engineering`.
- Table `SalesDB.Public.Orders` has no explicit owner → auto-assigned to `Data-Engineering`.
- If a user manually assigns Table `SalesDB.Public.Orders` to User `Alice`, propagation stops for that table.
- If User `Alice` is later removed as owner of the table, propagation re-applies `Data-Engineering`.

## Benefits

- Reduces manual effort when onboarding new assets.
- Ensures consistent ownership across the data hierarchy.
- Provides a safety net: if a child owner is removed, the parent owner is automatically restored.

## Limitations

- Only applies to the Database → Schema → Table hierarchy. It is unclear whether propagation extends to other asset types (e.g., Dashboards, Pipelines).
- Does not override explicit owners — manual assignments are preserved.
