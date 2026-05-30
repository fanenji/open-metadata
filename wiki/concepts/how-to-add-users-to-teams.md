---
type: concept
title: "How to Add Users to Teams"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, teams, users, administration, how-to, onboarding]
related: [teams-and-users, how-to-add-a-team, roles-and-policies, team-hierarchy-rules, multi-team-membership, role-inheritance-via-teams]
sources: ["how-to-add-users-to-teams---openmetadata-documenta-20260514.md"]
---

# How to Add Users to Teams

This page documents the step-by-step procedures for adding users to teams in OpenMetadata. There are two distinct workflows depending on whether the user is being newly invited to the platform or already exists.

## Adding Users During Invitation

When inviting a new user to OpenMetadata, you can simultaneously add them to one or more relevant Teams and assign them the appropriate Roles. This streamlines onboarding by combining user creation with team placement.

**Note:** You can add a User to multiple Teams when creating a New User.

## Adding Existing Users to Teams

If the user already exists in OpenMetadata:

1. Navigate to **Settings >> Team & User Management >> Teams >> Users Tab**.
2. Select the specific team you would like to add a user to. If the team has sub-teams, navigate to the required sub-team.
3. Click **Add User**.
4. Search for the user, select the checkbox next to their name, and click **Update**.

## Role Inheritance

Users automatically inherit the Roles assigned to the Teams they belong to. This is a core access control mechanism that simplifies permission management by linking roles to team membership rather than requiring per-user role assignment. For details on how roles and policies work, see [[roles-and-policies]].

## Multi-Team Membership

A user can belong to multiple Teams. This is explicitly supported during the new user creation flow. The documentation does not clarify whether existing users can be added to multiple teams through the "Add User" flow, which may imply single-team addition for existing users. For the broader implications of team membership, see [[multi-team-membership]].

## Relationship to Team Hierarchy

Teams in OpenMetadata follow a strict hierarchy (see [[team-hierarchy-rules]]). When adding users, you must navigate to the specific sub-team level where the user should be placed. This reinforces the hierarchical structure and ensures users are added at the correct organizational level. For creating teams, see [[how-to-add-a-team]].

## See Also

- [[teams-and-users]] — Conceptual overview of teams and users in OpenMetadata.
- [[how-to-add-a-team]] — Procedure for creating new teams.
- [[roles-and-policies]] — Access control mechanisms and role definitions.
- [[team-hierarchy-rules]] — Parent-child constraints and team type rules.