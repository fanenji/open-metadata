---
type: concept
title: PII Sample Data Masking
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, pii, sample-data, masking, security]
related: [classification-tags, system-classification, tag-based-access-control, tag-inheritance-for-masking, how-to-classify-data-assets-official-documentation-20260514]
sources: ["sample-data-handling-using-pii-tags---openmetadata-20260514.md"]
---
# PII Sample Data Masking

PII Sample Data Masking is an automatic data protection feature in OpenMetadata that masks sample data displayed in the UI when a PII (Personally Identifiable Information) classification tag is applied to a column or table. Masked values are replaced with `******`, preventing sensitive information from being exposed through sample data views.

## How It Works

### Column-Level Masking
When a PII tag (specifically `PII.Sensitive`) is applied to an individual column, only that column's sample data is masked. Other columns in the same table without PII tags continue to display their actual sample data.

**Example:**
| Column Name | Tag | Sample Data Displayed |
|-------------|-----|-----------------------|
| email | PII.Sensitive | ****** |
| phoneNumber | PII.Sensitive | ****** |
| age | (None) | 25 |

### Table-Level Masking and Inheritance
When a PII tag is applied at the table level, all columns within that table inherit the masking behavior. The UI displays "Inherited from Table" as the tag notation for each column, and all sample data values show `******`.

**Example:**
| Column Name | Tag | Sample Data Displayed |
|-------------|-----|-----------------------|
| email | Inherited from Table | ****** |
| phoneNumber | Inherited from Table | ****** |
| age | Inherited from Table | ****** |

This inheritance mechanism simplifies governance for wide tables with many sensitive columns, allowing a single tag application to protect all columns at once.

## Relationship to Classification Tags

PII Sample Data Masking demonstrates that [[classification-tags]] in OpenMetadata are not merely descriptive labels — they can trigger automated platform behaviors. This is a key differentiator from simpler tagging systems. See [[tag-inheritance-for-masking]] for more on the propagation mechanism.

## Relationship to Access Control

While [[tag-based-access-control]] governs *who can see* data assets, PII masking governs *what sample data is displayed* within those assets. These two features are complementary layers of a comprehensive data governance strategy.

## Open Questions

- **API Response Masking:** Does PII sample data masking apply to API responses, or only to the OpenMetadata UI? This has significant security implications for integrations and automation that consume metadata via the REST API.
- **Complete PII Tag List:** The documentation only mentions `PII.Sensitive`. Are there other PII tags (e.g., `PII.None`, `PII.Confidential`) that also trigger masking?
- **Tag Conflict Resolution:** If a column has both a PII tag and a non-PII tag, which takes precedence for masking behavior?

## How to Apply

1. Navigate to the column or table in the OpenMetadata UI.
2. Apply the `PII.Sensitive` tag via the tagging options.
3. Ensure auto-classification or manual tagging captures the correct columns during ingestion.

See [[how-to-classify-data-assets-official-documentation-20260514]] for the full classification workflow.