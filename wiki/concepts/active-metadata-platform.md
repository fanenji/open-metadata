---
type: concept
title: Active Metadata Platform
created: 2026-05-06
updated: 2026-05-06
tags: [metadata, governance, data-catalog, active-metadata]
related: [openmetadata, data-catalog-critique, embedded-metadata, data-contract-platform]
sources: ["OpenMetadata.md"]
---
# Active Metadata Platform

An **Active Metadata Platform** is an evolution of traditional data catalogs where metadata is not just passively stored and searched but actively used to drive governance, data quality, discovery, and automation.

## Key Characteristics

- **Governance Enforcement:** Metadata rules are enforced automatically (e.g., schema validation, data quality checks).
- **Data Quality Integration:** Built-in quality tests and alerting, not just documentation.
- **Lineage and Impact Analysis:** Active tracking of data flow and dependencies.
- **Automated Discovery:** Proactive profiling and classification of data assets.
- **Resolution Workflows:** Closing the feedback loop on data issues.

## Relationship to Other Concepts

- Contrasts with [[data-catalog-critique|traditional data catalogs]] that are passive and disconnected from data creation.
- Aligns with [[embedded-metadata]] by integrating metadata capture into the data creation process.
- Complements [[data-contract-platform]] by providing the metadata infrastructure for contract enforcement.

## Examples

- [[openmetadata]] — The primary example of an active metadata platform in this wiki.