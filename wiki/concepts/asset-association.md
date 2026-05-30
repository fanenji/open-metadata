---
type: concept
title: Asset Association
created: 2026-05-14
updated: 2026-05-14
tags: [glossary, data-governance, assets, discovery]
related: [glossary-terms, how-to-add-glossary-terms, how-to-add-assets-to-glossary-terms, classification-tags, pii-sample-data-masking]
sources: ["how-to-add-assets-to-glossary-terms---openmetadata-20260514.md"]
---
# Asset Association

Asset Association is the process of linking data assets (Tables, Topics, Dashboards, etc.) to a [[glossary-terms|Glossary Term]] in OpenMetadata. This bidirectional relationship enables business metadata to be applied to technical assets and supports discovery of all assets related to a given business concept.

## Workflow

The primary workflow for associating assets with a Glossary Term is via the **Assets Tab** on the Glossary Term page:

1. Navigate to the Glossary Term.
2. Click **Add > Assets**.
3. Search and filter assets by type (Tables, Topics, Dashboards, etc.).
4. Select the relevant assets and click **Save**.

The reverse direction — applying a Glossary Term to an asset — is covered in [[how-to-add-glossary-terms]].

## Discovery Benefit

Once assets are associated, the Glossary Term page lists all linked assets, subgrouped by type. This makes it easy to discover all data assets related to a business term, supporting governance, impact analysis, and data lineage understanding.

## Tag Propagation

A critical governance feature of asset association is **tag propagation**. If a Glossary Term has associated [[classification-tags|Tags]], applying that term to a data asset automatically applies those tags as well. For example, if the Glossary Term "Account" has a `PII.Sensitive` tag, adding the "Account" term to a table automatically applies the `PII.Sensitive` tag to that table. This ensures consistent tagging without manual effort.

This tag propagation behavior connects to [[pii-sample-data-masking]], where a `PII.Sensitive` tag on a table or column triggers automatic masking of sample data in the UI.

## Open Questions

- Can multiple Glossary Terms be applied to the same asset? If so, how are conflicting tag propagations resolved?
- Is there a limit on the number of assets that can be associated with a single Glossary Term?
- Does removing a Glossary Term from an asset also remove the propagated tags?