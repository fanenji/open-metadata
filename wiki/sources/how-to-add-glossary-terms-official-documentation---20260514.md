---
type: source
title: "How to Add Glossary Terms | Official Documentation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, tags, data-governance]
related: [glossary-tags, classification-tags, how-to-add-tags, tag-inheritance-for-masking, how-to-add-glossary-terms]
sources: ["how-to-add-glossary-terms-official-documentation---20260514.md"]
---

# How to Add Glossary Terms | Official Documentation - OpenMetadata Documentation

**Source:** https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/glossary

## Summary

This official documentation page describes the procedure for applying Glossary Terms to data assets in OpenMetadata v1.12.x. It covers a simple 3-step UI workflow and introduces the key concept of tag propagation: when a Glossary Term has associated Tags, applying that term to a data asset automatically applies those tags as well.

## Key Content

- **Glossary Term Application Workflow:** From the Explore page, select a data asset, click the edit icon or + Add for Glossary Term, search/select the relevant term, and click the checkmark to save.
- **Tag Propagation:** If Tags are associated with a Glossary Term, applying that term to a data asset automatically applies the associated tags. Example: the glossary term 'Account' with a PII.Sensitive tag propagates that tag to the asset.
- **Viewing Associated Terms:** All associated glossary terms are visible in the right panel of the data asset page.

## Relevance

This source provides the practical application workflow for glossary terms, which was missing from the existing [[glossary-tags]] concept page. It also introduces the tag propagation behavior, which extends the understanding of [[classification-tags]] and [[tag-inheritance-for-masking]].