---
source_url: "https://openmetadatastandards.org/metadata-specifications/overview/#governance"
fetched: 2026-04-14
title: "OpenMetadata Standards — Overview"
author: OpenMetadata Community
published:
original_tags: [clippings]
clipped_from: obsidian-web-clipper
---
**Comprehensive metadata specifications for the modern data ecosystem**

OpenMetadata Standards define metadata models across six key areas:

## Data Assets
10+ asset types: databases, pipelines, dashboards, ML models, topics, storage, APIs, search indexes. Specifications available in JSON Schema, RDF/OWL, and JSON-LD.

## Governance
Business glossaries, sensitive data classification (PII/PHI, GDPR), hierarchical tags, governance policies.

## Data Quality
Quality tests, validation execution, data profiling, quality metrics over time. Integrates with OpenMetadata, Great Expectations, dbt, Deequ, Soda.

## Lineage
End-to-end data flow tracking using W3C PROV-O. Column-level and table-level lineage from source to dashboard to ML model.

## Data Contracts
Formal SLAs for any data asset: schema requirements, quality expectations, freshness guarantees.

## Teams & Users
Users, teams, roles, hierarchies, ownership, access policies.

## Standards Representation

Every entity expressed in three formats:
- **JSON Schema**: Draft-07, 700+ entity schemas, strongly typed
- **RDF & OWL**: W3C ontology, SPARQL-queryable, reasoning & inference
- **JSON-LD**: Linked data contexts, Schema.org compatible, web-scale integration
