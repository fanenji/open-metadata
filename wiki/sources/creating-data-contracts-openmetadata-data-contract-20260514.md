---
type: source
title: Creating Data Contracts | OpenMetadata Data Contracts Guide
created: 2026-05-14
updated: 2026-05-14
tags: [data-contracts, data-quality, governance, how-to-guide]
related: [data-contracts, creating-data-contracts, data-quality, data-asset-ownership, classification-tags, tiers, glossary-terms, snowflake]
sources: ["creating-data-contracts-openmetadata-data-contract-20260514.md"]
authors: [OpenMetadata Documentation Team]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/create"
venue: "OpenMetadata Documentation"
---

# Creating Data Contracts | OpenMetadata Data Contracts Guide

This official guide documents the 6-step UI workflow for creating a [[data-contracts|Data Contract]] for a table in OpenMetadata v1.12.x. Data contracts are formal, versioned agreements between data producers and consumers that specify schema, semantics (business rules), and quality expectations for a data asset. Currently, data contracts are available only for tables ingested into OpenMetadata.

The guide uses a Snowflake table (`DEMO_STAGE.JAFFLE_SHOP.CUSTOMERS`) as a concrete example. The six steps are:

1. **Contract Details** — Name the contract, optionally assign Owners and provide a description.
2. **Schema** — Select the columns to include in the contract.
3. **Semantics** — Define business rules for Service, Owners, Display Name, Name, Description, Tags, Domain, Data Product, and Tier.
4. **Quality** — Add Data Quality Tests to the contract.
5. **Save** — Finalize and create the contract.
6. **Run** — Execute the contract on demand via the "Run now" button.

The source is a procedural how-to guide and does not cover enforcement models, versioning, alerting, or API-based contract management. These are open questions for further research.

## Key Takeaways

- Data contracts unify governance (semantics) and data quality (tests) into a single, actionable artifact.
- The workflow is entirely UI-driven and follows a structured wizard pattern.
- The current scope is limited to tables, with potential future expansion to other asset types.
- The guide does not address what happens when a contract is violated, how contracts are versioned, or whether they are enforceable or purely documentary.

## Related Wiki Pages

- [[data-contracts]] — Core concept page for data contracts.
- [[creating-data-contracts]] — Procedural page documenting the 6-step workflow.
- [[data-quality]] — Data quality tests are a core component of contracts.
- [[data-asset-ownership]] — Owners are defined in the Semantics step.
- [[classification-tags]] — Tags are defined in the Semantics step.
- [[tiers]] — Tier is defined in the Semantics step.
- [[glossary-terms]] — Related via Tags and Domain in Semantics.
- [[snowflake]] — Example source system.