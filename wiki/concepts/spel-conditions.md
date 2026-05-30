---
type: concept
title: "SpEL Conditions for Authorization"
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, spel, conditions, abac, functions]
related: [authorization-rules, authorization-policies, hybrid-rbac-abac-model, resource-attributes, roles-and-policies]
sources: ["building-blocks-of-authorization---rules-policies--20260514.md"]
---

# SpEL Conditions for Authorization

OpenMetadata provides SpEL (Spring Expression Language)-based conditions that administrators can use when creating [[authorization-rules|Rules]]. These conditions evaluate [[resource-attributes|resource attributes]] at runtime, enabling dynamic, attribute-based access control as part of the [[hybrid-rbac-abac-model|hybrid RBAC-ABAC model]].

## Available Condition Functions

### `noOwner()`
Returns `true` if the resource being accessed has no assigned owner.

**Example**: Applied to `fact_orders` table — if the table lacks an owner, returns `true`; if an owner is present, returns `false`.

### `isOwner()`
Returns `true` if the user accessing the resource is the owner of the resource (either personally or via team ownership).

### `matchAllTags(tagFqn, [tagFqn...])`
Returns `true` if the resource has **all** of the specified tags from the tag list.

**Example**: `matchAllTags('PII.Sensitive', 'Tier.Tier1')` returns `true` only if the resource carries both the `PII.Sensitive` tag and the `Tier.Tier1` tag.

### `matchAnyTag(tagFqn, [tagFqn...])`
Returns `true` if the resource has **any** of the specified tags from the tag list.

**Example**: `matchAnyTag('PII.Sensitive')` applied to `dim_address` table that carries the `PII.Sensitive` tag yields `true`. Without this specific tag, it returns `false`.

### `matchTeam()`
Returns `true` if the user belongs to the team that owns the resource.

### `hasDomain()`
Returns `true` if the logged-in user has domain access to the entity being accessed.

## Logical Operators

Conditions can be combined using standard logical operators:

- `&&` (AND): Both conditions must evaluate to `true`
- `||` (OR): At least one condition must evaluate to `true`

**Example combined condition**:
```
noOwner() && matchAllTags('PersonalData.Personal', 'Tier.Tier1', 'Business Glossary.Clothing')
```
This returns `true` only if the data asset has no assigned owner AND simultaneously matches all three specified tags.

## Usage Context

Conditions are used to assess DataAssets (Tables, Topics, Dashboards, etc.) for specific attributes. They are specified in the Condition field of a Rule and evaluated at access time against the target resource's current state. This enables administrators to craft rules that holistically consider the data asset and its attributes when dictating access control.