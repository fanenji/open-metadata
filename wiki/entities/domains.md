---
type: entity
title: Domains
created: 2026-05-14
updated: 2026-05-15
tags: [data-mesh, governance, organizational, data-governance, openmetadata, domains]
related: [data-mesh-openmetadata, data-products, domain-inheritance, domain-only-view, data-mesh, openmetadata, teams-and-users, glossary-terms, classification-tags, data-asset-ownership, hierarchy-view, explore-page]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md", "domains-data-products-official-documentation---ope-20260514.md", "how-to-use-domains-openmetadata-governance-guide---20260514.md"]
---
# Domains

In [[OpenMetadata]], Domains are organizational units that implement the [[data-mesh]] principle of distributed data ownership while also serving as a governance tool for organizing data assets into logical groupings based on business area or purpose. A domain represents a team or business unit with end-to-end ownership of its data lifecycle — from operational data sources through ETL pipelines to curated data products. Each domain is aligned with a business capability and manages its data as a product, ensuring it is available, reliable, and understandable to other domains within the organization. Domains provide a structured way to manage data discovery, ownership, and accountability across the organization.

## Key Characteristics and Principles

- **Exclusive membership**: Data assets, glossaries, and other entities can belong to only one domain, establishing clear organizational boundaries.
- **Rich documentation**: Domains include a dedicated documentation tab for extensive descriptions of the domain's purpose, use cases, and structure.
- **Ownership and experts**: Each domain has a designated owner and can list domain experts for collaboration and support.
- **Internal asset listing**: All assets belonging to a domain are listed within the domain view, including tables, dashboards, pipelines, and more.
- **Decentralization**: Each domain operates independently, owning and managing its data. This reduces bottlenecks and allows for scalable and agile data management.
- **Domain Ownership**: The domain team is responsible for data quality, security, and compliance within their scope. This ensures accountability and commitment to high data standards.
- **Cross-functional Teams**: Domain teams include data engineers, data scientists, product managers, and domain experts, covering all aspects of data management from technical implementation to business relevance.
- **Domain-driven Design**: Data products and services are aligned with the business domain, ensuring relevance to business needs and processes.

Domains are categorized into three types (see [[#Domain Types]]).

## Domain Types

OpenMetadata defines three domain types that align with the typical data flow architecture:

- **Source-aligned Domain**: Closer to online services and transactional databases, including events and transactional data. These domains represent the raw, operational data sources.
- **Aggregate Domain**: Collects and curates data from multiple source-aligned domains to provide aggregated data and data products, such as Customer 360. In the [[data-mesh]] model, these are sometimes referred to as centralized multi-domain teams.
- **Consumer-aligned Domain**: User-facing domains where the end product combines data from various domains for business users or data citizens for decision-making. These domains represent the final, consumption-ready data layer.

## Benefits

- **Improved Data Quality**: Dedicated domain teams focus on data quality and relevance.
- **Scalability**: Decentralized domains can scale independently.
- **Agility**: Domain teams can rapidly develop and deploy data solutions without waiting for centralized teams.
- **Enhanced Collaboration**: Clear ownership and well-defined interfaces facilitate better data sharing.

## Implementing Domains

The following steps guide the implementation of domains in an OpenMetadata instance:

1. **Define organizational structure and identify key domains**: Determine the business areas or capabilities that will form the domains.
2. **Create the domain in the OpenMetadata UI**:
   - **Name & Display Name**: Provide a unique internal identifier and a user‑friendly display name.
   - **Description**: Write a detailed description explaining the domain's purpose, the types of data it contains, and relevant context.
   - **Domain Type**: Select one of the three domain types (Source-aligned, Aggregate, Consumer-aligned).
   - **Owner/Experts**: Assign users or teams as owners or experts responsible for the domain.
3. **Add data assets**: After creation, add data assets (tables, dashboards, pipelines, etc.) to the domain. This can be done from the domain view.
4. **Categorize associated entities**: Assign glossaries and teams to the appropriate domain to ensure governance alignment.
5. **Assign ownership and governance responsibilities**: Ensure that domain teams have clear ownership and accountability for the data within their domain.
6. **Use the Explore page filter**: The Explore page allows filtering data assets by domain, enhancing discoverability and reducing cognitive load.

## Domain Inheritance

Domains support hierarchical inheritance: setting a domain at the database level automatically propagates the domain assignment to all schemas, tables, and stored procedures underneath. This eliminates the need to tag each asset individually. See [[domain-inheritance]].

## Domain-Only View

A UI filter that restricts visibility to assets within a single domain, reducing cognitive load for domain-specific users (e.g., a data scientist in the Marketing domain seeing only Marketing assets). This view is planned to extend to data quality and data insights in future releases. See [[domain-only-view]].

## Relationship to Other Entities

Domains interact with several other OpenMetadata governance and organizational features:

- **[[teams-and-users]]**: Teams can be associated with specific domains. Users and teams can be assigned as domain owners or experts, linking organizational structure to domain governance.
- **[[glossary-terms]]**: Glossaries can be associated with domains for domain‑specific business metadata. Glossary terms define business metadata classification and can be applied within or across domains.
- **[[classification-tags]]**: Tags provide granular metadata labels on individual assets, while domains provide a higher‑level organizational container. Tags can be applied within domain contexts.
- **[[data-asset-ownership]]**: Domains extend the ownership model by adding domain‑level ownership, distinct from individual asset ownership. Domain teams own and manage their data assets.
- **[[data-products]]**: Domains produce and manage data products as their core outputs. Data Products can be considered the next step after domain creation, representing the curated outputs of a domain.
- **[[hierarchy-view]] and [[Explore Page]]**: Domains provide an additional filtering dimension on the Explore page, enhancing hierarchical data discovery by allowing users to filter assets by domain.
- **[[domain-only-view]]**: (Closely related; see dedicated section above.)

## Configuration Flexibility

- **Subdomains**: Supported in the backend but hidden in the initial 1.2.0 release to avoid overwhelming users; planned for gradual introduction.
- **Disable entirely**: Organizations that find data mesh overkill can turn off domains and data products entirely.
- **Independent data products**: Future releases will support data products that exist independently of domains.

## Open Questions

- How do domains interact with the [[hybrid-rbac-abac-model]]? Can domain membership grant or restrict access to data assets?
- How do domains relate to [[data-products]]? The guide presents Data Products as the next step after domain creation.
- Can a data asset belong to multiple domains? The guide implies a single-domain assignment but does not explicitly state constraints.