---
type: concept
title: "Search RBAC"
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, rbac, search, security, governance]
related: [roles-and-policies, authorization-policies, authorization-rules, hybrid-rbac-abac-model]
sources: ["building-blocks-of-authorization---rules-policies--20260514.md"]
---

# Search RBAC

Search RBAC (Role-Based Access Control) is an optional feature in OpenMetadata that extends authorization enforcement to search functionality. When enabled, search results are filtered based on the user's assigned [[roles-and-policies|Roles and Policies]], ensuring that users can only discover data assets they have explicit permission to access.

## Default Behavior

**Search RBAC is disabled by default.** In the default configuration, all users can see all data assets in search results, regardless of their permissions. This means a user might discover assets via search that they cannot actually access — a potential gap between discoverability and authorization.

## Enabling Search RBAC

To enable or disable Search RBAC:
1. Navigate to **Settings > Preferences > Search** in the OpenMetadata UI
2. Toggle the Search RBAC setting

## Implications of Enabling Search RBAC

- **Restricted Search Results**: Users will only see search results for data assets they have explicit permissions to access, enhancing data security and compliance
- **Policy Enforcement at Search Level**: The system enforces policies at the search level, ensuring unauthorized users cannot discover sensitive metadata
- **Alignment with Governance**: Search behavior aligns with the organization's data governance and security requirements

## Additional Considerations

- **Role and Policy Configuration**: Ensure that [[authorization-policies|Policies]] and [[roles-and-policies|Roles]] are appropriately configured to reflect desired access controls before enabling Search RBAC
- **Testing**: After enabling Search RBAC, conduct thorough testing to verify that users can access only the data assets permitted by their roles and policies
- **User Experience Impact**: Users accustomed to seeing all assets in search may need communication about the change, as previously visible assets may disappear from search results

## Relationship to Authorization Model

Search RBAC is a presentation-layer enforcement of the same [[hybrid-rbac-abac-model|hybrid RBAC-ABAC model]] that governs direct resource access. It ensures consistency between what users can discover and what they can access, closing the gap that exists when Search RBAC is disabled.