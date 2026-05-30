---
type: concept
title: Public Team
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, teams, collaboration, access-control]
related: [how-to-add-a-team, teams-and-users, team-types]
sources: ["how-to-add-a-team-openmetadata-admin-guide---openm-20260514.md"]
---

# Public Team

A configuration option available during team creation in OpenMetadata that enables open access to the team. When a team is designated as **Public**, anyone can join the team, view its data assets, and collaborate without requiring an explicit invitation from an administrator.

## Purpose

The Public Team option supports open collaboration patterns where broad participation is desired. It contrasts with the default restricted model, where users must be explicitly added to a team by an administrator.

## Configuration

The Public Team toggle is presented during the [[how-to-add-a-team|Add Team]] workflow, alongside other team properties such as Name, Display Name, Email, Team Type, and Description. It can be enabled or disabled at creation time.

## Relationship to Access Control

The Public Team setting governs **membership access** — who can join the team. It is distinct from the permissions and policies defined by [[roles-and-policies]], which control what team members can *do* within the platform. A Public Team may still have restricted permissions on specific data assets based on the policies assigned to it.