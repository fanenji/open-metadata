---
type: source
title: "How to Define Personas in OpenMetadata - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [persona, administration, ui-customization, openmetadata]
related: [persona, persona-and-landing-page-customization, openmetadata-administration, role-based-ui-customization]
sources: ["how-to-define-personas-in-openmetadata---openmetad-20260514.md"]
authors: ["OpenMetadata Documentation Team"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/persona-landing-page-customization/defining-persona"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# How to Define Personas in OpenMetadata - OpenMetadata Documentation

This source is a section of the official OpenMetadata v1.12.x Administration Guide, specifically the "Persona and Landing Page Customization" chapter. It provides the foundational definition of a [[persona|Persona]] and the basic procedural steps for administrators to create and manage Personas within the platform.

## Key Content

### What is a Persona?

In OpenMetadata, a persona represents an organization's specific role or function, such as a data engineer, data steward, or data scientist. Personas define how the user interacts with the platform by tailoring the interface and functionality to their role.

**Examples provided:**
- A **data engineer** might focus on pipelines and data quality.
- A **data steward** is more concerned with governance and glossary management.

### Steps to Define a Persona

1. As an administrator, navigate to **Settings > Personas** in OpenMetadata.
2. Create a new persona or modify an existing one.
3. Associate users with the appropriate persona to customize their experience based on their roles.

## Significance

This document establishes the conceptual foundation for the Persona feature, linking organizational roles to a tailored user experience. It serves as the prerequisite step for [[persona-and-landing-page-customization|landing page customization]], where the specific UI panels and layout are configured per persona. The source is notably sparse, providing a high-level overview without detailing the specific UI elements controllable by a Persona or how Personas interact with [[roles-and-policies|Roles and Policies]] and [[teams-and-users|Teams]].

## Open Questions

- What specific UI elements (e.g., landing page panels, menu items) are controlled by a Persona?
- How do Personas relate to Roles and Policies for access control? Are they complementary or overlapping?
- Can a single user be assigned multiple Personas?