---
type: concept
title: My Data Page
created: 2026-05-14
updated: 2026-05-14
tags: ["openmetadata", "user-interface", "navigation", "landing-page", "widgets"]
related: ["persona-and-landing-page-customization", "pluggable-panels", "data-user-perspective", "guide-for-data-users-openmetadata-user-guide---ope-20260514", "activity-feed-widget", "my-data-widget", "kpi-widget", "total-data-assets-widget", "openmetadata-collaboration"]
sources: ["guide-for-data-users-openmetadata-user-guide---ope-20260514.md", "understanding-the-basics-of-openmetadata---openmet-20260514.md"]
---

# My Data Page

The **My Data Page** is the default landing page in OpenMetadata that users see after logging in. It provides a widget-rich, single-pane view of all data assets, collaboration updates, data insights, and more. The page is composed of several configurable widgets that together form the primary user entry point for data discovery, collaboration, and governance monitoring.

## Widgets

The My Data Page includes the following widgets:

- **[[activity-feed-widget]]** — The main section widget displaying all activities related to owned, followed, or mentioned data assets, plus @mentions and open tasks.
- **[[my-data-widget]]** — Lists all data assets owned by the current user; directs users to the Explore page to claim unowned assets.
- **[[kpi-widget]]** — Shows ownership, description, and tiering coverage metrics; accessible to Admins by default.
- **[[total-data-assets-widget]]** — 14-day trend visualization of total data assets by type (Tables, Dashboards, Databases, etc.).
- **Right-Side Panel** — Contains Announcements, Following, and Recent Views.

## Relationship to Persona Customization

The My Data Page is the concrete implementation of the [[persona-and-landing-page-customization]] concept. The widgets described here are examples of [[pluggable-panels]] that can be configured per [[persona]] to tailor the user experience.

## See Also

- [[persona-and-landing-page-customization]]
- [[pluggable-panels]]
- [[openmetadata-collaboration]]