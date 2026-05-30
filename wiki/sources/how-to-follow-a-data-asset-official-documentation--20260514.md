---
type: source
title: How to Follow a Data Asset | Official Documentation - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-assets, collaboration, activity-feeds]
related: [following-data-assets, openmetadata-collaboration, change-events-system, data-asset-ownership]
sources: ["how-to-follow-a-data-asset-official-documentation--20260514.md"]
---

# How to Follow a Data Asset | Official Documentation

**Source:** https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/follow-data-asset

**Clipped:** 2026-05-14

## Summary

This official documentation page describes the "Follow" feature in OpenMetadata v1.12.x. It explains that users can subscribe to activity updates, announcements, and feed notifications for data assets they do not own by clicking the Follow button. Owners receive all updates by default without needing to follow. The page provides a step-by-step UI workflow: navigate to the Explore page, select the asset type (Tables, Topics, Dashboards, Pipelines, ML Models, Containers), select a specific asset, and click Follow. Followed assets appear in the "Following" section of the My Data page, with a "View All" link redirecting to the Profile Page > Following Tab. The Activity Feeds tab aggregates updates from owned assets, followed assets, and @mentions.

## Key Points

- Following is a subscription mechanism for non-owners to receive updates on data assets.
- Owners automatically receive all updates without needing to follow.
- The follow action is performed via the Explore page on any supported data asset type.
- Followed assets are displayed in the My Data page's "Following" section and the Profile Page's "Following" tab.
- Activity Feeds consolidate updates from three sources: owned assets, followed assets, and @mentions.
- The feature is a lightweight collaboration pattern distinct from ownership and task-based workflows.

## Connections

- [[following-data-assets]] — Dedicated concept page for the follow feature.
- [[openmetadata-collaboration]] — The follow feature is a concrete collaboration mechanism.
- [[change-events-system]] — Following leverages the underlying event system for notifications.
- [[data-asset-ownership]] — Ownership and following are complementary; owners get automatic updates.
- [[teams-and-users]] — Following is per-user, not team-based.