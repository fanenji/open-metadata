---
type: concept
title: Resource Attributes
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, abac, access-control, resources]
related: [hybrid-rbac-abac-model, roles-and-policies, viewbasic-viewall-operations]
sources: ["advanced-guide-for-roles-and-policies---openmetada-20260514.md"]
---
# Resource Attributes

Resource Attributes are properties of the target resource identified from API calls, used in the Attribute-Based Access Control (ABAC) component of OpenMetadata's [[hybrid-rbac-abac-model|Hybrid RBAC-ABAC Model]].

## Role in Authorization

Resource Attributes form the second factor in the three-factor authorization framework: **What Resource**. When an API call is made, OpenMetadata identifies the target resource and its associated attributes. These attributes are then evaluated alongside the user's identity and the requested operation to determine whether access should be granted.

## Resource Types

The following resources correspond to entities within OpenMetadata and have associated attributes used in authorization decisions:

- Table
- Topic
- Pipeline
- Dashboard
- ML Model
- Container
- And other metadata entities

Each resource type may have specific attributes that influence access decisions, such as ownership, domain, tags, or custom properties.

## Operations on Resources

There are common operations that apply to all resources:
- `Create`
- `Delete`
- `ViewAll`

Additionally, each resource can have resource-specific operations. For example, the Table resource supports:
- `ViewTests`
- `ViewQueries`

The granularity of operations is further defined by the distinction between [[viewbasic-viewall-operations|ViewBasic and ViewAll]].