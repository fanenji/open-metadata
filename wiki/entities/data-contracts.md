---
type: entity
title: Data Contracts
created: 2026-05-14
updated: 2026-05-14
tags: [data-contracts, governance, data-quality, collaboration]
related: [creating-data-contracts, data-quality, data-asset-ownership, classification-tags, tiers, glossary-terms, data-observability-alerts, openmetadata-features, openmetadata-collaboration]
sources: ["creating-data-contracts-openmetadata-data-contract-20260514.md"]
---

# Data Contracts

A **Data Contract** is a formal, versioned agreement between data producers and consumers that defines expectations for a data asset. In OpenMetadata, data contracts are currently available for tables and are created through a structured 6-step UI workflow.

## Purpose

Data contracts shift data governance from passive documentation to active, enforceable agreements. They bridge three critical dimensions:

- **Schema** — Which columns are included in the contract.
- **Semantics** — Business rules governing the asset (Owners, Tags, Domain, Tier, etc.).
- **Quality** — Data Quality Tests that enforce reliability expectations.

## Components

A data contract in OpenMetadata consists of:

1. **Contract Details** — Name, optional Owners, and description.
2. **Schema** — Selected columns from the table.
3. **Semantics** — Business rules for: Service, Owners, Display Name, Name, Description, Tags, Domain, Data Product, Tier.
4. **Quality** — Attached Data Quality Tests.

## Current Scope

- **Supported asset types:** Tables only.
- **Creation method:** UI-driven wizard (see [[creating-data-contracts]]).
- **Execution:** On-demand via "Run now" button after creation.

## Open Questions

- What is the enforcement model? Are contracts purely documentary, or do they block queries/ingestion when violated?
- How are contract violations surfaced? Do they integrate with [[data-observability-alerts]]?
- How are contracts versioned and updated?
- Is there an API for programmatic contract management?
- Will contracts be extended to other asset types (topics, pipelines, dashboards)?

## Related Pages

- [[creating-data-contracts]] — Step-by-step procedural guide.
- [[data-quality]] — Quality tests are a core component.
- [[data-asset-ownership]] — Owners defined in Semantics.
- [[classification-tags]] — Tags defined in Semantics.
- [[tiers]] — Tier defined in Semantics.
- [[glossary-terms]] — Related via Tags and Domain.
- [[openmetadata-features]] — Data Contracts as a platform feature.
- [[openmetadata-collaboration]] — Contracts as a collaboration/governance mechanism.