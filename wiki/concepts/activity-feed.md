---
type: concept
title: Activity Feed
created: 2026-05-14
updated: 2026-05-14
tags: [collaboration, notifications, ui]
related: [announcements, openmetadata-collaboration, data-observability-alerts]
sources: ["overview-of-announcements-official-documentation---20260514.md"]
---

# Activity Feed

The Activity Feed is a central UI component in [[OpenMetadata]] that displays real-time updates about data assets, including announcements, tasks, conversations, and other events. It serves as the primary notification channel for users following data assets.

## Role in Announcements

When an announcement is created, it appears in the Activity Feed of all users who follow the affected data asset. This ensures that the announcement is visible not only as a banner on the data asset's detail page but also in the user's main feed on the homepage. Users can interact with announcements directly from the Activity Feed by reacting with emojis or replying with threaded comments.

## Integration with Alerts

The Activity Feed can be integrated with the [[data-observability-alerts]] system. When alerts are configured for Activity Feeds, notifications about announcements (and other feed events) are sent to external channels such as Email, Chat, Slack, MS Teams, and Webhooks.