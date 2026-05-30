---
type: concept
title: How to Change Team Type
created: 2026-05-14
updated: 2026-05-14
tags: [teams, administration, team-types, ui-procedure, governance]
related: [team-types, team-hierarchy-rules, how-to-add-a-team, public-team, multi-team-membership]
sources: ["how-to-change-the-team-type-official-documentation-20260514.md"]
---

# How to Change Team Type

The administrative procedure for altering an existing team's type classification (e.g., from `Department` to `Division`) through the OpenMetadata UI. This capability provides flexibility when initial team structuring was incorrect or organizational needs evolve.

## Procedure

1. Navigate to **Settings > Team & User Management > Teams**.
2. Click on the target team name to open its details page.
3. Locate the **Type** field and click its edit icon.
4. Select the desired new type from the dropdown and click ✅ to confirm.
5. The change takes effect immediately.

## Prerequisites

Before changing a team type, administrators should thoroughly understand the [[team-types|five team type classifications]] and their implications. The official documentation explicitly references the [[team-types|Team Structure in OpenMetadata]] page as required reading.

## Known Constraints and Warnings

> ⚠️ **Critical Warning:** The official procedure documentation does not explicitly state any constraints on type changes. However, based on related documentation, the following concerns must be considered:

### Group Immutability

The [[how-to-add-a-team]] documentation explicitly warns that the `Group` type **cannot be changed** after creation. It is unclear whether this restriction applies to the type-change procedure described here. **Assume Group type changes are not permitted** unless verified otherwise.

### Hierarchy Validity

Changing a team's type may violate the strict parent-child constraints defined in [[team-hierarchy-rules]]. For example:
- Changing a `Division` to a `Group` could create an invalid hierarchy if the team has child teams, since `Group` cannot have children.
- Changing a `Department` to a `BusinessUnit` could violate the rule that `BusinessUnit` must be a child of `Organization`.

The official procedure does not document whether the UI validates these constraints before allowing the change, or whether it is the administrator's responsibility to ensure hierarchy integrity.

### Impact on Child Teams

If a parent team's type is changed to one that does not support its current children (per the [[team-hierarchy-rules|parent-child matrix]]), the status of those child teams is undefined. Administrators should restructure the hierarchy before changing a parent team's type.

### Data Asset Ownership

Only `Group` type teams can own data assets. Changing a `Group` to another type would strip its data asset ownership capabilities. Conversely, changing a non-`Group` team to `Group` would grant ownership capabilities.

### Role Assignments

The effect of type changes on existing role assignments and inherited policies is not documented. Administrators should verify role assignments after any type change.

## Relationship to Other Procedures

- [[how-to-add-a-team]] — Covers initial team creation, where the type is set and (for Groups) made permanent.
- [[team-hierarchy-rules]] — Defines the parent-child constraints that may be violated by a type change.
- [[team-types]] — Defines the five team classifications and their capabilities.

## Open Questions

- Can a `Group` type be changed using this procedure, or is it truly immutable?
- Does the UI validate hierarchy constraints during type change?
- What happens to child teams when a parent's type is changed to an incompatible type?
- Are role assignments preserved, modified, or stripped during a type change?