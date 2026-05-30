---
type: concept
title: How to Add a Team
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, administration, teams, how-to, governance]
related: [teams-and-users, team-types, team-hierarchy-rules, multi-admin-model, public-team]
sources: ["how-to-add-a-team-openmetadata-admin-guide---openm-20260514.md"]
---

# How to Add a Team

The procedure for creating a new team in OpenMetadata, which establishes an organizational unit within the platform's hierarchical structure. This workflow is the practical mechanism through which the [[team-hierarchy-rules]] are enforced and the [[multi-admin-model]] is realized.

## Procedure

1. Navigate to **Settings > Team & User Management > Teams**.
2. Drill down into the relevant parent team — a [[team-types|BusinessUnit, Division, or Department]] — where the new team will reside.
3. Click **Add Team**.
4. Fill in the required details:
   - **Name** — unique identifier for the team.
   - **Display Name** — human-readable label.
   - **Email** — contact email for the team.
   - **Team Type** — select from the available options. The choices are dynamically restricted based on the parent team's type, as defined in the [[team-hierarchy-rules]].
   - **Description** — optional descriptive text.
5. Optionally enable the **Public Team** toggle to allow open access, permitting anyone to join the team, view data, and collaborate without explicit invitation. See [[public-team]].
6. Click **OK** to create the team.

## Critical Constraints

### Group Immutability
Once a team is created with the `Group` type, its **teamType cannot be changed later**. This is an irreversible design decision. Administrators must carefully consider whether a team should be a `Group` before creation.

### Data Asset Ownership
Only teams of type `Group` can own data assets in OpenMetadata. This is the fundamental governance rule that determines which organizational units can be assigned as owners of tables, dashboards, pipelines, and other data assets. If a team needs to own assets, it must be created as a `Group` from the outset.

## Post-Creation

After the team is created, administrators can:
- Add users to the team (see [[teams-and-users]]).
- Create additional sub-teams within it, subject to the parent-child constraints of the [[team-hierarchy-rules]].

## Open Question

Can team types other than `Group` (i.e., `BusinessUnit`, `Division`, `Department`) be changed after creation? The official documentation references a "How to Change the Team Type" page, but the rules for non-Group type mutability are not covered in this source. This remains an open question for further investigation.