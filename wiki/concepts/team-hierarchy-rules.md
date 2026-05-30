---
type: concept
title: Team Hierarchy Rules
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, teams, governance, hierarchy]
related: [teams-and-users, team-types, multi-admin-model, roles-and-policies, glossary-tags]
sources: ["team-structure-in-openmetadata-official-documentat-20260514.md"]
---

# Team Hierarchy Rules

OpenMetadata enforces a strict, typed hierarchy for teams that governs parent-child relationships, data asset ownership, and organizational structure. Understanding these rules is essential for designing a governance model that aligns with your organization.

## Team Types and Their Constraints

| Team Type | Allowed Parents | Allowed Children | Multiple Parents | Can Own Data Assets |
|-----------|----------------|------------------|------------------|---------------------|
| **Organization** | None (root) | BusinessUnit, Division, Department, Group, Users | No | No |
| **BusinessUnit** | Organization, BusinessUnit | BusinessUnit, Division, Department, Group | No | No |
| **Division** | Organization, BusinessUnit, Division | Division, Department, Group | No | No |
| **Department** | Organization, BusinessUnit, Division, Department | Department, Group | **Yes** | No |
| **Group** | Organization, BusinessUnit, Division, Department, Group | Users only | **Yes** | **Yes** |

## Key Rules

1. **Organization is the root.** It represents the entire company, cannot have a parent, and cannot be deleted. Users who are not assigned to any team can be direct children of Organization.

2. **Only Groups can own data assets.** This is the fundamental governance rule: data asset ownership is restricted to leaf-level `Group` teams. All other team types (`Organization`, `BusinessUnit`, `Division`, `Department`) serve as organizational containers and cannot own assets.

3. **Group type is immutable.** Once a team is created as a `Group`, its `teamType` cannot be changed. This has significant implications for planning: if you anticipate a team needing to own data assets, it must be created as a `Group` from the start.

4. **Multiple parents for Department and Group.** `Department` and `Group` support multiple parents, enabling matrix-style organizational structures where a team reports to multiple higher-level units. `BusinessUnit` and `Division` are restricted to a single parent.

5. **No hardcoded depth limit.** While there is no enforced maximum depth, leaf nodes (`Group`) cannot have child teams. To extend the hierarchy, use intermediate types (`BusinessUnit`, `Division`, `Department`) as appropriate.

## Open Questions

- Can `BusinessUnit`, `Division`, or `Department` types be changed after creation? The official documentation only explicitly states immutability for `Group`. The behavior for other types remains unconfirmed.

## See Also

- [[teams-and-users]] — Overview of team and user management.
- [[team-types]] — Classification of team types and their roles.
- [[multi-admin-model]] — How team hierarchy enables decentralized administration.
- [[roles-and-policies]] — Access control built on team structure.
- [[glossary-tags]] — Business metadata governance tied to Group ownership.