---
type: concept
title: Permission Debugger
created: 2026-05-14
updated: 2026-05-14
tags: [administration, access-control, troubleshooting, diagnostics]
related: [openmetadata-administration, roles-and-policies, teams-and-users]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md"]
---
# Permission Debugger

The Permission Debugger is a diagnostic tool for troubleshooting access permission issues in OpenMetadata. It helps administrators understand why a user or team can or cannot access a specific resource.

## Purpose

When users report that they cannot view, edit, or perform operations on data assets they believe they should have access to, the Permission Debugger allows administrators to:

- Trace the effective permissions for a given user or team
- Identify which [[roles-and-policies|Roles and Policies]] are granting or denying access
- Diagnose conflicts between multiple policies
- Verify that team hierarchy inheritance is working as expected

## Usage Context

The Permission Debugger is listed as an administrative capability, indicating it is available to users with the Administrator role. It is most valuable in environments with complex access control configurations involving multiple roles, policies, and hierarchical [[teams-and-users|Teams]].

## Open Questions

- Does the debugger provide a visual policy evaluation trace, or is it a text-based log?
- Can it simulate permissions for hypothetical role assignments before applying changes?