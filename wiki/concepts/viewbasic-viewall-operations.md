---
type: concept
title: "ViewBasic and ViewAll Operations"
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, permissions, access-control, operations]
related: [hybrid-rbac-abac-model, roles-and-policies, resource-attributes]
sources: ["advanced-guide-for-roles-and-policies---openmetada-20260514.md"]
---
# ViewBasic and ViewAll Operations

`ViewBasic` and `ViewAll` are two distinct authorization operations in OpenMetadata that control the level of detail a user can access for a given asset. They represent a critical granular permission distinction within the [[hybrid-rbac-abac-model|Hybrid RBAC-ABAC Model]].

## ViewBasic

`ViewBasic` provides access only to the **basic details** of an asset:
- **Included:** Description, Tags, Owner, and fundamental metadata.
- **Excluded:** Profile data, Sample data, Data profile, Tests, and Queries.

**Key Points:**
- Suitable for viewing foundational asset metadata.
- Limited access for users who do not require in-depth technical details.

## ViewAll

`ViewAll` provides access to **all details** of an asset:
- **Included:** Everything in `ViewBasic`, plus Profile data, Sample data, Data profile, Tests, and Queries.

**Key Points:**
- Designed for users who need a complete view of the asset.
- Offers comprehensive insights and detailed metadata.

## Summary Table

| Feature | ViewBasic | ViewAll |
|---|---|---|
| Basic Details | ✅ Included | ✅ Included |
| Profile Data | ❌ Not Included | ✅ Included |
| Sample Data | ❌ Not Included | ✅ Included |
| Data Profile | ❌ Not Included | ✅ Included |
| Tests & Queries | ❌ Not Included | ✅ Included |

## Guidance

Choose the appropriate operation based on the level of access required:
- Use `ViewBasic` for roles that only need foundational metadata (e.g., business analysts viewing descriptions and tags).
- Use `ViewAll` for roles that require comprehensive technical details (e.g., data engineers needing profile data, sample data, and test results).