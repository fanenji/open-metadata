---
type: source
title: "Auto-Classification in OpenMetadata"
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, auto-classification, pii, nlp]
related: [auto-classification, auto-pii-tagging, tag-mapping, classification-tags, data-profiling, pii-sample-data-masking]
sources: ["auto-classification-in-openmetadata---openmetadata-20260514.md"]
authors: ["OpenMetadata Documentation"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification"
venue: "OpenMetadata Docs v1.12.x"
---
# Auto-Classification in OpenMetadata

Official documentation page covering the auto-classification workflow in OpenMetadata v1.12.x. Describes how the platform uses NLP during the profiler ingestion phase to automatically detect PII and sensitive data, assigning relevant classification tags such as `PII.Sensitive`. Also introduces the concept of tag mapping — a backend-only feature where applying one tag automatically cascades to another associated tag.

Key topics:
- **Auto PII Tagging**: NLP-based detection of personally identifiable information using column names and sample data content.
- **Tag Mapping**: Backend association between related tags (e.g., `Personal Data.Personal` → `Data Classification.Confidential`) that triggers automatic secondary tag application.
- **Sample Data Analysis**: Classification can be content-driven, not just name-driven, as demonstrated by the `number_of_orders` example.

This source is the primary reference for understanding OpenMetadata's automated classification capabilities and their relationship to the broader data governance framework.