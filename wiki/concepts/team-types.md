---
type: concept
title: Team Types
created: 2026-05-14
updated: 2026-05-14
tags: [administration, teams, openmetadata, hierarchy]
related: [teams-and-users, multi-admin-model, hierarchical-team-structure, roles-and-policies]
sources: ["manage-teams-and-users---openmetadata-documentatio-20260514.md"]
---
# Team Types

Team Types in OpenMetadata are classifications that Administrators can assign when creating teams, allowing the platform's hierarchical structure to mirror various organizational units. The official documentation mentions that Admins can create various team types and change a team's type, but does not enumerate the available types in this source.

## Known Information

- Team types are mentioned as a capability: Admins can create teams of different types (e.g., Department, Division, Group) to represent organizational units.
- Admins can change the team type of an existing team.
- Team types contribute to the versatile hierarchical structure that aligns with an organization's setup.

## Open Questions

- **What are the specific team types available?** The source references the capability but does not provide a definitive list.
- **How does changing a team type affect existing users, policies, and child teams?** The documentation mentions the ability to change team type but does not detail the downstream effects.
- **Do team types influence policy inheritance or access control?** The relationship between team types and the [[roles-and-policies|Roles and Policies]] framework is not clarified in this source.

## Related Concepts

- [[teams-and-users]] — The broader concept of team and user management.
- [[hierarchical-team-structure]] — The multi-level organizational model that team types help define.
- [[multi-admin-model]] — Decentralized administration that may interact with team type boundaries.