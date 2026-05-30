---
type: concept
title: Roles and Policies
created: 2026-05-14
updated: 2026-05-14
tags: [administration, access-control, roles, policies, security]
related: [openmetadata-administration, teams-and-users, permission-debugger]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md"]
---
# Roles and Policies

Roles and Policies are the core access control mechanisms in OpenMetadata. They allow Administrators to define and enforce permissions across the organization, governing who can access which data assets and what operations they can perform.

## Overview

- **Roles** — Named collections of permissions that can be assigned to users or teams.
- **Policies** — Rules that define what actions are allowed or denied on specific resources.

Together, Roles and Policies form a flexible, fine-grained authorization system that supports the principle of least privilege.

## Relationship to Teams

Roles and Policies integrate with the [[teams-and-users|Teams and Users]] organizational structure. Policies can be assigned at the team level, allowing administrators to manage access for groups of users rather than individuals. This hierarchical approach streamlines onboarding and ensures consistent access control as team membership changes.

## Advanced Guide

OpenMetadata provides an advanced guide for Roles and Policies, intended for administrators who need to implement complex access management scenarios beyond basic setup. This includes:

- Custom role definitions
- Policy composition and inheritance
- Resource-level permissions
- Integration with team hierarchies

## Diagnostic Tooling

When access issues arise, administrators can use the [[permission-debugger|Permission Debugger]] to diagnose and troubleshoot permission problems, identifying which role or policy is granting or denying access to a specific resource.

## Open Questions

- What is the exact interaction model between Teams and Roles/Policies? Are policies assigned to teams, to individual users within teams, or both?
- How do inherited permissions propagate through the team hierarchy?