---
type: concept
title: Hybrid RBAC-ABAC Model
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, rbac, abac, access-control, security]
related: [roles-and-policies, viewbasic-viewall-operations, bot-authentication, teams-and-users, resource-attributes]
sources: ["advanced-guide-for-roles-and-policies---openmetada-20260514.md"]
---
# Hybrid RBAC-ABAC Model

The Hybrid RBAC-ABAC Model is the core authorization framework of OpenMetadata. It merges **Role-Based Access Control (RBAC)** with **Attribute-Based Access Control (ABAC)** to create a powerful and flexible access control mechanism.

In this hybrid model, access decisions are not based solely on a user's assigned role. Instead, OpenMetadata dynamically evaluates three factors:

1. **Who is the User** — Determined by the authentication process (human user via SSO or bot via JWT token).
2. **What Resource** — The target resource and its associated [[resource-attributes|attributes]], identified from the API call (e.g., Table, Topic, Pipeline).
3. **What Operation** — The specific action being requested, such as `Create`, `Delete`, `ViewAll`, or resource-specific operations like `ViewTests` and `ViewQueries` for Tables.

By synthesizing these three components, OpenMetadata dynamically ascertains whether a user or bot can perform a particular action on a specific resource. This fusion of RBAC and ABAC contributes to a robust and flexible access control mechanism, bolstering the security and control of the OpenMetadata environment.

The model is reinforced by:
- **SSO Integration** with providers like Azure AD, Google, Okta, Auth0, and OneLogin.
- **Team Hierarchy** that mirrors organizational structure for granular access control.
- **Roles and Policies** that combine user attributes, roles, and resource attributes to determine permissions.

For the granular permission levels within this model, see [[viewbasic-viewall-operations]]. For how automated applications authenticate, see [[bot-authentication]].