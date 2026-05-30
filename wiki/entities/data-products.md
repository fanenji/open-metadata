---
type: entity
title: Data Products
created: 2026-05-14
updated: 2026-05-15
tags: ["data-mesh", "domains", "governance", "data-governance", "openmetadata", "data-products", "explore-page", "data-assets", "glossary-terms", "classification-tags"]
related: ["data-mesh-openmetadata", "domains", "data-mesh", "openmetadata", "openmetadata-features", "data-asset-ownership", "hierarchy-view", "explore-page", "data-assets", "glossary-terms", "classification-tags"]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md", "domains-data-products-official-documentation---ope-20260514.md", "how-to-use-domains-openmetadata-governance-guide---20260514.md", "how-to-use-data-products-official-documentation----20260514.md"]
---

# Data Products

Data Products are logical entities in [[OpenMetadata]] that group one or more data assets (tables, dashboards, pipelines, etc.) into a consumable unit, organized for a specific business purpose. They implement the "data as a product" principle from [[data-mesh-openmetadata|data mesh]], where curated datasets, dashboards, and APIs are treated as products with consumers, SLAs, and continuous improvement. In a [[data-mesh]] architecture, they are the core outputs managed by each [[domains|domain]], designed to be easily discoverable, understandable, and usable by other domains within the organization. Data Products are also a key governance and discoverability tool within OpenMetadata, enabling domain‑oriented data architecture.

## Key Characteristics

- **Composition**: A data product consists of one or more data assets (tables, dashboards, pipelines, etc.). For example, a "Customer Churn" data product could group multiple dashboards (monthly, yearly, by region, by demographic). They are curated and intentionally designed for specific use cases.
- **Multi‑membership**: A data asset can be part of multiple data products. This differs from [[domains]], where data assets cannot belong to multiple domains.
- **Discoverability & Understandability**: Data products are designed as public‑facing assets discoverable even when domain‑only view is active. They can be found and filtered on the [[explore-page|Explore page]], similar to other data assets. Clear documentation and metadata ensure users can understand the data product's contents and usage. Implementation details (ETL pipelines, raw data) should remain internal to the domain.
- **Usability**: Well‑defined interfaces and APIs facilitate easy integration and use by other domains.
- **Ownership & Accountability**: Owned by a team or domain experts who ensure data quality guarantees, SLAs, documentation, and responsiveness to consumer use cases. Clear ownership is crucial for maintaining quality and SLAs. Owners and Experts follow the [[data-asset-ownership]] model and are assigned during creation, serving as points of contact for governance and maintenance.
- **Reliability**: Data products must be reliable and maintain high quality, ensuring trust across the organization.
- **Interoperability**: Data products should integrate seamlessly with other data products and systems within the data mesh.
- **Consumable**: They are packaged for easy consumption by business users, analysts, or downstream systems.
- **Governance**: Provides a structured way to organize and manage data assets around business domains.
- **Domain Relationship**: In the initial release (1.2.0), data products must be created within a domain. Future releases plan to support data products independent of domains.

## Consumer‑Centric Design

The data product paradigm shifts thinking from "data engineers fulfilling requirements" to "product teams understanding consumer use cases and continuously improving the product." This includes providing guarantees (quality, freshness, SLAs) similar to any other product offering.

## Relationship to Domains

Data Products exist within the **Domain → Data Product → Asset** hierarchy. Domains are the top‑level organizational unit, Data Products are logical groupings within a domain, and individual data assets (tables, dashboards, etc.) are the leaf nodes. Data Products represent the output of a domain's data curation and transformation activities. For example, a "Customer 360" domain might produce a "Customer Profile" data product that combines data from multiple source‑aligned domains. In the initial OpenMetadata release (1.2.0), data products must be created inside a domain, but future releases are planned to support them independently.

## Creation Workflow

The process of creating a Data Product involves the following steps:

1. **Name & Display Name**: Provide a unique internal identifier and a user‑friendly display name.
2. **Description**: Write a detailed description explaining the purpose and contents.
3. **Owner/Experts**: Assign users or teams as Owners and Experts for maintenance and governance.
4. **Group Data Assets**: Navigate to the Data Product and add related data assets (tables, dashboards, pipelines, etc.) from within the domain.
5. **Documentation & Metadata**: Provide comprehensive documentation and metadata for each Data Product to ensure discoverability.
6. **View on Explore**: Once created, use the Explore page to view and filter assets by Data Product.

This workflow is performed through the UI; API support is an open question.

## Ownership

Ownership of a Data Product follows the same [[data-asset-ownership]] model as other entities. Owners and Experts are assigned during creation and serve as points of contact for governance and maintenance.

## Examples

- **Analytical Data Models**: Models built for analyzing data to support decision‑making.
- **Streaming Data Products**: Products handling real‑time data streams for immediate insights.
- **Data Pipelines**: Automated processes for collecting, transforming, and loading data.

## Open Questions

- Can Data Products be created/updated via API, or only through the UI?
- What is the JSON Schema for Data Products in the metadata graph?
- Can a Data Product span multiple Domains?
- How do Data Products interact with [[hybrid-rbac-abac-model|RBAC/ABAC policies]]? Can access be scoped to a Data Product? (Currently undocumented.)
- Is there a Data Product catalog or marketplace view?

## Related Entities

- **[[data-asset-ownership]]**: Each Data Product has clear ownership, which is crucial for maintaining quality and SLAs.
- **[[openmetadata-features]]**: Data Products are a key feature of OpenMetadata, enabling the data mesh paradigm within the catalog.
- **[[hierarchy-view]]**: Related to the organizational structure of domains and data products.
- **[[explore-page]]**: Used to discover and filter Data Products.
- **[[data-assets]]**: The building blocks of Data Products.
- **[[glossary-terms]]** and **[[classification-tags]]**: May be associated with Data Products for governance.