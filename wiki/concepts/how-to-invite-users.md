---
type: concept
title: How to Invite Users
created: 2026-05-14
updated: 2026-05-14
tags: [administration, user-management, onboarding, teams, roles]
related: [teams-and-users, roles-and-policies, how-to-add-a-team, multi-admin-model, admin-toggle]
sources: ["how-to-invite-users-to-openmetadata---openmetadata-20260514.md"]
---

# How to Invite Users

Inviting users is the primary administrative workflow for onboarding collaborators onto the OpenMetadata platform. This procedure is performed by an Admin through the UI and involves specifying the user's identity, team memberships, and role assignments.

## Navigation Path

1. Navigate to **Settings** in the left sidebar.
2. Select **Team & User Management**.
3. Click on the **Users** tab.
4. Click the **Add Users** button.

## Invitation Form Fields

The Add Users form presents the following fields:

| Field | Description |
|-------|-------------|
| **Email** | The email address of the user to invite. This serves as the unique identifier for the account. |
| **Display Name** | The name that will be displayed throughout the platform for this user. |
| **Description** | An optional free-text description providing context about the user (e.g., role, department). |
| **Teams** | One or more teams the user will belong to. Users can be invited to multiple teams simultaneously. Teams must already exist — see [[how-to-add-a-team]]. |
| **Roles** | One or more roles explicitly assigned to the user. Multiple roles can be assigned. |
| **Admin** | A toggle that grants the user full administrative privileges. See [[admin-toggle]] for details. |

## Role Inheritance

Users automatically inherit the roles assigned to the teams they belong to. This means:

- If a team has a role assigned (e.g., "Data Steward"), all members of that team receive that role.
- Additional roles can be explicitly assigned to a user through the **Roles** field, supplementing the inherited roles.
- The effective set of permissions for a user is the union of inherited roles and explicitly assigned roles.

This inheritance model is a core principle of the [[roles-and-policies]] system and reduces administrative overhead by ensuring consistent policy application through the team hierarchy.

## Relationship to Other Procedures

- **Prerequisite**: Teams must be created before users can be invited to them. See [[how-to-add-a-team]].
- **Follow-up**: After invitation, users can be added to additional teams. See the "How to Add Users to Teams" procedure.
- **Governance**: The Admin toggle supports the [[multi-admin-model]] by allowing designation of additional platform administrators.

## Open Questions

- Does the **Admin** toggle assign a specific built-in role, or does it grant a separate super-admin flag? How does it interact with roles explicitly assigned in the **Roles** field? The official documentation does not clarify this interaction.