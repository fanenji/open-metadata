---
type: concept
title: Authorization Policies
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, policies, rbac, inheritance, deny-precedence]
related: [authorization-rules, roles-and-policies, teams-and-users, team-hierarchy-rules, default-organization-policy, spel-conditions]
sources: ["building-blocks-of-authorization---rules-policies--20260514.md"]
---

# Authorization Policies

A Policy is a collection of multiple [[authorization-rules|Rules]] that together define a set of access controls. When a user accesses a resource, the policy evaluates all its associated rules in the context of that user's current session.

## Conflict Resolution: Deny Precedence

When a policy contains conflicting rules — for example, one rule allows `EditDescription` for all resources while another denies the same operation — the **Deny effect takes precedence**. This security-first posture ensures that an explicit denial cannot be overridden by a more permissive rule within the same policy.

## Policy Assignment

Policies are assigned to **teams**, not to individual users. This design choice means:
- Policies flow through the organizational hierarchy via team membership
- Individual user exceptions require team-level workarounds
- Administrators should plan team structures with policy assignment in mind

## Inheritance and Propagation

Policy inheritance follows a top-down model through the [[team-hierarchy-rules|team hierarchy]]:

- **Organization level**: A policy assigned at the Organization level applies to all members throughout the entire hierarchy
- **Division level**: A policy assigned to a Division cascades to all subordinate Departments, Groups, and their members
- **Team level**: A policy assigned to a specific team applies only to that team's members

This architecture enables a design philosophy where broad, potentially more lenient rules are established at the organizational level, while lower-level teams can sculpt stricter, more tailored policies. For example, an organization-wide policy might allow general access, while a specific team's policy might dictate: "Deny access to everyone outside of Team 1."

## Relationship to Roles

While Policies are the direct enforcement mechanism, [[roles-and-policies|Roles]] provide a higher-level abstraction by bundling multiple policies aligned with a job function. Roles simplify administration by allowing administrators to assign a single role rather than multiple individual policies.

## Default Organization Policy

OpenMetadata ships with a [[default-organization-policy|default Organization Policy]] containing two pre-configured rules that establish baseline governance for ownership assignment and owner privileges.