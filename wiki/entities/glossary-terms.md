---
type: entity
title: Glossary Terms
created: 2026-05-14
updated: 2026-05-15
tags: [openmetadata, glossary, governance, metadata, business-metadata, classification, data-governance, glossary-styling]
related: [glossary-tags, classification-tags, data-asset-ownership, tag-inheritance-for-masking, how-to-add-glossary-terms, import-export-troubleshooting, mutually-exclusive-glossary-terms, glossary-term-version-history, glossary-term-lifecycle, tag-based-access-control, glossary-styling, asset-association, how-to-add-assets-to-glossary-terms, pii-sample-data-masking, tags]
sources: ["how-to-add-glossary-terms-official-documentation---20260514.md", "troubleshooting-for-import-export-issue---openmeta-20260514.md", "what-is-a-glossary-term-official-documentation---o-20260514.md", "glossary-styling-openmetadata-glossary-customizati-20260514.md", "how-to-add-assets-to-glossary-terms---openmetadata-20260514.md", "“how-to-add-glossary-terms-official-documentation---20260514.md”", "“troubleshooting-for-import-export-issue---openmeta-20260514.md”", "“what-is-a-glossary-term-official-documentation---o-20260514.md”", "“glossary-styling-openmetadata-glossary-customizati-20260514.md”", "“how-to-add-assets-to-glossary-terms---openmetadata-20260514.md”"]
---

# Glossary Terms

A **Glossary Term** is a preferred terminology for a concept within OpenMetadata’s data governance framework. Glossary Terms are business metadata classification objects that can be applied to data assets, enabling consistent terminology, semantic relationships, and automated tag propagation. They provide a structured vocabulary for describing and categorizing data in business terms, supporting governance, discovery, and collaboration. They are part of the [[glossary-tags]] system and serve as a structured way to organize and govern data assets using business vocabulary. Glossary Terms complement technical metadata with business context.

## Structure

A glossary term can include the following information:

- **Description** — A unique and clear definition to establish consistent usage and understanding. This is a mandatory requirement.
- **Tags** — [[classification-tags]] can be added to glossary terms. When adding a glossary term to assets, it will also add the associated tags to that asset. This helps to further describe and categorize the data assets.
- **Synonyms** — Other terms that are used for the same concept (e.g., for ‘Customer’, synonyms can be ‘Client’, ‘Shopper’, ‘Purchaser’).
- **Child Terms** — Build a conceptual hierarchy (Parent-Child relationship) to go from generic to specific concepts (e.g., for ‘Customer’, child terms can be ‘Loyal Customer’, ‘New Customer’).
- **Related Terms** — Build a network of concepts to capture an associative relationship (e.g., for ‘Customer’, related terms can be ‘Customer LTV’, ‘Customer Acquisition Cost’).
- **References** — Links from the internet from where the term was inherited.
- **Mutually Exclusive** — Configuration preventing assignment of multiple terms from the same glossary/term to a single data asset. See [[mutually-exclusive-glossary-terms]].
- **Reviewers** — A set of users who review and accept changes to the glossary for governance.
- **Assets** — Data assets associated with the term, aiding in data discovery.

## UI Layout

The details of a Glossary Term are displayed in three tabs:

1. **Overview Tab** — Displays the term’s details, synonyms, related terms, references, tags, owner, and reviewers.
2. **Glossary Term Tab** — Displays all child terms associated with the parent term; allows adding more child terms.
3. **Assets Tab** — Displays all assets associated with the term, subgrouped by database; allows adding more assets via search and filter.

## Asset Association

Glossary Terms support a bidirectional relationship with data assets:

- **Term → Asset:** From the Glossary Term’s **Assets Tab** (see [UI Layout](#ui-layout) for details), users can add associated data assets by clicking **Add > Assets**, searching and filtering by type, and saving. For the full workflow, refer to [[how-to-add-assets-to-glossary-terms]].
- **Asset → Term:** From a data asset’s page, users can apply a Glossary Term to it. See [[how-to-add-glossary-terms]] for the step-by-step UI procedure.

For the concept of this bidirectional relationship, see [[asset-association]].

## Tag Propagation

A key governance feature: when a Glossary Term is applied to a data asset, any [[classification-tags]] associated with the term are automatically propagated to that asset. This enables consistent classification across the data estate and ensures consistent tagging without manual effort.

For example, if the glossary term ‘Account’ has a `PII.Sensitive` tag associated with it, adding the ‘Account’ term to a data asset will also add the `PII.Sensitive` tag to that asset.

This behavior is similar to [[tag-inheritance-for-masking]], where a table-level PII tag propagates masking to all columns, but operates at the level of glossary term → associated tags rather than parent → child asset. It also connects to [[pii-sample-data-masking]] for sensitive data handling.

## Styling

Glossary Terms support [[glossary-styling]] — the ability to customize terms with colors and icons for visual identification. When a glossary term is styled with a color and/or icon, and then applied to a data asset, the visual styling helps users quickly differentiate and identify the required data assets.

The styling procedure is:
1. Navigate to the glossary term.
2. Click the three dots icon (⋮) and select **style**.
3. Add an icon image URL and/or change the font color.
4. Click **Submit**.

## Version History

Glossary terms maintain a version history:

- **Backward compatible changes** (e.g., changes to description, tags, or ownership) → Minor version change (+0.1).
- **Backward incompatible changes** (e.g., term deletion) → Major version change (+1.0).

See [[glossary-term-version-history]] for details.

## Life Cycle Status

Each term has a life cycle status (e.g., Draft, Approved). See [[glossary-term-lifecycle]] for details.

## CSV Export Troubleshooting

When exporting a Glossary as a CSV file, the process may hang on “Export initiated successfully” if [[websocket-dependency|WebSockets]] are blocked by network infrastructure. See [[import-export-troubleshooting]] for the full diagnostic and resolution procedure.

## Open Questions

- Is tag propagation one-way (glossary term → asset) or bidirectional?
- Can tags be removed from an asset without removing the glossary term?
- Does the propagation apply retroactively to existing glossary term assignments?
- What happens when a glossary term’s associated tags change after it has been applied to assets?

## Related Pages

- [[how-to-add-glossary-terms]] — Step-by-step procedure for applying glossary terms to data assets.
- [[how-to-add-assets-to-glossary-terms]] — Step-by-step procedure for adding assets to glossary terms.
- [[classification-tags]] — Metadata labels that can be associated with glossary terms.
- [[glossary-tags]] — Broader overview of business metadata classification.
- [[glossary-styling]] — Customizing glossary terms with colors and icons.
- [[mutually-exclusive-glossary-terms]] — Detailed documentation of the mutually exclusive configuration.
- [[tag-based-access-control]] — How tags interact with access control policies.
- [[tag-inheritance-for-masking]] — Visual differentiation through PII masking.
- [[glossary-term-version-history]] — Detailed versioning information.
- [[glossary-term-lifecycle]] — Life cycle status documentation.
- [[asset-association]] — Concept of the bidirectional relationship between glossary terms and data assets.
- [[pii-sample-data-masking]] — Details on PII sample data masking.
- [[tags]] — General tagging concepts.
- [[import-export-troubleshooting]] — Diagnostics for CSV export issues.
- [[data-asset-ownership]] — Ownership assignment for data assets.