---
type: concept
title: Data User Perspective
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-users, user-guide, governance, collaboration]
related: [data-consumer-role, classification-tags, glossary-tags, custom-properties, data-asset-versioning, soft-deletion, tag-request-workflow, persona-and-landing-page-customization, data-observability-alerts, data-insights-application-troubleshooting, guide-for-data-users-openmetadata-user-guide---ope-20260514]
sources: ["guide-for-data-users-openmetadata-user-guide---ope-20260514.md"]
---

# Data User Perspective

The Data User Perspective is a conceptual lens for understanding OpenMetadata's features from the viewpoint of a non-administrative data consumer. Unlike the Admin or Steward roles, which focus on configuration, governance, and system management, the Data User perspective emphasizes discovery, collaboration, and day-to-day interaction with data assets.

## Key Characteristics

- **Discovery-Focused:** Data users primarily browse, search, and explore data assets (tables, topics, dashboards, pipelines) to find relevant information.
- **Collaboration-Oriented:** Features like requesting descriptions, tags, and glossary terms via Tasks enable users to contribute to metadata enrichment without administrative privileges.
- **Consumption-Driven:** The landing page widgets (Activity Feeds, Data Insights, Announcements) are designed to keep data users informed about changes, quality issues, and important updates.
- **Self-Service:** Users can follow data assets, create personal access tokens for API access, and customize their landing page experience through Personas.

## Workflows

The Data User Perspective encompasses several key workflows:

1. **Discovery:** Navigating the "My Data" page, searching for assets, and exploring the data catalog.
2. **Documentation:** Adding descriptions using Markdown, requesting descriptions from owners.
3. **Classification:** Adding tags (including auto-PII classification), requesting tags, and adding glossary terms.
4. **Ownership:** Assigning or changing data ownership, following data assets.
5. **Collaboration:** Creating and viewing announcements, participating in conversations around data assets.
6. **Versioning:** Reviewing version history of data assets to track changes.
7. **Deletion:** Soft or hard deleting data assets as needed.

## Relationship to Other Concepts

- The [[data-consumer-role]] defines the permissions for this perspective, but the Data User Perspective is broader — it includes workflows, collaboration patterns, and UI customization.
- [[persona-and-landing-page-customization]] enables tailoring the interface to different data user types (e.g., Data Analyst, Data Scientist).
- [[classification-tags]] and [[glossary-tags]] are the primary metadata tools used by data users for governance.
- [[tag-request-workflow]] and [[data-asset-versioning]] support collaborative governance without blocking productivity.

## Importance

Understanding the Data User Perspective is critical for designing effective onboarding, training, and documentation for non-admin users. It ensures that the platform's features are presented in a way that matches how data consumers actually work — discovering, understanding, and collaborating on data assets.