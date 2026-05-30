---
type: concept
title: Data Collaboration
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, collaboration, conversations, tasks, announcements]
related: [openmetadata-collaboration, conversation-threads, tasks, announcements, activity-feed, tag-request-workflow, glossary-terms]
sources: ["data-collaboration-openmetadata-collaboration-feat-20260514.md"]
---

# Data Collaboration

Data Collaboration in OpenMetadata refers to the set of built-in features that enable teams to communicate, coordinate, and share knowledge directly within the platform. It transforms metadata from a static catalog into a dynamic, social environment where users can discuss data assets, request changes, and announce upcoming events.

## Three Pillars

OpenMetadata's data collaboration is built on three core features:

1. **[[conversation-threads|Conversation Threads]]** — Threaded discussions initiated from data assets or tags, supporting @mentions, replies, and reactions. Enables contextual collaboration directly within the platform.
2. **[[tasks|Tasks]]** — Structured, assignable requests (e.g., "Request for Description," "Request for Tags," glossary term approval) that create a formal workflow around metadata changes.
3. **[[announcements|Announcements]]** — Scheduled, time-bound notifications about upcoming events (deprecation, deletion, schema changes) displayed as banners and in the Activity Feed.

All three features surface in the [[activity-feed|Activity Feed]], which serves as the central UI component for collaboration.

## Purpose

The primary goal of data collaboration is to break information silos and enhance data understanding across the organization. By enabling conversations, structured requests, and announcements directly on data assets, OpenMetadata encourages knowledge sharing and reduces the friction of coordinating metadata changes through external tools.

## Relationship to Other Concepts

- [[openmetadata-collaboration]] — The umbrella wiki page that covers all collaboration features.
- [[tag-request-workflow]] — A specific task type for requesting classification tag changes.
- [[glossary-terms]] — Glossary term approval workflows are initiated through Tasks.
- [[activity-feed]] — The central UI component where all collaboration activity is displayed.