---
type: source
title: "Building Blocks of Authorization - Rules, Policies, and Roles"
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, rbac, abac, rules, policies, roles, spel, conditions]
related: [roles-and-policies, hybrid-rbac-abac-model, resource-attributes, viewbasic-viewall-operations, teams-and-users, team-hierarchy-rules, authorization-rules, authorization-policies, spel-conditions, search-rbac, default-organization-policy]
sources: ["building-blocks-of-authorization---rules-policies--20260514.md"]
authors: ["OpenMetadata Documentation"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies/authorization"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# Building Blocks of Authorization - Rules, Policies, and Roles

Official OpenMetadata v1.12.x documentation detailing the three-tier authorization architecture: Rules (atomic building blocks with SpEL-based conditions), Policies (bundles of rules with Deny precedence and team-level assignment), and Roles (structured hierarchies of policies aligned with job functions). Covers the default Organization Policy with its two out-of-the-box rules, policy inheritance through team hierarchy, and the optional Search RBAC feature.

## Key Topics

- **Rules**: Atomic authorization units with Name, Description, Resources, Operations, Condition (SpEL), and Effect (Allow/Deny)
- **Conditions**: SpEL-based functions including `noOwner()`, `isOwner()`, `matchAllTags()`, `matchAnyTag()`, `matchTeam()`, `hasDomain()`, with logical operators `&&` and `||`
- **Policies**: Collections of rules evaluated in user session context; Deny takes precedence in conflicts; assigned to teams only (not individual users); inherited down the organizational hierarchy
- **Roles**: Bundles of policies aligned with job functions (e.g., Data Engineer, Data Scientist, Data Steward, Data Consumer); assignable to users or teams
- **Default Organization Policy**: `OrganizationPolicy-NoOwner-Rule` (allow ownership assignment to unowned resources) and `OrganizationPolicy-Owner-Rule` (grant extensive rights to resource owners)
- **Policy Inheritance**: Top-down propagation from Organization to all subordinate teams; lower-level teams can add stricter policies
- **Search RBAC**: Optional setting (disabled by default) that filters search results based on user roles and policies; enabled via Settings > Preferences > Search