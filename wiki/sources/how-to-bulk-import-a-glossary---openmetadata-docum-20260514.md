---
type: source
title: How to Bulk Import a Glossary - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, bulk-import, csv, data-governance]
related: [glossary-bulk-import, mutually-exclusive-glossary, glossary-terms, data-asset-ownership, classification-tags]
sources: ["how-to-bulk-import-a-glossary---openmetadata-docum-20260514.md"]
---

# How to Bulk Import a Glossary - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for bulk importing glossary terms via CSV. It covers the complete workflow: creating or updating a glossary, exporting a CSV template, filling in fields (parent, name, displayName, description, synonyms, relatedTerms, references, tags), the mutually exclusive glossary configuration, Owner/Reviewer inheritance, and the validation preview step before final import.

## Key Topics

- **Bulk Import Workflow**: Step-by-step procedure for uploading a CSV with thousands of glossary terms in one go.
- **CSV Field Specifications**: Detailed format rules for each column, including semicolons for list fields (synonyms, relatedTerms, references, tags) and dots for hierarchical parent paths.
- **Mutually Exclusive Glossary**: Configuration option ensuring only one term from a glossary can be applied to a data asset (e.g., PII Sensitive vs. PII Non-Sensitive).
- **Owner/Reviewer Inheritance**: Owners and Reviewers set at the glossary level are automatically propagated to all terms, with the ability to change them later.
- **Validation Preview**: The import utility validates the CSV and shows a preview of elements to be imported before finalizing.

## Relevance

This source is essential for understanding how to efficiently manage large glossaries in OpenMetadata. It complements the existing [[glossary-terms]] page by adding the bulk import workflow and mutually exclusive configuration details. It also extends [[data-asset-ownership]] by clarifying glossary-level Owner/Reviewer propagation.