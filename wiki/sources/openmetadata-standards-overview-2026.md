---
type: source
title: "OpenMetadata Standards — Overview"
created: 2026-07-15
updated: 2026-07-15
tags: [openmetadata, standards, json-schema, rdf, json-ld, metadata-specifications]
related: [openmetadata-standards, rdf-ontology, data-contracts, data-quality, data-lineage]
authors: [OpenMetadata Community]
year: 2026
source_path: "[[raw/sources/openmetadata-standards-overview]]"
sources: ["https://openmetadatastandards.org/metadata-specifications/overview/"]
venue: "OpenMetadata Standards"
---
# OpenMetadata Standards — Overview

Overview of the OpenMetadata Standards project, defining metadata models across six key areas.

## Six Standard Areas

1. **Data Assets** — 10+ asset types (databases, pipelines, dashboards, ML models, topics, storage, APIs, search indexes)
2. **Governance** — Business glossaries, sensitive data classification (PII/PHI, GDPR), hierarchical tags, governance policies
3. **Data Quality** — Quality tests, validation execution, data profiling, quality metrics over time. Integrates with OpenMetadata, Great Expectations, dbt, Deequ, Soda
4. **Lineage** — End-to-end data flow tracking using W3C PROV-O, column-level and table-level
5. **Data Contracts** — Formal SLAs for any data asset: schema requirements, quality expectations, freshness guarantees
6. **Teams & Users** — Users, teams, roles, hierarchies, ownership, access policies

## Three Representation Formats

- **JSON Schema** — Draft-07, 700+ entity schemas, strongly typed
- **RDF & OWL** — W3C ontology, SPARQL-queryable, reasoning & inference
- **JSON-LD** — Linked data contexts, Schema.org compatible, web-scale integration

## Relevance

This source documents the standards that underpin OpenMetadata's [[schema-first-approach]] and [[unified-metadata-graph]], with specific coverage of [[data-contracts]] and [[rdf-ontology]] standards.