---
type: synthesis
title: User and Role Management Workflow
created: 2026-05-22
updated: 2026-05-22
tags: [openmetadata, administration, roles, policies, teams, workflow]
related: [openmetadata-administration, roles-and-policies, teams-and-users, hybrid-rbac-abac-model, policy-use-cases, data-asset-ownership, permission-debugger, team-types, team-hierarchy-rules, authorization-rules, authorization-policies, spel-conditions, tag-based-access-control, default-organization-policy, data-steward-role, serviceowner-role, multi-admin-model, viewbasic-viewall-operations]
sources: ["thinkwe-need-to-answer-the-question-explain-in-det-2026-05-22-061312.md"]
---
# User and Role Management Workflow

Managing users and roles in OpenMetadata is a two-pronged process: organizing users into a hierarchical team structure and controlling access via the Roles & Policies framework. These two systems are tightly integrated, with teams providing the organizational grouping and roles/policies defining what users can do.

## Recommended 5-Step Workflow

The following sequence represents the recommended approach for setting up user and role management:

1. **Establish your organizational hierarchy** — Create teams (BusinessUnit, Division, Department, Group) that mirror your real-world structure. Refer to [[team-types]] and [[team-hierarchy-rules]] for the complete parent-child constraints.

2. **Invite users** — Add users to the appropriate teams, optionally attaching one or more Roles directly. Users inherit roles from all teams they belong to. See [[how-to-add-users-to-teams]] for procedural details.

3. **Assign baseline access** — Keep the default Organization Policy. Create additional Roles tailored to your departments (e.g., ServiceOwner, DataSteward). The [[default-organization-policy]] provides the foundational rules that enable basic collaboration.

4. **Layer restrictive policies** — Add Deny rules for sensitive data (tag-based) or to confine teams to their own assets. See [[policy-use-cases]] for concrete design patterns including Team-Owned Data Protection and Tag-Based Access Control.

5. **Verify with the Permission Debugger** — Confirm that the intended effective permissions are in place before going live. Use the [[permission-debugger]] to simulate access checks and review which rules matched.

## Design Principle

Start with the default Organization Policy, add Allow rules for specific capabilities, and use Deny rules for restrictions. SpEL conditions (documented in [[spel-conditions]]) provide dynamic, attribute-based decisions within rules.

## Core Building Blocks

- **Teams**: Hierarchical organizational units (Organization, BusinessUnit, Division, Department, Group). Only Group teams can own data assets. See [[team-types]].
- **Roles**: Named bundles of Policies, functioning as job function profiles (e.g., "Data Steward", "Service Owner"). See [[roles-and-policies]].
- **Policies**: Collections of Rules assigned to users or teams, inherited down the hierarchy. See [[authorization-policies]].
- **Rules**: Atomic authorization building blocks with Effect (Allow/Deny), Resources, Operations, and SpEL Conditions. Deny always takes precedence over Allow. See [[authorization-rules]].
- **ViewBasic vs ViewAll**: Granular permission distinction for metadata visibility. See [[viewbasic-viewall-operations]].

## Policy Design Patterns

Four official use cases are consolidated in [[policy-use-cases]]:

1. **ServiceOwner Role** — Delegates service creation and ingestion pipeline management to non-Admin users.
2. **Data Steward Role** — Grants governance capabilities (glossary management, description/tag editing) without full administration.
3. **Team-Owned Data Protection** — Restricts data asset access to the owning team using `isOwner()` and `matchTeam()` conditions.
4. **Tag-Based Access Control** — Uses classification tags like `PII.Sensitive` as ABAC attributes to dynamically restrict access.

## Multi-Admin Model

OpenMetadata supports a [[multi-admin-model]] where different Administrators can independently manage separate team branches, enabling decentralized governance without a single super-admin bottleneck.

## Open Question

A user can be assigned Roles directly and also inherit them from Teams. The general Deny-over-Allow precedence applies, but the detailed mechanics of role conflict resolution when a user has multiple roles with overlapping rules warrants further investigation.