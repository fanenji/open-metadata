---
type: concept
title: Tag Inheritance for Masking
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, pii, inheritance, masking]
related: [pii-sample-data-masking, classification-tags, system-classification]
sources: ["sample-data-handling-using-pii-tags---openmetadata-20260514.md"]
---
# Tag Inheritance for Masking

Tag Inheritance for Masking is the mechanism by which a PII classification tag applied at the table level propagates its sample data masking effect to all columns within that table. In the OpenMetadata UI, columns display "Inherited from Table" as their tag notation, and all sample data values are masked as `******`.

## Behavior

- **Trigger:** Applying a PII tag (e.g., `PII.Sensitive`) to a table rather than to individual columns.
- **Effect:** Every column in the table displays masked sample data (`******`), regardless of whether the column actually contains PII.
- **UI Indication:** The tag column for each affected column shows "Inherited from Table" instead of the tag name directly.

## Purpose

This inheritance behavior simplifies data governance for tables with many sensitive columns. Instead of tagging each column individually — which is error-prone and labor-intensive for wide tables — a data steward can apply a single tag at the table level to protect all sample data at once.

## Open Questions

- **Metadata Model:** Is "Inherited from Table" a display convention in the UI, or does actual tag propagation occur in the metadata model? The documentation does not specify whether child columns receive the tag in the underlying graph.
- **Override Behavior:** Can a column-level tag override or remove the inherited masking? For example, if a table has `PII.Sensitive` but one column is genuinely non-sensitive, can that column be exempted?

## Related Features

- [[pii-sample-data-masking]] — The core masking feature that inheritance supports.
- [[classification-tags]] — The broader tagging system within which inheritance operates.