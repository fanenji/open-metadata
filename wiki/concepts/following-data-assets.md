---
type: concept
title: Following Data Assets
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, collaboration, data-assets, activity-feeds]
related: [openmetadata-collaboration, change-events-system, data-asset-ownership, teams-and-users, explore-page, my-data-page, profile-page]
sources: ["how-to-follow-a-data-asset-official-documentation--20260514.md"]
---

# Following Data Assets

Following a data asset is a lightweight subscription mechanism in OpenMetadata that allows users to opt-in to receive activity updates, announcements, and feed notifications for assets they do not own. It is a collaboration feature distinct from ownership, designed to keep users informed about changes to data assets of interest.

## Purpose

The follow feature addresses the need for users to stay updated on data assets they care about but do not own. While owners automatically receive all updates by default, non-owners must explicitly follow an asset to receive notifications. This creates a clear separation between ownership responsibilities and passive awareness.

## Workflow

The procedure for following a data asset is straightforward:

1. Navigate to the **Explore** page.
2. Select the relevant type of data asset: Tables, Topics, Dashboards, Pipelines, ML Models, or Containers.
3. Select a specific data asset from the list.
4. Click the **Follow** button to start following it.

## Viewing Followed Assets

Followed assets are displayed in two locations:

- **My Data Page > Following Section** — A dedicated section listing all assets the user is following.
- **Profile Page > Following Tab** — An aggregated view accessible via the "View All" link from the My Data page.

## Relationship to Activity Feeds

The **Activity Feeds** tab consolidates updates from three sources:

1. **Owned assets** — Updates for assets the user owns (automatic).
2. **Followed assets** — Updates for assets the user has explicitly followed.
3. **@mentions** — Updates where the user is mentioned.

This unified model ensures users see all relevant activity in a single feed.

## Key Distinctions

- Following is **per-user**, not team-based. Each user manages their own follow list.
- Following is **optional** for owners; they already receive all updates.
- Following is a **read-only subscription** — it does not grant any additional permissions or ownership rights.
- The feature is distinct from task-based collaboration (e.g., requesting tags or descriptions) and from ownership-based governance.

## Open Questions

- Is there a limit to how many assets a user can follow?
- Can users unfollow assets, and is there a UI mechanism for that?
- Does following affect search results or RBAC evaluation?
- Are follow notifications configurable (e.g., digest vs. real-time)?