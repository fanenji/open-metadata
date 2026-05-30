---
type: concept
title: Admin Toggle
created: 2026-05-14
updated: 2026-05-14
tags: [administration, access-control, user-management]
related: [how-to-invite-users, roles-and-policies, multi-admin-model]
sources: ["how-to-invite-users-to-openmetadata---openmetadata-20260514.md"]
---

# Admin Toggle

The Admin toggle is a UI control available during the user invitation workflow that grants a user full administrative privileges on the OpenMetadata platform. It appears as a simple on/off switch in the **Add Users** form.

## Behavior

When toggled on, the invited user receives complete administrative access to the platform. This provides a quick way to designate platform administrators without requiring separate role configuration through the [[roles-and-policies]] system.

## Ambiguity

The official documentation does not specify the underlying mechanism:

- It is unclear whether the toggle assigns a specific built-in Admin role (e.g., a predefined "Admin" role in the roles system) or whether it sets a separate super-admin flag that operates independently of the role-based access control model.
- The interaction between the Admin toggle and roles explicitly assigned in the **Roles** field of the invitation form is not documented. For example, if a user is given the Admin toggle and also assigned a restricted role, it is unknown which takes precedence or how conflicts are resolved.

## Relationship to Multi-Admin Model

The Admin toggle directly supports the [[multi-admin-model]] by enabling the designation of multiple administrators during user onboarding. This allows decentralized governance where different administrators can manage separate teams and departments.