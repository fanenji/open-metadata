---
type: entity
title: Glossary Export
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, export, csv, data-governance]
related: [glossary-terms, how-to-add-glossary-terms, classification-tags, glossary-approval-workflow]
sources: ["glossary-export-openmetadata-export-guide---openme-20260514.md"]
---
# Glossary Export

**Glossary Export** is a feature in [[OpenMetadata]] that allows users to download the terms of a [[glossary-terms|Glossary]] as a CSV file. It is the counterpart to the Bulk Import feature, which enables uploading glossary terms via CSV.

## Procedure

1. Navigate to **Govern > Glossary** in the OpenMetadata UI.
2. Locate the desired glossary and click the **⋮ (ellipsis) icon**.
3. Select **Export** from the dropdown menu.

## Behavior

- If the glossary contains terms, the exported CSV file will be populated with those terms.
- If the glossary is empty, a blank CSV template is downloaded instead. This template can be used as a starting point for [[how-to-add-glossary-terms|bulk importing]] terms.

## Related Features

- **[[how-to-add-glossary-terms|Bulk Import]]** — The complementary operation for uploading glossary terms via CSV.
- **Glossary Approval Workflow** — A review and approval process for glossary terms (not yet documented in this wiki).
- **[[classification-tags]]** — A parallel governance concept for classifying data assets.

## Notes

- The exact CSV schema/column structure for exported terms is not specified in the official documentation.
- The export feature is a simple, two-step UI process with no configuration options.