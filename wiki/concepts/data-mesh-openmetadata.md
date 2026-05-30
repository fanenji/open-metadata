---
type: concept
title: "Data Mesh in OpenMetadata"
created: 2026-05-14
updated: 2026-05-14
tags: [data-mesh, domains, data-products, governance, organizational]
related: [domains, data-products, domain-inheritance, domain-only-view, glossary-approval-workflow, data-contracts]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Data Mesh in OpenMetadata

Data mesh is an organizational principle for distributed data ownership, where domain-aligned teams own the end-to-end lifecycle of their data and expose curated data products to consumers. [[OpenMetadata]] implements data mesh through [[domains]] and [[data-products]], introduced in the 1.2.0 release.

## Core Philosophy

As stated in the 1.2.0 community meeting: **"data mesh is not an architectural principle, it's an organizational principle."** OpenMetadata's approach focuses on enabling the organizational structure — domains, distributed ownership, data products — rather than prescribing infrastructure changes. This pragmatic framing lowers adoption barriers by not requiring organizations to restructure their data platforms.

## Key Components

### Domains
Organizational boundaries representing teams or business units with end-to-end data ownership. Domains contain data assets, glossaries, and other entities. Key properties:
- **Exclusive membership**: Assets belong to exactly one domain.
- **Domain inheritance**: Setting a domain at the database level propagates to all child assets.
- **Domain-only view**: UI filter restricting visibility to a single domain's assets.
- **Configurable**: Can be disabled entirely for small organizations.

See [[domains]] for full details.

### Data Products
Logical groupings of one or more data assets (tables, dashboards, APIs) exposed as consumable products. Key properties:
- **Multi-membership**: An asset can belong to multiple data products.
- **Public discoverability**: Visible even under domain-only view.
- **Consumer-centric**: Designed around consumer use cases with guarantees (quality, SLAs).

See [[data-products]] for full details.

## Design Decisions for Gradual Adoption

1. **Subdomains hidden initially**: Backend support exists but UI is hidden to avoid overwhelming users.
2. **Disable toggle**: Small organizations can turn off domains and data products entirely.
3. **Independent data products (planned)**: Future releases will allow data products without domains.
4. **Domain inheritance**: Reduces tagging burden by propagating domain assignment downward through hierarchy.

## Asymmetry: Domains vs. Data Products

A notable design choice: **data assets cannot belong to multiple domains**, but **a data asset can be part of multiple data products**. This asymmetry reflects the different purposes — domains are organizational boundaries (exclusive), while data products are consumable groupings (flexible).

## Future Directions

- **Subdomains**: Hierarchical nesting within domains for specialized sub-groupings.
- **Domain-only views for data quality and insights**: Scoping analytics to individual domains.
- **Data contracts**: Combining data quality tests, SLAs, and freshness guarantees into formal agreements for data products.
- **Community-driven best practices**: The team acknowledges that data mesh implementation varies across organizations and plans to adapt based on community feedback.