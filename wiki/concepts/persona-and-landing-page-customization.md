---
type: concept
title: Persona and Landing Page Customization
created: 2026-05-14
updated: 2026-05-14
tags: [administration, user-experience, customization, ui, persona, landing-page, ui-customization]
related: ["openmetadata-administration", "teams-and-users", "persona", "pluggable-panels", "role-based-ui-customization", "data-steward-role", "roles-and-policies", "how-to-define-personas-in-openmetadata---openmetad-20260514", "customizable-landing-page-with-pluggable-panels----20260514", "hybrid-rbac-abac-model"]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md", "persona-and-landing-page-customization-in-openmeta-20260514.md"]
---
# Persona and Landing Page Customization

**Persona and Landing Page Customization** is the OpenMetadata feature that enables administrators to tailor the user interface and experience based on user roles, teams, or preferences. It is the primary implementation surface for [[role-based-ui-customization]], ensuring that each user interacts with the platform in a way that aligns with their responsibilities.

## Purpose and Benefits

OpenMetadata’s persona and landing page customization aims to:

- **Relevance** — Show users the data assets, metrics, and dashboards most relevant to their role.
- **Efficiency** — Reduce cognitive load by presenting a focused view of the platform.
- **Adoption** — Improve user satisfaction by providing a personalized entry point.

In achieving these goals, the feature delivers:

- **Persona-Based Personalization** — Users interact with OpenMetadata based on their selected persona, allowing them to switch between different perspectives to access the most relevant data and tools for their needs.
- **Customizable Landing Pages** — Each persona can have a tailored landing page that displays role‑relevant panels.
- **Multi-Persona Flexibility** — Users can switch between multiple personas (e.g., a user can be both a Data Engineer and a Data Steward), and the application adapts the layout and functionality accordingly. This is a key differentiator from simpler role‑based UI systems.

## Hierarchical Structure

The feature follows a clear hierarchical structure:

1. **[[persona|Persona]]** — The selector. A named role profile (e.g., Data Engineer, Data Steward) that determines *which* landing page configuration is active for a user.
2. **Landing Page** — The surface. A customizable entry point composed of discrete, configurable widgets.
3. **[[pluggable-panels|Pluggable Panels]]** — The components. Modular UI widgets (Activity Feed, KPIs, Announcements, Tasks, Recently Viewed) that can be added, removed, or rearranged per persona.

## Customization Scope

Both the landing page (the first page users see after login) and broader persona‑based experiences can be customized. This includes, but is not limited to:

- Default dashboard or view configuration
- Widget placement, visibility, and arrangement
- Role‑specific navigation and featured content
- The selection and ordering of [[pluggable-panels]] such as Activity Feed, KPIs, Announcements, and Recently Viewed

## Distinction from Access Control

Persona and Landing Page Customization operates at the **presentation layer**. It determines *what a user sees*. This is distinct from [[roles-and-policies|Roles and Policies]], which operate at the **authorization layer** and determine *what a user can do*. A user’s effective permissions are governed by the [[hybrid-rbac-abac-model|RBAC-ABAC system]], not by their active persona.

## Design Philosophy

OpenMetadata is designed as a platform for everyone in the organization — not just technical users. Persona and Landing Page Customization embodies this philosophy by ensuring that data engineers, data scientists, [[data-steward-role|data stewards]], and other roles each experience a tailored interface that enhances productivity by surfacing relevant information and tools for their daily activities.

## Administration

This capability is managed by Administrators and is part of the platform’s user experience configuration. It complements the organizational structure defined through [[teams-and-users|Teams and Users]].