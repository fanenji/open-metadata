---
type: concept
title: Authorization Rules
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, rbac, abac, rules, spel, conditions]
related: [authorization-policies, spel-conditions, roles-and-policies, hybrid-rbac-abac-model, resource-attributes, viewbasic-viewall-operations, default-organization-policy]
sources: ["building-blocks-of-authorization---rules-policies--20260514.md"]
---

# Authorization Rules

A Rule is the atomic building block of authorization in OpenMetadata. Each rule defines a single access control decision with six components:

- **Name**: A unique identifier for the rule
- **Description**: Human-readable explanation of the rule's purpose
- **Resources**: The target resources this rule applies to — either a specific resource type (e.g., `Table`) or `All` to apply across all resources
- **Operations**: The operations this rule governs — either a specific operation (e.g., `EditOwner`) or `All` to cover all operations
- **Condition**: A SpEL (Spring Expression Language) expression that evaluates to `true` or `false` against the resource's attributes at runtime
- **Effect**: Either `Allow` or `Deny` — the action taken when the condition evaluates to `true`

Rules are the foundation upon which [[authorization-policies|Policies]] and [[roles-and-policies|Roles]] are built. They are not assigned directly to users or teams; instead, they are bundled into Policies, which are then assigned to teams or bundled into Roles.

## Conditions

The Condition field is the core innovation of OpenMetadata's authorization model, enabling dynamic, attribute-based access control. Conditions are written using SpEL expressions that evaluate properties of the resource being accessed. For a complete reference of all available condition functions, see [[spel-conditions]].

Conditions can be combined using logical operators:
- `&&` (AND): Both conditions must be true
- `||` (OR): At least one condition must be true

Example combined condition:
```
noOwner() && matchAllTags('PersonalData.Personal', 'Tier.Tier1', 'Business Glossary.Clothing')
```
This returns `true` only if the data asset has no owner AND simultaneously matches all three specified tags.

## Relationship to the Hybrid Model

Rules with SpEL-based conditions are the concrete implementation of the Attribute-Based Access Control (ABAC) component within OpenMetadata's [[hybrid-rbac-abac-model|hybrid RBAC-ABAC model]]. The conditions evaluate [[resource-attributes]] (owner, tags, domain, team) at runtime, while the Resources and Operations fields define the scope of the rule. The Effect field determines whether access is granted or denied.

## Operations Granularity

The Operations field supports the granular operation types documented in [[viewbasic-viewall-operations]], including `ViewBasic`, `ViewAll`, `EditDescription`, `EditOwner`, and many others. This allows administrators to craft precise rules that distinguish between viewing basic metadata versus viewing comprehensive data including profiles, samples, and queries.