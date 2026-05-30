---
type: concept
title: Role-Based UI Customization
created: 2026-05-14
updated: 2026-05-14
tags: ["ui-customization", "persona", "user-experience", "openmetadata", "administration", "landing-page"]
related: ["persona", "persona-and-landing-page-customization", "pluggable-panels", "roles-and-policies", "teams-and-users", "hybrid-rbac-abac-model"]
sources: ["how-to-define-personas-in-openmetadata---openmetad-20260514.md", "customizable-landing-page-with-pluggable-panels----20260514.md", "persona-and-landing-page-customization-in-openmeta-20260514.md"]
---

# Role-Based UI Customization

**Role-Based UI Customization** is the mechanism in OpenMetadata that tailors the platform's user interface and functionality based on the user's assigned organizational role. It is implemented through [[persona|Personas]] and [[persona-and-landing-page-customization|Landing Page Customization]], which leverages [[pluggable-panels|pluggable panels]] to compose the landing page.

## How It Works

Rather than presenting every user with an identical interface, OpenMetadata allows administrators to define distinct [[persona|Personas]] — named profiles corresponding to organizational roles such as Data Engineer, Data Steward, or Data Scientist. Each Persona specifies:

- Which [[pluggable-panels|pluggable panels]] appear on the landing page (e.g., Activity Feed, KPIs, Announcements, Tasks, Recently Viewed).
- The layout and arrangement of those panels.
- Potentially, which menu items and navigation options are emphasized or surfaced.

When a user logs in, the platform applies the UI configuration associated with their assigned Persona, creating a role-appropriate experience.

## Multi-Persona Flexibility

A key differentiator of OpenMetadata's approach is that users are not limited to a single Persona. A user who functions as both a Data Engineer and a Data Steward can hold and switch between these perspectives at runtime. The application dynamically adapts the landing page layout and visible panels to match the active Persona, enabling efficient context-switching for users with cross-functional responsibilities.

## Distinction from Access Control

Role-Based UI Customization operates at the **presentation layer** — it determines *what a user sees*. This is distinct from [[roles-and-policies|Roles and Policies]], which operate at the **authorization layer** and determine *what a user can do* via the [[hybrid-rbac-abac-model|RBAC-ABAC authorization model]]. The two mechanisms are complementary but independent: a user's effective permissions are governed by policies, not by their active Persona.

| Aspect | Role-Based UI Customization | Access Control |
|--------|----------------------------|----------------|
| **Mechanism** | [[persona|Personas]] | [[roles-and-policies|Roles and Policies]] |
| **Governs** | What the user *sees* | What the user *can do* |
| **Scope** | Landing page layout, panel visibility, UI emphasis | Permissions to read, create, edit, delete metadata entities |

For example, a Data Steward might have a Persona emphasizing governance panels while Role-Based Policies grant them permission to manage glossary terms.

## Benefits

- **Reduced cognitive load**: Users see only the tools and information relevant to their role.
- **Improved productivity**: Frequently used features are surfaced prominently.
- **Consistent experience**: All users in the same role share a standardized interface.
- **Flexibility**: Users can switch between assigned Personas at runtime if they hold multiple roles.

## Design Philosophy

This feature reflects OpenMetadata's design as a platform for everyone in the organization. By tailoring the interface to each role's responsibilities, it enhances productivity by providing relevant information and tools without overwhelming users with irrelevant functionality.

## Future Directions

The official documentation indicates that future enhancements will extend Persona-based customization beyond the landing page to entity detail pages, and introduce additional panel types such as Data Quality Status and Knowledge Articles.