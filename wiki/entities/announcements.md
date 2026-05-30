---
type: entity
title: Announcements
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-collaboration, notifications]
related: [activity-feed, data-observability-alerts, openmetadata-collaboration, data-asset]
sources: ["overview-of-announcements-official-documentation---20260514-2.md"]
---
# Announcements

Announcements are a feature in [[OpenMetadata]] that enables scheduled, time-bound notifications about upcoming changes to data assets. They address the challenge of informing data teams about changes such as deprecation, deletion, or schema modifications in a timely manner.

## Display and Interaction

- Announcements appear as a **banner** on the data asset details page.
- They are also displayed on the **top right of the landing page**.
- Clicking an announcement reveals further details: Creator, Data Asset (type and name), and Scheduled Date (a date range with start and end dates).
- Users can **react with emojis** and **reply** to announcements from both the Activity Feed on the homepage and from the data asset page.

## Best Practices

- Schedule announcements **well in advance** of the actual change to give the team reasonable time to prepare.
- Ensure all **backward incompatible changes** (e.g., deleting a column from a table) are announced well in advance.

## Integration with Alerts

If [[data-observability-alerts|Alerts]] have been configured for Activity Feeds, the concerned data owners and followers will be notified via external channels such as Email, Chat, Slack, MS Teams, and Webhooks.

## Related Features

- [[activity-feed]] — Central UI component where announcements appear alongside other updates.
- [[openmetadata-collaboration]] — Announcements are a key collaboration feature.
- [[data-observability-alerts]] — External notification mechanism that can be configured to send announcement notifications.