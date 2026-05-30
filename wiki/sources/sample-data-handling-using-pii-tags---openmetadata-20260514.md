---
type: source
title: "Sample Data Handling Using PII Tags - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, pii, sample-data, masking]
related: [pii-sample-data-masking, classification-tags, system-classification, tag-based-access-control, how-to-classify-data-assets-official-documentation-20260514]
sources: ["sample-data-handling-using-pii-tags---openmetadata-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/sample-data-using-pii-tag"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# Sample Data Handling Using PII Tags - OpenMetadata Documentation

Official documentation page describing how OpenMetadata automatically masks sample data in the UI when PII (Personally Identifiable Information) tags are applied to columns or tables.

## Key Points

- Applying a PII tag (specifically `PII.Sensitive`) to a column masks that column's sample data, displaying `******` instead of actual values.
- Applying a PII tag at the table level causes all columns in that table to inherit the masking behavior, with the tag notation "Inherited from Table."
- This is a UI-level protection mechanism ensuring sensitive data is not exposed through sample data views.
- The documentation does not specify whether masking applies to API responses or only to the UI display.

## Related Pages

- [[pii-sample-data-masking]] — Dedicated concept page for this feature.
- [[classification-tags]] — General concept of classification tags in OpenMetadata.
- [[system-classification]] — Pre-built system classification tags, including PII.Sensitive.
- [[tag-based-access-control]] — How tags can govern access to data assets.