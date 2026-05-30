---
type: concept
title: Resource Types (Permission Debugger)
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, authorization, abac, resource-attributes, permission-debugger]
related: [permission-debugger, resource-attributes, authorization-rules, hybrid-rbac-abac-model]
sources: ["permission-debugger-analyze-and-troubleshoot-user--20260514.md"]
---

# Resource Types (Permission Debugger)

The Permission Debugger in OpenMetadata supports permission checks against a fixed enumerable set of resource types. These resource types define the scope of entities that can be evaluated during a permission simulation and correspond directly to the [[resource-attributes]] used in the [[hybrid-rbac-abac-model|ABAC]] condition evaluation within [[authorization-rules]].

## Complete Resource Type List

The following resource types are available in the Permission Debugger dropdown:

- `user`
- `team`
- `table`
- `database`
- `glossary`
- `tag`
- `glossaryTerm`
- `searchIndex`
- `mlModel`
- `container`
- `topic`
- `pipeline`
- `dashboard`
- `databaseSchema`

## Relationship to Authorization Framework

Each resource type maps to a set of [[resource-attributes]] that can be referenced in SpEL conditions within [[authorization-rules]]. When the Permission Debugger evaluates a check, it uses the selected resource type to determine which attributes are available for condition matching.

For instance-level debugging, the optional **Resource FQN** field allows administrators to test permissions against a specific resource instance (e.g., `sample_data.ecommerce_db.shopify.dim_address_clean`), which is essential for validating [[tag-based-access-control]] policies that depend on instance-specific attributes like tags or domains.