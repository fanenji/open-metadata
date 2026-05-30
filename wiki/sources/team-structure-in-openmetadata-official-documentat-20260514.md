---
type: source
title: "Team Structure in OpenMetadata | Official Documentation"
created: 2026-05-14
updated: 2026-05-30
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/team-structure-openmetadata"
venue: "OpenMetadata Documentation v1.12.x"
tags: [openmetadata, teams, hierarchy, governance]
related: [teams-and-users, team-types, team-hierarchy-rules, multi-admin-model, roles-and-policies]
sources: ["team-structure-in-openmetadata-official-documentat-20260514.md"]
---

# Team Structure in OpenMetadata | Official Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/team-structure-openmetadata

This official documentation page defines the hierarchical team structure in OpenMetadata v1.12.x, including the five team types (`Organization`, `BusinessUnit`, `Division`, `Department`, `Group`), their parent-child constraints, data asset ownership rules, and the immutability of the `Group` type. It serves as the definitive reference for how teams are organized and governed within the platform.

Key points:
- `Organization` is the mandatory root team; it cannot have a parent and cannot be deleted.
- `BusinessUnit`, `Division`, `Department`, and `Group` form a typed hierarchy with specific parent and child constraints.
- `Department` and `Group` support multiple parents, enabling matrix-style organizational structures.
- Only teams of type `Group` can own data assets.
- Once created, the `teamType` for `Group` cannot be changed.
- There is no hardcoded depth limit, but leaf nodes (`Group`) cannot have child teams.