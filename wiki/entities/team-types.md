---
type: entity
title: Team Types
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, teams, governance, hierarchy]
related: [teams-and-users, team-hierarchy-rules, multi-admin-model, roles-and-policies]
sources: ["team-structure-in-openmetadata-official-documentat-20260514.md"]
---

# Team Types

Team types in OpenMetadata are classifications that define a team's position in the organizational hierarchy, its allowed parent and child relationships, and whether it can own data assets. OpenMetadata v1.12.x supports five team types: `Organization`, `BusinessUnit`, `Division`, `Department`, and `Group`.

## Available Team Types

### Organization
- **Role:** Root of the entire hierarchy, representing the whole company.
- **Parent:** None (cannot be reparented or deleted).
- **Children:** BusinessUnit, Division, Department, Group, and Users (for teamless users).
- **Data Asset Ownership:** No.

### BusinessUnit
- **Role:** Second-level organizational unit.
- **Parent:** Organization or another BusinessUnit (single parent only).
- **Children:** BusinessUnit, Division, Department, Group.
- **Data Asset Ownership:** No.

### Division
- **Role:** Third-level organizational unit, below BusinessUnit.
- **Parent:** Organization, BusinessUnit, or Division (single parent only).
- **Children:** Division, Department, Group.
- **Data Asset Ownership:** No.

### Department
- **Role:** Fourth-level organizational unit, below Division.
- **Parent:** Organization, BusinessUnit, Division, or Department (**multiple parents allowed**).
- **Children:** Department, Group.
- **Data Asset Ownership:** No.

### Group
- **Role:** Leaf-level team; the fundamental unit for data governance.
- **Parent:** Any team type (**multiple parents allowed**).
- **Children:** Users only (no child teams).
- **Data Asset Ownership:** **Yes** — only Groups can own data assets.
- **Immutability:** Once created as `Group`, the type cannot be changed.

## Key Constraints

- **Group immutability:** The `Group` type is locked after creation. Plan team structures carefully.
- **Ownership restriction:** Data assets can only be owned by `Group` teams. This is a hard governance rule.
- **Multiple parents:** Only `Department` and `Group` support multiple parents, enabling matrix organizations.
- **No depth limit:** There is no hardcoded maximum hierarchy depth, but `Group` nodes are always leaves.

## Open Questions

- Can `BusinessUnit`, `Division`, or `Department` types be changed after creation? The official documentation only confirms immutability for `Group`. The mutability of other types is not explicitly documented.

## See Also

- [[team-hierarchy-rules]] — Complete parent-child matrix and constraints.
- [[teams-and-users]] — How to manage teams and users.
- [[multi-admin-model]] — Decentralized administration using team hierarchy.
- [[roles-and-policies]] — Access control assignment through teams.