---
type: entity
title: Permission Debugger
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, administration, authorization, rbac, abac, diagnostics]
related: [hybrid-rbac-abac-model, authorization-rules, authorization-policies, resource-attributes, viewbasic-viewall-operations, roles-and-policies, audit-logs, tag-based-access-control, search-rbac]
sources: ["permission-debugger-analyze-and-troubleshoot-user--20260514.md"]
---

# Permission Debugger

The Permission Debugger is a diagnostic UI tool in OpenMetadata that allows administrators to analyze and troubleshoot user access permissions. It simulates permission checks for a given user on a selected resource and operation, providing detailed insight into the authorization decision process without altering any actual permissions.

## Purpose

The debugger serves as the primary troubleshooting companion to the [[roles-and-policies|Roles and Policies]] system. While [[audit-logs|Audit Logs]] record what *has happened* historically, the Permission Debugger simulates what *would happen* for a given user-resource-operation combination, making it essential for:

- Debugging why a specific user cannot access a resource
- Validating that newly created [[authorization-policies]] behave as expected
- Understanding the effective permissions resulting from the [[hybrid-rbac-abac-model]]
- Tracing which rules fire during evaluation for a specific scenario

## How to Access

Navigate to **Settings > Access Control > Permission Debugger** in the OpenMetadata UI.

## Workflow

### 1. Select a User

Use the input field to search for and select the user whose permissions you want to inspect.

### 2. Define the Permission Check

Three parameters define the check:

| Parameter | Description | Required |
|-----------|-------------|----------|
| **Resource** | The resource type to check against. Options include: `user`, `team`, `table`, `database`, `glossary`, `tag`, `glossaryTerm`, `searchIndex`, `mlModel`, `container`, `topic`, `pipeline`, `dashboard`, `databaseSchema` | Yes |
| **Operation** | The action to check. Examples: `ViewAll`, `EditAll`, `Deploy`, `Trigger`, `Kill`, `GenerateToken` | Yes |
| **Resource FQN or ID** | A Fully Qualified Name or unique ID of a specific resource instance for instance-level debugging | No |

The resource types correspond to the [[resource-attributes]] used in ABAC condition evaluation. The operations map to those defined in [[authorization-rules]].

### 3. Evaluate Permission

Click the **Evaluate** button to perform the simulation. The debugger returns a decision (ALLOWED or DENIED) and an Evaluation Summary.

## Evaluation Summary Metrics

| Metric | Meaning |
|--------|---------|
| **Policies Evaluated** | Number of [[authorization-policies]] that were checked |
| **Rules Evaluated** | Total number of [[authorization-rules]] across all evaluated policies |
| **Matching Rules** | Number of rules whose conditions matched the user, resource, and operation |
| **Allow Rules** | Number of matching rules with Effect = Allow |
| **Deny Rules** | Number of matching rules with Effect = Deny |
| **Evaluation Time** | Time taken to complete the evaluation (in milliseconds) |

## Worked Examples

### Example 1: DENIED (EditAll on Table)

- **User**: `prajwal.pp44`
- **Resource**: `table`
- **Operation**: `EditAll`
- **Resource FQN**: `sample_data.ecommerce_db.shopify.dim_address_clean`

**Result**: DENIED

| Metric | Value |
|--------|-------|
| Policies Evaluated | 2 |
| Rules Evaluated | 1,048 |
| Matching Rules | 0 |
| Allow Rules | 0 |
| Deny Rules | 0 |
| Evaluation Time | 354ms |

This example demonstrates a default-deny outcome: when zero rules match, access is denied. This aligns with the Deny precedence principle documented in [[authorization-policies]], extended to the case where no rule fires at all.

### Example 2: ALLOWED (ViewAll on Table)

- **User**: `prajwal.pp44`
- **Resource**: `table`
- **Operation**: `ViewAll`
- **Resource FQN**: `sample_data.ecommerce_db.shopify.dim_address_clean`

**Result**: ALLOWED

| Metric | Value |
|--------|-------|
| Policies Evaluated | 2 |
| Rules Evaluated | 1,048 |
| Matching Rules | 1,046 |
| Allow Rules | 0 |
| Deny Rules | 0 |
| Evaluation Time | 363ms |

This example reinforces the [[viewbasic-viewall-operations|ViewAll vs. EditAll]] distinction: the same user on the same resource is allowed `ViewAll` but denied `EditAll`, demonstrating how operation type is a critical factor in the [[hybrid-rbac-abac-model]].

## Relationship to Other Diagnostic Tools

- **[[audit-logs]]**: Provide historical records of actual access events; the debugger simulates hypothetical scenarios.
- **[[authorization-policies]]**: The debugger is the recommended validation tool for policy behavior before or after deployment.
- **[[search-rbac]]**: The debugger evaluates the authorization layer only; it is an open question whether it accounts for search-level RBAC filtering.

## Open Questions

- What is the behavior when a Resource FQN is *not* provided? Does evaluation occur at the type level only?
- Are there resource types or operations that the debugger cannot evaluate?
- How does evaluation time scale with significantly larger or more complex policy sets?
- Does the debugger incorporate [[search-rbac]] filtering, or is it purely authorization-layer?