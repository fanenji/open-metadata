---
type: concept
title: "Multi-Team Membership"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, teams, users, access-control, governance]
related: [teams-and-users, roles-and-policies, team-hierarchy-rules, how-to-add-users-to-teams]
sources: ["how-to-add-users-to-teams---openmetadata-documenta-20260514.md"]
---

# Multi-Team Membership

Multi-team membership is the capability in OpenMetadata that allows a single user to belong to multiple Teams simultaneously. This feature enables flexible organizational modeling where individuals may participate in multiple functional groups, cross-functional projects, or matrix-style reporting structures.

## Supported Scenarios

- **During user creation:** A new user can be added to multiple Teams at the time of invitation. This is explicitly documented in the [[how-to-add-users-to-teams]] procedure.
- **For existing users:** The documentation describes an "Add User" flow that appears to add a user to a single team at a time. It is unclear whether the UI supports adding an existing user to multiple teams in a single operation, or whether multiple "Add User" operations are required.

## Implications for Role Inheritance

Since users inherit Roles from all Teams they belong to (see [[roles-and-policies]]), multi-team membership raises important questions about role conflict resolution:

- What happens when a user inherits conflicting roles from different teams?
- Is there a precedence or priority system for resolving such conflicts?
- Does the system apply a union of all permissions, or does a deny rule from one team override an allow rule from another?

These questions are not addressed in the current documentation and represent an open area for investigation.

## Relationship to Team Hierarchy

Multi-team membership operates within the constraints of the [[team-hierarchy-rules]]. A user can be a member of teams at different levels of the hierarchy, and potentially across different branches of the organizational tree. This flexibility supports complex organizational structures but requires careful administration to avoid unintended permission grants.

## See Also

- [[how-to-add-users-to-teams]] — Step-by-step procedures for adding users to teams.
- [[teams-and-users]] — Conceptual overview of teams and users.
- [[roles-and-policies]] — Access control mechanisms.