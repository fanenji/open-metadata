---
type: concept
title: Mutually Exclusive Glossary
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, data-governance, classification]
related: [glossary-terms, glossary-bulk-import, classification-tags, tag-based-access-control]
sources: ["how-to-bulk-import-a-glossary---openmetadata-docum-20260514.md"]
---

# Mutually Exclusive Glossary

A Mutually Exclusive Glossary is a configuration option in [[OpenMetadata]] that ensures only one term from a given glossary can be applied to a data asset at a time. This is useful for classification scenarios where terms represent mutually exclusive categories.

## Use Cases

- **PII Classification**: An asset can be either `PII Sensitive` or `PII Non-Sensitive`, but not both.
- **Data Criticality**: An asset can be classified as `Critical`, `High`, `Medium`, or `Low`, but only one level applies.
- **Compliance Status**: An asset can be `Compliant` or `Non-Compliant`, but not both simultaneously.

## How It Works

When creating or editing a glossary, the user can enable the **Mutually Exclusive** toggle. Once enabled:

- The system prevents assigning multiple terms from the same glossary to a single data asset.
- If a term from the glossary is already applied, applying another term from the same glossary will replace the previous one or be blocked, depending on the UI behavior.

## Configuration

Mutually Exclusive is set at the glossary level, not at the individual term level. It applies to all terms within that glossary. This can be configured during glossary creation or via the glossary settings.

## Relationship to Tags

Mutually Exclusive glossaries interact with the [[classification-tags]] system. Tags from a mutually exclusive glossary follow the same restriction: only one tag from that glossary can be applied to a data asset. This is distinct from [[tag-based-access-control]], which uses tags for authorization rather than classification exclusivity.

## Related Concepts

- [[glossary-terms]] — Individual terms within a glossary.
- [[glossary-bulk-import]] — CSV-based bulk import workflow for glossary terms.
- [[classification-tags]] — Broader tagging system for data assets.