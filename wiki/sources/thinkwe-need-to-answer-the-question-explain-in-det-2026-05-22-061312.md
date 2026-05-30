---
type: source
title: "Managing Users and Roles in OpenMetadata: A Synthesis"
created: 2026-05-22
updated: 2026-05-22
tags: [openmetadata, administration, roles, policies, teams, synthesis]
related: [openmetadata-administration, roles-and-policies, teams-and-users, hybrid-rbac-abac-model, policy-use-cases, data-asset-ownership, permission-debugger, team-types, team-hierarchy-rules, authorization-rules, authorization-policies, spel-conditions, tag-based-access-control, default-organization-policy, data-steward-role, serviceowner-role, multi-admin-model, viewbasic-viewall-operations]
sources: ["thinkwe-need-to-answer-the-question-explain-in-det-2026-05-22-061312.md"]
---
# Managing Users and Roles in OpenMetadata: A Synthesis

This source synthesizes official OpenMetadata documentation into a consolidated guide for managing users and roles. It presents a two-pronged approach: organizing users into a hierarchical team structure and controlling access via the Roles & Policies framework. The document provides a recommended 5-step administration workflow and consolidates four official policy design patterns.

## Key Contributions

- **Recommended Workflow**: A sequential 5-step process: 1) Establish hierarchy, 2) Invite users, 3) Assign baseline access, 4) Layer restrictive policies, 5) Verify with Permission Debugger.
- **Design Principle**: Start with the default Organization Policy, add Allow rules for specific capabilities, and use Deny rules for restrictions.
- **Policy Design Patterns**: Consolidates ServiceOwner delegation, Data Steward governance, Team-Owned Data Protection, and Tag-Based Access Control into a single practical guide.
- **Integration of Teams and Roles**: Explicitly describes how users inherit roles from teams and can also have directly assigned roles.

## References

This source cites and synthesizes multiple existing wiki pages and official documentation sources, including the Advanced Guide for Roles and Policies, Manage Teams and Users documentation, and the Building Blocks of Authorization.