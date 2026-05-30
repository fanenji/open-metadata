---
type: concept
title: OpenMetadata Collaboration
created: 2026-05-14
updated: 2026-05-15
tags: [openmetadata, collaboration, communication, teamwork, activity-feeds, announcements, tasks]
related: [openmetadata, openmetadata-features, following-data-assets, change-events-system, data-asset-ownership, teams-and-users, conversations-around-classification, tag-request-workflow]
sources: ["OMD - Getting Started.md", "how-to-follow-a-data-asset-official-documentation--20260514.md"]
---

# OpenMetadata Collaboration

OpenMetadata includes native collaboration features designed to enable effective teamwork among diverse data practitioners, including data platform engineers, governance professionals, data scientists, analysts, and business users. These features allow users to discuss data assets, request changes, and stay informed about updates without leaving the metadata interface, eliminating the need to switch between multiple tools for communication and coordination.

## Purpose

These collaboration features aim to eliminate the need for teams to switch between multiple tools, keeping all context within the OpenMetadata platform.

## Core Collaboration Features

### Activity Feeds

The Activity Feeds tab is the central hub for collaboration. It displays all activities related to data assets that a user owns, follows, or is @mentioned in. This unified feed consolidates updates from three sources:

1. **Owned assets** — Automatic updates for assets the user owns.
2. **Followed assets** — Updates for assets the user has explicitly followed (see [[following-data-assets]]).
3. **@mentions** — Updates where the user is directly mentioned.

This feed allows users to track recent changes and activities on data assets.

### Following Data Assets

Users can subscribe to updates on data assets they do not own by using the Follow button. This lightweight subscription mechanism is distinct from ownership — owners receive all updates by default. Followed assets appear in the My Data page's "Following" section and the Profile Page's "Following" tab. See [[following-data-assets]] for details.

### Announcements

Users can create announcements to broadcast important updates about data assets to the organization.

### Tasks

The task system enables structured collaboration workflows, such as requesting descriptions, tags, or glossary terms on data assets. Users can assign and track work items related to data assets.

### Team Conversations

Users can discuss data assets directly within the platform through team conversations, enabling real-time discussion and collaboration.

### Conversations Around Classification

Threaded discussions can be initiated from individual tags on data assets. These conversations support @mentions, #mentions, replies, reactions, editing, and deletion. See [[conversations-around-classification]].

### Tag Request Workflow

Users can request tag changes and discuss them within the platform via Tasks. The workflow supports review-based classification with a three-tab interface (Current, New, Difference) and Accept/Edit Accept resolution. See [[tag-request-workflow]].

### Slack/Teams Integration

Receive notifications and communicate via external messaging platforms such as Slack and Microsoft Teams.

### Team Dashboards

Monitor team progress and performance.

## Relationship to Other Concepts

- [[change-events-system]] — The underlying event capture mechanism that powers activity feeds and notifications.
- [[data-asset-ownership]] — Ownership grants automatic update notifications; following is for non-owners.
- [[teams-and-users]] — Collaboration is user-centric, though team membership influences visibility and permissions.
- [[following-data-assets]] — Details on the follow feature.
- [[conversations-around-classification]] — Details on tag-based conversations.
- [[tag-request-workflow]] — Details on the tag request workflow.