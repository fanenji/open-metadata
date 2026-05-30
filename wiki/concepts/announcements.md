---
type: concept
title: Announcements
created: 2026-05-14
updated: 2026-05-14
tags: [announcements, collaboration, notifications, data-assets]
related: [openmetadata-collaboration, data-observability-alerts, activity-feed, data-asset-ownership, openmetadata-features]
sources: ["overview-of-announcements-official-documentation---20260514.md"]
---

# Announcements

Announcements are a collaboration feature in [[OpenMetadata]] that enable data teams to communicate upcoming changes to data assets in a scheduled, visible manner. They address the common organizational challenge of late or missed communication about data changes such as deprecation, deletion, or schema modifications.

## Purpose

The primary goal of announcements is to ensure that all team members are informed about planned changes to data assets well in advance. This is especially critical for backward-incompatible changes, such as deleting a column from a table, where downstream consumers need time to adapt their workflows.

## Mechanics

- **Scheduling:** Each announcement has a start date and an end date that define the window during which it is displayed.
- **Display:** Announcements appear as a prominent banner on the data asset's detail page and are also shown in the Activity Feed on the homepage.
- **Creator:** The user who creates the announcement is identified as the creator.
- **Data Asset:** The announcement is associated with a specific data asset (e.g., Table, Pipeline), and the asset type and name are displayed.
- **Interactions:** Users can react to announcements with emojis and reply with threaded comments from both the Activity Feed and the data asset page.

## Relationship to Alerts

While announcements are displayed within the OpenMetadata UI, they can be integrated with the [[data-observability-alerts]] system. If alerts are configured for Activity Feeds, then data owners and followers of the affected data asset receive notifications via Email, Chat, Slack, MS Teams, or Webhooks.

## Best Practices

- Schedule announcements well in advance of the actual change to give the team adequate time to prepare.
- Use announcements for all backward-incompatible changes to minimize disruption.
- Combine announcements with the existing alerting system to reach users who may not be actively monitoring the Activity Feed.

## Open Questions

- The exact relationship between announcements and the existing Tasks and Conversations features is not fully clarified. It is unclear whether announcements are a distinct entity type or a subtype of activity feed items.
- The permission model for creating announcements is not documented — it is unknown whether only data owners or admins can create them, or if any user can.
- Whether announcements can be edited or deleted after creation is not specified.
- The interaction between announcements and the data asset versioning system is undocumented.