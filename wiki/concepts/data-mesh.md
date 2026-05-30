---
type: concept
title: Data Mesh
created: 2026-05-14
updated: 2026-05-14
tags: [data-mesh, data-architecture, data-governance, openmetadata]
related: [domains, data-products, domain-only-view, openmetadata, openmetadata-features]
sources: ["domains-data-products-official-documentation---ope-20260514.md"]
---
# Data Mesh

Data Mesh is an architectural paradigm for decentralized data management that serves as the foundation for [[domains|Domains]] and [[data-products|Data Products]] in [[OpenMetadata]]. It shifts data ownership from centralized teams to domain-specific cross-functional teams, treating data as a product.

## Core Principles

- **Domain Ownership**: Each business domain owns and manages its data.
- **Data as a Product**: Data is treated as a product with defined quality, discoverability, and usability standards.
- **Self-serve Data Infrastructure**: Domain teams have access to tools and platforms to manage their data independently.
- **Federated Computational Governance**: Governance is applied across domains through shared standards and policies.

## Relationship to OpenMetadata

OpenMetadata implements Data Mesh principles through:

- **[[domains]]**: Organizational units aligned with business capabilities.
- **[[data-products]]**: Packaged data assets produced by domains.
- **[[domain-only-view]]**: UI feature for focused navigation within a domain.

## Benefits

- Decentralized data ownership reduces bottlenecks.
- Improved data quality through domain accountability.
- Scalable and agile data management.
- Enhanced collaboration across organizational boundaries.