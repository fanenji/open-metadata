---
type: concept
title: Glossary Styling
created: 2026-05-14
updated: 2026-05-14
tags: [glossary, styling, customization, data-governance, visual-identification]
related: [glossary-terms, how-to-add-glossary-terms, classification-tags, tag-inheritance-for-masking]
sources: ["glossary-styling-openmetadata-glossary-customizati-20260514.md"]
---
# Glossary Styling

**Glossary Styling** is a feature in OpenMetadata that allows users to customize [[glossary-terms]] with colors and icons for visual identification. It enables one-glance differentiation of related concepts and terms, and when applied to data assets via tagging, it makes data assets easier to identify visually.

## Purpose

The primary purpose of glossary styling is to enhance the discoverability and differentiation of data assets through visual cues. By color-coding glossary terms and adding icons, users can quickly identify related concepts and terms without needing to read labels or descriptions.

## Procedure

1. Navigate to the glossary term to be edited.
2. Click on the three dots icon (⋮) and select **style**.
3. Add a link to the icon image. Optionally, change the font color.
4. Click **Submit** to save the changes.

## Benefits

- **One-glance identification**: Color-coded terms enable rapid visual scanning of related concepts.
- **Improved data asset discovery**: When glossary terms are used for tagging data assets, the color-coding helps users quickly locate the required data assets.
- **Consistent visual language**: Icons and colors can be used to establish a consistent visual vocabulary across the organization.

## Open Questions

- What image formats are supported for icons?
- Does styling apply to the tag badge on data assets or only within the glossary tree view?
- Can styling be applied in bulk (e.g., via import/export)?
- Is there a performance impact with many icon URLs?
- Does styling survive glossary export/import operations?

## Related Concepts

- [[glossary-terms]] — The objects being stylized.
- [[how-to-add-glossary-terms]] — The workflow for applying glossary terms to data assets, where styling becomes visible.
- [[classification-tags]] — Another classification mechanism; glossary styling provides visual differentiation that classification tags do not.
- [[tag-inheritance-for-masking]] — A different form of visual differentiation (masking) based on PII tags.