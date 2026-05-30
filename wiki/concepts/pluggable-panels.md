---
type: concept
title: Pluggable Panels
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, ui, customization, persona, administration]
related: [persona-and-landing-page-customization, openmetadata-administration, openmetadata-features]
sources: ["customizable-landing-page-with-pluggable-panels----20260514.md"]
---

# Pluggable Panels

Pluggable Panels are the modular UI components that compose the OpenMetadata customizable landing page. Each panel is a discrete widget that can be added, removed, or rearranged by administrators to tailor the homepage experience for different user [[persona-and-landing-page-customization|personas]].

## Current Panel Catalog

The following panels are available for landing page customization:

- **Activity Feed** — Displays recent platform activity, conversations, and notifications.
- **Key Performance Indicators (KPIs)** — Shows data quality, ownership, and description coverage metrics.
- **Recent Announcements** — Surfaces organizational announcements and updates.
- **Tasks** — Lists assigned and pending tasks for the user.
- **Recently Viewed** — Provides quick access to recently visited data assets.

## Configuration Mechanism

Administrators configure panels through the Persona settings:

1. Navigate to **Settings > Persona**.
2. Select a persona to customize.
3. Choose **Customize Homepage**.
4. Click **Add Widget** to select from available panels.
5. Rearrange panels by dragging to the desired layout.
6. Click **Apply** to save the configuration.

## Persona Switching and Default Persona

The pluggable panels system supports dynamic persona switching. When a user changes their active persona, the landing page automatically reconfigures to display the panels assigned to that persona. Users can also set a **Default Persona**, which determines the layout loaded upon login.

## Use Case Examples

- **Data Engineer**: Prioritizes Pipeline Status, data quality metrics, and recent tasks. Announcements and KPIs may be deprioritized.
- **Data Steward**: Focuses on recent data views, KPI dashboards, and governance-related panels. Pipeline Status may be removed.

## Future Enhancements

The OpenMetadata roadmap includes:

- **Entity Pages Customization**: Extending pluggable panels to entity detail pages, allowing role-specific metadata panels (e.g., knowledge articles, glossary terms).
- **Knowledge Panel Expansion**: New panel types such as Data Quality Status, Product Knowledge Articles, and Service Status.

## Relationship to Other Concepts

Pluggable Panels are the technical foundation for [[persona-and-landing-page-customization|Persona and Landing Page Customization]], a key capability within [[openmetadata-administration|OpenMetadata Administration]]. They represent a shift from a static UI to a composable, role-aware dashboard system.