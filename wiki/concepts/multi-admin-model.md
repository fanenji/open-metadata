---
type: concept
title: Multi-Admin Model
created: 2026-05-14
updated: 2026-05-14
tags: [administration, governance, openmetadata, decentralized-management]
related: [teams-and-users, roles-and-policies, openmetadata-administration, team-types]
sources: ["manage-teams-and-users---openmetadata-documentatio-20260514.md"]
---
# Multi-Admin Model

The multi-Admin model is a design feature of OpenMetadata that allows an organization to have multiple Administrators, each managing separate teams and departments independently. This enables decentralized governance and scalable administration across large or distributed organizations.

## How It Works

Rather than relying on a single super-admin, OpenMetadata supports multiple Admin accounts. Each Admin can be assigned responsibility for specific teams or organizational units. This allows different departments — such as Engineering, Marketing, and Finance — to be managed by their respective Admins without interference.

## Benefits

- **Decentralized Governance**: Distributes administrative responsibilities across the organization.
- **Scalability**: Supports large organizations with many teams and users.
- **Autonomy**: Departments can manage their own users, team structures, and policies within their scope.
- **Alignment with Organizational Structure**: Mirrors real-world reporting lines and management hierarchies.

## Relationship to Teams and Users

The multi-Admin model works in conjunction with the hierarchical [[teams-and-users|team structure]]. Admins are typically assigned to manage specific branches of the team hierarchy. This ensures that administrative authority is scoped appropriately and aligns with organizational boundaries.

## Relationship to Roles and Policies

While the multi-Admin model governs *who can manage* teams and users, [[roles-and-policies|Roles and Policies]] govern *what users can do* within the platform. Admins use the policy framework to define and enforce access controls for the teams under their management.

## Considerations

- The exact scope of an Admin's authority (e.g., whether they can manage other Admins or system-wide settings) should be verified against the official documentation.
- Best practices for implementing a multi-Admin model include clearly defining team boundaries and ensuring that Admin assignments follow the principle of least privilege.