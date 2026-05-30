---
type: concept
title: Teams and Users
created: 2026-05-14
updated: 2026-05-14
tags: [administration, collaboration, teams, users, onboarding, access-control, openmetadata, governance]
related: [openmetadata-administration, roles-and-policies, openmetadata-collaboration, multi-admin-model, team-types, hierarchical-team-structure]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md", "manage-teams-and-users---openmetadata-documentatio-20260514.md"]
---
# Teams and Users

Teams and Users form the organizational backbone of OpenMetadata, enabling collaboration, access management, and governance. OpenMetadata provides a versatile hierarchical team structure that allows administrators to mirror their real-world organizational hierarchy within the platform. Teams enable hierarchical grouping of users for streamlined onboarding, collaboration, and fine-grained access control.

## Hierarchical Team Structure

The team structure in OpenMetadata is hierarchical and multi-level, meaning a team can contain sub-teams. This design mirrors real-world organizational charts and allows administrators to:

- Model departments, divisions, groups, and other organizational units
- Manage access at the department, division, or project level
- Delegate administration to team leads
- Inherit policies and permissions down the hierarchy

Admins can create various [[team-types|team types]] to represent different parts of the organization. Once users are onboarded into the relevant teams, their platform access aligns with their organizational roles.

## User Onboarding

Administrators can add individual users or create teams to streamline onboarding. The recommended workflow is:

1. **Create Teams** — Establish the hierarchical structure that reflects the organization.
2. **Invite Users** — Add users to the appropriate teams, ensuring they are part of the correct organizational unit.
3. **Assign Roles** — Apply [[roles-and-policies|Roles and Policies]] to teams to grant appropriate access, which cascade through the hierarchy.

## Relationship to Roles and Policies

The team structure serves as the foundation upon which [[roles-and-policies|Roles and Policies]] are applied. By organizing users into teams that reflect the organizational hierarchy, administrators can assign policies at the team level, ensuring that access controls cascade appropriately through the hierarchy. This inheritance model simplifies access management at scale.

## Collaboration

Teams are central to [[openmetadata-collaboration|OpenMetadata Collaboration]]. They enable:

- Shared ownership of data assets
- Team-based activity feeds and conversations
- Collaborative workflows for data quality and governance

## Multi-Admin Model

A key design feature is the [[multi-admin-model|multi-Admin model]]. Because an organization can have multiple Administrators, each can independently manage specific teams and departments. This enables decentralized governance and scalable administration across large organizations, where different business units can operate semi-autonomously within the platform. It also allows large organizations to distribute administrative responsibilities without creating bottlenecks.

## Administration

Managing teams and users is a core administrative function covered under [[openmetadata-administration]]. The Admin Guide provides detailed procedures for creating teams, inviting users, adding users to teams, changing team types, and other administrative tasks.