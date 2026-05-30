---
type: entity
title: Persona
created: 2026-05-14
updated: 2026-05-14
tags: ["openmetadata", "persona", "administration", "ui-customization", "user-experience"]
related: ["persona-and-landing-page-customization", "pluggable-panels", "openmetadata-administration", "teams-and-users", "roles-and-policies", "role-based-ui-customization", "data-steward-role"]
sources: ["customizable-landing-page-with-pluggable-panels----20260514.md", "how-to-define-personas-in-openmetadata---openmetad-20260514.md", "persona-and-landing-page-customization-in-openmeta-20260514.md"]
---

# Persona

A **Persona** in OpenMetadata is a named role profile representing an organizational role (e.g., Data Engineer, Data Steward, Data Scientist) that defines a customized user experience. Personas tailor the interface and functionality—primarily the landing page layout and [[pluggable-panels|Pluggable Panels]]—to align with the needs of specific user groups. They are the primary mechanism for [[role-based-ui-customization|role-based UI customization]], allowing administrators to move beyond a one-size-fits-all interface and ensure that each user sees the most relevant information and tools for their daily work.

## Key Features and Characteristics

- **Role-Based Profiles**: Each persona corresponds to a specific role or function, providing a tailored landing page with role-appropriate panels.
- **Landing Page Customization**: Administrators can define a unique homepage layout for each persona by adding, removing, and rearranging [[pluggable-panels|Pluggable Panels]]. Common panels include Activity Feed, KPIs, Announcements, Tasks, and Recently Viewed.
- **Multi-Persona Flexibility**: Users can be assigned multiple personas. They can switch between personas at runtime without logging out, and the UI dynamically reconfigures to reflect the selected persona's settings. A **default persona** can be set to load automatically upon login. Supporting multiple personas per user is a key differentiator from simpler role-based systems.
- **Administrator-Defined**: Personas are created and managed by administrators through the OpenMetadata UI (under **Settings > Personas**).
- **Presentation Layer Focus**: Personas govern *what a user sees* (UI customization), while [[roles-and-policies|Roles and Policies]] govern *what a user can do* (access control). This separation keeps the UX and permission layers distinct.

## Relationship to Landing Pages and Pluggable Panels

The persona is the driver for [[persona-and-landing-page-customization|landing page customization]]. The relationship follows a hierarchy: **Persona → Landing Page → Pluggable Panels**. A persona selects which landing page configuration is active; that landing page is composed of discrete, configurable pluggable panels. This modular design enables precise tailoring of the information architecture for each role.

## Use Cases

- **Data Engineer Persona**: Configured with Pipeline Status, [[data-lineage|data lineage]], [[data-quality|data quality]] metrics, and task panels. Announcements and KPIs may be deprioritized.
- **Data Steward Persona**: Prioritizes KPI dashboards, recently viewed assets, governance-related panels, [[glossary-tags|glossary terms]], and data classification tasks. Pipeline Status may be removed.
- **Data Scientist Persona**: Emphasizes data discovery and profiling, with quick access to [[data-profiling|data profiling]] results and dataset search.

## Configuration and Management

Personas are managed under **Settings > Personas** in the OpenMetadata UI. Administrators can:

1. Navigate to **Settings > Personas**.
2. Create a new persona or modify an existing one.
3. Associate users with one or more personas to customize their experience based on their roles.
4. Customize the landing page for each persona by adding, removing, and rearranging [[pluggable-panels|Pluggable Panels]].
5. Save and apply configurations.

Once configured, the persona features (landing page customization, switching, default persona) become available to users.

## Relationship to Other Mechanisms

Personas complement the [[teams-and-users|Teams and Users]] hierarchy. While Teams define organizational structure and access policies, Personas define the user experience layer. A user can belong to a Team and be assigned one or more Personas, enabling streamlined UX assignment without impacting team-based permissions.

Personas are also distinct from [[roles-and-policies|Roles and Policies]]. Roles and policies determine *what a user can do* (access controls and permissions), while Personas determine *what a user sees* (interface and layout). Both mechanisms can be used together to provide a comprehensive, role-appropriate experience.

## Design Philosophy

OpenMetadata is designed as a platform for everyone in the organization. Personas embody this philosophy by ensuring that each user—regardless of technical background—experiences the platform in a way that aligns with their responsibilities, enhancing productivity by providing relevant information and tools tailored to their daily activities.

## Future Direction

OpenMetadata plans to extend persona-based customization to entity detail pages, allowing role-specific metadata panels such as knowledge articles and glossary terms.

## Open Questions

- What is the full set of UI elements that a Persona can control, beyond the landing page?
- When a user is assigned multiple personas, how are conflicting UI configurations (e.g., different landing page layouts) resolved? Is there a default priority or merge behavior?
- How does multi-persona switching interact with the [[hybrid-rbac-abac-model|RBAC-ABAC authorization model]]? Does switching personas affect permissions, or is the change purely a UI customization layer?
- How do Persona assignments interact with Team memberships? Can personas be inherited through team hierarchies, or are they directly assigned to individual users?