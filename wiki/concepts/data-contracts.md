---
type: concept
title: Data Contracts
created: 2026-05-14
updated: 2026-05-15
tags: [data-mesh, data-quality, governance, future-feature, data-contracts, collaboration]
related: [data-mesh-openmetadata, data-products, data-quality, glossary-approval-workflow, data-contracts, creating-data-contracts, data-asset-ownership, classification-tags, tiers, glossary-terms, data-observability-alerts]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md", "creating-data-contracts-openmetadata-data-contract-20260514.md"]
---

# Data Contracts

A **Data Contract** is a formal, versioned agreement between data producers and consumers that specifies the schema, semantics (business rules), and quality expectations for a data asset. In [[OpenMetadata]], data contracts represent a shift from passive metadata documentation to active, enforceable agreements, unifying three dimensions of data governance:

- **Schema** — Which columns are included.
- **Semantics** — Business rules (Owners, Tags, Domain, Tier, Glossary terms, etc.).
- **Quality** — Data Quality Tests that enforce reliability.

## Vision and Planned Components

Data contracts were first described as a future concept in the OpenMetadata 1.2.0 community meeting, aligning with the [[data-mesh-openmetadata|data mesh]] framework. In data mesh, [[data-products|data products]] are provided to consumers with guarantees; data contracts formalise those guarantees, making them explicit, measurable, and enforceable. The planned components include:

- **Data quality tests** — Using existing [[data-quality]] definitions and results.
- **SLAs** — Service level agreements defining expected availability, performance, and accuracy.
- **Freshness guarantees** — Commitments on how up-to-date data will be.

The full vision – including SLAs, freshness guarantees, an enforcement model, versioning, and a programmatic API – remains on the roadmap. The existing [[glossary-approval-workflow]] and data quality features are foundational building blocks for this concept.

## Current Implementation

As of the latest release, OpenMetadata provides a structured UI workflow for creating data contracts on tables. The process follows a 6‑step wizard:

1. **Contract Details** — Name, optional Owners, description.
2. **Schema** — Select columns.
3. **Semantics** — Define business rules (Owners, Tags, Domain, Tier, Glossary Terms, etc.).
4. **Quality** — Add Data Quality Tests.
5. **Save** — Finalize.
6. **Run** — Execute on demand.

This initial implementation focuses on the schema and semantics aspects, with integrated data quality tests. It does not yet include the planned SLAs or freshness guarantees.

## Current Limitations

- Available only for tables.
- No documented enforcement model (blocking vs. documentary).
- No documented versioning or update mechanism.
- No API for programmatic management.

## Relationship to OpenMetadata Concepts

- [[data-quality]] — Contracts incorporate Data Quality Tests.
- [[data-asset-ownership]] — Owners are a semantic rule.
- [[classification-tags]] — Tags are a semantic rule.
- [[tiers]] — Tier is a semantic rule.
- [[glossary-terms]] — Related via Tags and Domain.
- [[data-observability-alerts]] — Potential integration point for violation notifications.
- [[data-products]] — Contracts are the formal guarantee for data products within the data mesh framework.
- [[glossary-approval-workflow]] — A building block for future contract lifecycle workflows.