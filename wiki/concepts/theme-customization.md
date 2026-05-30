---
type: concept
title: Theme Customization
created: 2026-05-14
updated: 2026-05-14
tags: [theme, customization, branding, ui, administration]
related: [persona-and-landing-page-customization, openmetadata-administration, role-based-ui-customization]
sources: ["how-to-customize-openmetadata---openmetadata-docum-20260514.md"]
---

# Theme Customization

Theme customization is a feature in OpenMetadata that allows administrators to personalize the platform's global appearance with company branding and custom colors. It is accessed via **Settings > Preferences > Theme**.

## Customizable Elements

- **Company Logo** — Upload a custom logo image for the platform header.
- **Monogram** — Upload a monogram image for use in place of the logo in compact views.
- **Favicon** — Upload a custom favicon for browser tabs.
- **Primary Color** — A custom color that dynamically adjusts the appearance of buttons, navigation panes, data assets, tab headers, and other UI components.
- **Info Color** — A secondary custom color that is reflected on selected data assets.

## Dynamic UI Adjustment

Changing the primary color automatically updates the styling of multiple UI components across the platform, providing a cohesive branded experience without manual per-component configuration.

## Revert to Original Theme

A one-click option is available to reset all theme customizations back to the default OpenMetadata theme.

## Relationship to Persona Customization

Theme customization is **global** — it affects the appearance for all users of the platform. This is distinct from [[persona-and-landing-page-customization]], which is **per-user** and controls the layout, panels, and content visible on the landing page. The two systems are complementary: theme sets the overall look and feel, while persona tailors the user experience for different roles.

## Administration Context

Theme customization is part of the broader [[openmetadata-administration]] capabilities, falling under the Settings > Preferences section alongside other platform-wide configuration options.

## Open Questions

- Can theme customization be applied per-persona, or is it strictly global?
- Are there any accessibility concerns or limitations with custom colors (e.g., contrast ratios)?
- Is there an API or programmatic way to set the theme for automated deployments?