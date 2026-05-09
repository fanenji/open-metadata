---
type: entity
title: OpenMetadata Provenance Ontology
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, provenance, lineage, prov-o, rdf, semantic-web]
related: [openmetadata, openmetadata-ontology, data-observability-three-pillars, data-root-cause-analysis, data-incident-management]
sources: ["openmetadata-rdf-ontologies-overview.md"]
---
# OpenMetadata Provenance Ontology

The OpenMetadata Provenance Ontology extends the W3C PROV-O standard to provide standardized provenance tracking within OpenMetadata's semantic web stack.

## Coverage

- **Data Lineage**: Track data transformations and dependencies between entities
- **Activity Tracking**: Record metadata operations and changes over time
- **Attribution**: Identify responsible agents (users, systems, processes)
- **Derivation**: Capture how entities are derived from others

## W3C PROV-O Standard

PROV-O is a W3C-recommended ontology for provenance interchange. By extending PROV-O, OpenMetadata ensures compatibility with external provenance systems and tools.

## Relationship to Existing Wiki Concepts

The provenance ontology provides a standardized, machine-readable foundation for concepts already documented in the wiki:

- [[data-observability-three-pillars]] — Lineage is one of the three pillars; PROV-O provides a formal model
- [[data-root-cause-analysis]] — Standardized provenance enables automated upstream dependency tracing
- [[data-incident-management]] — Attribution and activity tracking support incident investigation

## Significance

This ontology enables OpenMetadata to serve as a provenance hub that can exchange lineage information with external systems using a W3C standard, rather than relying on proprietary formats. This is particularly valuable for organizations with heterogeneous tooling.

## Open Questions

- How does the PROV-O extension handle real-time lineage updates?
- Can external systems push provenance data into OpenMetadata using PROV-O?
- What is the granularity of activity tracking (per-query, per-job, per-pipeline)?