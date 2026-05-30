---
type: source
title: "How to Add a Team | OpenMetadata Admin Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, administration, teams, how-to]
related: [teams-and-users, team-types, team-hierarchy-rules, multi-admin-model]
sources: ["how-to-add-a-team-openmetadata-admin-guide---openm-20260514.md"]
authors: ["OpenMetadata Documentation"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/add-team"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# How to Add a Team | OpenMetadata Admin Guide

Official step-by-step guide for creating a new team within the OpenMetadata organizational hierarchy. This procedure covers navigating to the appropriate parent team (BusinessUnit, Division, or Department), configuring team properties including the critical teamType selection, enabling the Public Team option for open collaboration, and understanding the irreversible implications of choosing the Group team type.

Key points:
- Teams are created within an existing parent team via **Settings > Team & User Management > Teams**.
- The available teamType choices are dynamically restricted based on the parent team's type, enforcing the [[team-hierarchy-rules]].
- The **Public Team** option allows anyone to join, view data, and collaborate without explicit invitation.
- **Group immutability**: Once a team is created with the `Group` type, its teamType cannot be changed later.
- **Data asset ownership**: Only teams of type `Group` can own data assets in OpenMetadata.

This source directly extends the conceptual pages [[team-types]] and [[team-hierarchy-rules]] with the practical UI workflow, and serves as a procedural child of [[teams-and-users]].