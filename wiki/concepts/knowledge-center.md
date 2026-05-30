---
type: concept
title: Knowledge Center
created: 2026-05-14
updated: 2026-05-14
tags: [saas, documentation, collate-cloud, articles]
related: [collate-inc, openmetadata-collaboration]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Knowledge Center

Knowledge Center is a SaaS-only feature available in [[collate-inc|Collate Cloud]] introduced in [[OpenMetadata]] 1.2.0. It provides a full-page article creation and documentation system within the platform, enabling organizations to document data best practices, onboarding guides, and architectural overviews alongside their data assets.

## Features

- **Full-page articles**: Create rich, long-form documentation pages with architecture diagrams, images, and formatted text.
- **Enhanced markdown editor**: Slash-command formatting, team mentions, and entity references (linking to tables, dashboards, pipelines, etc.).
- **Quick links**: Predefined shortcuts to frequently referenced resources or diagrams.
- **Collaboration features**: Upvote/downvote, version history, bookmarks, shareable links, and comment threads on articles.
- **Discovery**: Articles appear in a dedicated Knowledge Center menu item, separate from asset-level documentation.

## Use Cases

- **Onboarding guides**: "Day One at Company" articles explaining data infrastructure and best practices.
- **Naming conventions**: Documenting standards for creating and naming data assets.
- **Architecture documentation**: Explaining how data flows through the organization's systems.
- **Best practices**: Guidelines for data usage, transformation patterns, and governance policies.

## Why Not Confluence or Google Docs?

Traditional approaches use separate tools (Confluence, Google Docs) for organizational documentation, forcing users to switch contexts. Knowledge Center brings this documentation into OpenMetadata, so data users can discover both data assets and the knowledge about how to use them in one place.

## Availability

Knowledge Center is **exclusively available in Collate Cloud**. It is not part of the open-source OpenMetadata distribution.