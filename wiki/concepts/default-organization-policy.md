---
type: concept
title: "Default Organization Policy"
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, policies, rules, default-configuration, ownership]
related: [authorization-policies, authorization-rules, roles-and-policies, spel-conditions]
sources: ["building-blocks-of-authorization---rules-policies--20260514.md"]
---

# Default Organization Policy

OpenMetadata ships with a pre-configured Organization Policy that establishes baseline governance rules at the organizational level. This policy is accessible via **Settings > Policies > Organization Policy** and contains two default rules.

## OrganizationPolicy-NoOwner-Rule

**Purpose**: Allows users to assign ownership to resources that currently have no owner.

**Behavior**: If a user accesses a data asset (e.g., `fact_table`) and finds it unowned, they can modify the ownership field to establish a new owner. However, for assets that already have an assigned owner (e.g., `dim_address`), any attempt to change ownership will be restricted.

**Condition**: Uses the `noOwner()` [[spel-conditions|SpEL condition]] to evaluate whether the resource lacks an owner.

## OrganizationPolicy-Owner-Rule

**Purpose**: Grants extensive permissions based on ownership of a data asset.

**Behavior**: When a user who either personally owns a data asset or belongs to the team that owns it logs in, they are granted comprehensive rights. They can modify all properties of that data asset and access complete information about it.

**Condition**: Uses the `isOwner()` [[spel-conditions|SpEL condition]] to verify the user's ownership relationship to the resource.

## Design Philosophy

These default rules ensure clarity in access control based on ownership status. They establish a foundation where:
- Unowned assets can be claimed by any user
- Owners have full control over their assets
- Organizations can build additional, more restrictive [[authorization-policies|Policies]] on top of this baseline

The Organization Policy applies to all members throughout the entire organizational hierarchy via [[authorization-policies#inheritance-and-propagation|policy inheritance]].