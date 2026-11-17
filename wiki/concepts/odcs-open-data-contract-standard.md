---
type: concept
title: "ODCS: Open Data Contract Standard"
created: 2026-07-07
updated: 2026-07-07
tags: [openmetadata, data-contracts, standards, interoperability, odcs]
related: [data-contracts, openmetadata, openlineage-integration, data-quality]
sources: ["Announcing OpenMetadata 1.12 1.md"]
---
# ODCS: Open Data Contract Standard

The **Open Data Contract Standard (ODCS)** is an open specification for defining data contracts between producers and consumers. Version **3.1** support was introduced in OpenMetadata 1.12.

## What ODCS Defines

Data contracts specify the interface, quality guarantees, and service-level expectations between data producers and consumers — similar to API contracts but for data assets. ODCS standardizes these definitions so contracts are portable across tools and platforms.

## OpenMetadata 1.12 Support

- **Import**: Ingest ODCS 3.1-compliant contracts into OpenMetadata
- **Export**: Publish OpenMetadata data contracts in ODCS format for use by external tools
- **Superset Semantics**: OpenMetadata's contract model provides additional capabilities beyond ODCS — terms of service, ownership definitions, quality specifications — while maintaining ODCS compatibility

## Why It Matters

Open standards like ODCS prevent vendor lock-in. Organizations with existing ODCS contracts can adopt OpenMetadata without rewriting integrations. OpenMetadata's superset approach means teams get:
- Standard compliance for tool interoperability
- Enhanced semantics within the OpenMetadata platform

## Relationship to OpenMetadata Data Contracts

[[data-contracts]] in OpenMetadata were introduced in version 1.9. ODCS 3.1 support in 1.12 adds an interoperability layer: contracts created in OpenMetadata can be exported to ODCS, and external ODCS contracts can be imported into OpenMetadata.

## See Also

- [[data-contracts]] — OpenMetadata data contracts
- [[openlineage-integration]] — OpenLineage support (companion open standard)
- [[openmetadata]] — Platform overview