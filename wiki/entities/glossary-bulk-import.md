---
type: entity
title: Glossary Bulk Import
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, bulk-import, csv, data-governance]
related: [glossary-terms, mutually-exclusive-glossary, data-asset-ownership, classification-tags, tag-request-workflow]
sources: ["how-to-bulk-import-a-glossary---openmetadata-docum-20260514.md"]
---

# Glossary Bulk Import

Glossary Bulk Import is a feature in [[OpenMetadata]] that allows users to create or update thousands of [[glossary-terms|glossary terms]] simultaneously by uploading a CSV file. It replaces manual term-by-term creation, saving time and ensuring consistency across large taxonomies.

## Workflow

1. **Navigate** to Govern > Glossary.
2. **Create or select** a glossary. You can bulk upload terms to a new or existing glossary.
3. **Export the CSV template**: Click the ⋮ icon and select Export. If terms already exist, they are exported; otherwise, a blank template is downloaded.
4. **Fill in the CSV** with the required fields (see below).
5. **Import**: Click the ⋮ icon, select Import, drag and drop or browse to upload the CSV.
6. **Validation Preview**: The system validates the file and displays a preview of elements to be imported.
7. **Confirm Import**: Click Import to finalize. A success or failure message is shown.

## CSV Field Specifications

| Field | Required | Description | Format |
|-------|----------|-------------|--------|
| parent | No | Defines hierarchy; leave blank for root-level terms | Dots for hierarchy, e.g., `Banking.Account.Savings Account` |
| name | Yes | Name of the glossary term | Plain text |
| displayName | No | Display name of the glossary term | Plain text |
| description | Yes | Description or details of the term | Plain text |
| synonyms | No | Words with the same meaning | Semicolon-separated, e.g., `Client;Shopper;Purchaser` |
| relatedTerms | No | Terms with related concepts (must already exist in OpenMetadata) | Hierarchy with dots, semicolon-separated, e.g., `Banking.Account.Savings account;Banking.Debit card` |
| references | No | Links to external sources | Format: `(name;url;name;url)`, e.g., `IBM;https://www.ibm.com/;World Bank;https://www.worldbank.org/` |
| tags | No | Existing tags in OpenMetadata | Format: `PII.Sensitive;PersonalData.Personal` |

## Important Notes

- **Related Terms Dependency**: The `relatedTerms` field requires terms to already exist in OpenMetadata, creating a dependency on import order for complex glossaries.
- **Owner/Reviewer Inheritance**: Owners and Reviewers set at the glossary level are automatically propagated to all terms. These can be changed later at the term level.
- **Mutually Exclusive Glossaries**: If a glossary is marked as mutually exclusive, only one term from that glossary can be applied to a data asset. See [[mutually-exclusive-glossary]].
- **Validation Preview**: Always review the preview before importing to catch malformed data.

## Related Features

- [[glossary-terms]] — Individual classification objects within a glossary.
- [[mutually-exclusive-glossary]] — Configuration for mutually exclusive terms.
- [[data-asset-ownership]] — Owner/Reviewer propagation from glossary to terms.
- [[classification-tags]] — Tags that can be assigned to glossary terms during import.
- [[tag-request-workflow]] — Alternative workflow for requesting tag changes.