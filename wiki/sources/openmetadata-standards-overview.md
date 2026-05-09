---
type: source
title: OpenMetadata Standards — Overview
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, metadata, standards, governance, data-quality, lineage, data-contracts]
related: [openmetadata, openmetadata-business-glossary, openmetadata-lineage-provo, openmetadata-three-format-representation, openmetadata-data-quality-integrations, data-contract-platform, metadata-fields-definition, data-quality-dimensions, data-observability-three-pillars, custom-connector-openmetadata, openmetadata-data-quality]
sources: ["openmetadata-standards-overview.md"]
---
# OpenMetadata Standards — Overview

This source document provides a high-level overview of the OpenMetadata Standards specification, which defines comprehensive metadata models across six key domains of the modern data ecosystem. The specification covers Data Assets, Governance, Data Quality, Lineage, Data Contracts, and Teams & Users, with every entity expressed in three interoperable formats: JSON Schema (Draft-07, 700+ schemas), RDF/OWL (W3C ontology), and JSON-LD (linked data contexts).

The specification is designed to be a complete, standards-based framework for metadata management, integrating with major data quality tools (Great Expectations, dbt, Deequ, Soda) and using W3C PROV-O for end-to-end lineage tracking. It formalizes data contracts as SLAs with schema, quality, and freshness guarantees, and provides a hierarchical governance model through business glossaries and sensitive data classification.

This source is foundational for understanding the formal specification framework behind the [[openmetadata]] platform and provides the standards context for the wiki's existing coverage of data quality, lineage, contracts, and governance.