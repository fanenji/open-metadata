---
type: source
title: "How to Change the Team Type | Official Documentation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [teams, administration, team-types, ui-procedure]
related: [team-types, team-hierarchy-rules, how-to-add-a-team, how-to-change-team-type]
sources: ["how-to-change-the-team-type-official-documentation-20260514.md"]
authors: []
year: 2025
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/change-team-type"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# How to Change the Team Type | Official Documentation - OpenMetadata Documentation

Official procedural guide for changing an existing team's type classification through the OpenMetadata UI. The documentation uses a `Digital_Marketing` team as an example, demonstrating the change from `Department` to `Division`.

## Prerequisites

The guide explicitly instructs users to refer to the [[team-types|Team Structure in OpenMetadata]] page to understand the various team types before attempting a change.

## Procedure

1. Navigate to **Settings >> Team & User Management >> Teams** and click on the target team name (e.g., `Digital_Marketing`).
2. On the team details page, locate the **Type** field with its edit icon.
3. Click the edit button to reveal available type options, select the desired type (e.g., `Division`), and click ✅ to save.
4. The team type is updated immediately.

## Notable Omissions

The source does not address:
- Whether `Group` type teams can be changed (contradicting the immutability warning in [[how-to-add-a-team]])
- Impact on child teams when a parent's type is changed
- Validation against [[team-hierarchy-rules]] during type change
- Effects on existing role assignments or data asset ownership