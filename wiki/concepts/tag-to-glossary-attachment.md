---
type: concept
title: Tag-to-Glossary Attachment
created: 2026-05-14
updated: 2026-05-14
tags: [classification, glossary, data-governance, automation]
related: [classification-tags, glossary-terms, classification-best-practices, how-to-add-glossary-terms]
sources: ["best-practices-for-classification-official-documen-20260514.md"]
---
# Tag-to-Glossary Attachment

Tag-to-Glossary Attachment is a governance pattern in [[OpenMetadata]] where [[classification-tags|classification tags]] are attached to [[glossary-terms|glossary terms]] to combine semantic meaning with data type classification in a single step. When a glossary term with attached classification tags is applied to a data asset, the associated tags are automatically applied to that asset.

## How It Works

1. A glossary term is created to define the semantic meaning of a data concept (e.g., "Customer Email").
2. Classification tags (e.g., `PII.Sensitive`) are attached to the glossary term.
3. When the glossary term is applied to a data asset (column or table), the attached classification tags are automatically propagated to that asset.

## Benefits

- **Scales governance**: Data producers create tables and data models, while governance-aware team members define glossary terms with attached classification tags.
- **Reduces manual effort**: Eliminates the need to manually apply classification tags to each data asset individually.
- **Ensures consistency**: Guarantees that the same classification tags are applied whenever a specific glossary term is used.
- **Enables auto-assignment of PII tags**: The most impactful use case is attaching `PII.Sensitive` tags to glossary terms that represent personally identifiable information.

## Relationship to Existing Features

This pattern extends the behavior documented in [[how-to-add-glossary-terms]], which notes that "associated tags are automatically applied" when a glossary term is added to a data asset. The tag-to-glossary attachment pattern provides the strategic rationale and implementation guidance for this feature.

## Open Questions

- Does this pattern work with all classification tags or only specific ones (e.g., PII tags)?
- Is there a limit to how many classification tags can be attached to a single glossary term?
- Does renaming a classification tag retroactively update all existing tag assignments on data assets that were applied via glossary term attachment?