---
type: source
title: How to Add Assets to Glossary Terms - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [glossary, data-governance, assets, tags]
related: [glossary-terms, how-to-add-glossary-terms, classification-tags, asset-association, pii-sample-data-masking]
sources: ["how-to-add-assets-to-glossary-terms---openmetadata-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/assets"
venue: OpenMetadata Documentation
---
# How to Add Assets to Glossary Terms - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for associating data assets (Tables, Topics, Dashboards) with Glossary Terms. It covers the UI workflow via the Assets Tab, the discovery benefit of listing all assets related to a term, and the critical tag propagation behavior where tags associated with a Glossary Term are automatically applied to the data asset when the term is used.

## Key Content

- **Asset Association Workflow:** After creating a Glossary Term, users can add data assets via the Assets Tab by clicking Add > Assets, searching and filtering by type, and saving.
- **Discovery Benefit:** The Glossary Term page lists all associated assets, subgrouped by type (Tables, Topics, Dashboards), enabling easy discovery of all data assets related to a business term.
- **Tag Propagation:** If a Glossary Term has associated Tags, applying that term to a data asset automatically applies those tags as well. Example: the Glossary Term "Account" with a PII.Sensitive tag auto-applies the tag to the asset.

## Connections

- Complements [[how-to-add-glossary-terms]] (which covers the reverse direction: applying terms to assets).
- Strengthens [[glossary-terms]] with the specific asset association workflow and tag propagation detail.
- Connects to [[classification-tags]] and [[pii-sample-data-masking]] via the PII.Sensitive tag example.
- Introduces the [[asset-association]] concept for the bidirectional relationship.