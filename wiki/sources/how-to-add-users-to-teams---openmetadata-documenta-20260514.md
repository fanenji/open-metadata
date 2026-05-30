---
type: source
title: "How to Add Users to Teams - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, teams, users, administration, how-to]
related: [teams-and-users, how-to-add-a-team, roles-and-policies, team-hierarchy-rules, multi-team-membership]
sources: ["how-to-add-users-to-teams---openmetadata-documenta-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/add-users"
venue: "OpenMetadata Documentation v1.12.x"
---

# How to Add Users to Teams - OpenMetadata Documentation

Official procedural documentation for adding users to teams in OpenMetadata v1.12.x. Covers two distinct workflows: adding users to teams during the initial invitation process, and adding existing users to teams via the Settings UI. Documents the capability for multi-team membership during user creation and the inheritance of Roles from team membership.

## Key Points

- Users can be added to teams either during initial invitation or after the user already exists in OpenMetadata.
- During new user creation, a user can be added to multiple Teams simultaneously.
- For existing users, navigate to **Settings >> Team & User Management >> Teams >> Users Tab**, select the specific team (and sub-team if applicable), click **Add User**, search for the user, select the checkbox, and click **Update**.
- Users inherit the Roles that apply to the Teams they belong to.
- Team hierarchy must be navigated to the correct sub-team level before adding members.