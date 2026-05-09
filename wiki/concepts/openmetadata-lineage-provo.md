---
type: concept
title: OpenMetadata Lineage with W3C PROV-O
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, lineage, provenance, w3c, standards]
related: [openmetadata, openmetadata-standards-overview, data-observability-three-pillars, data-root-cause-analysis]
sources: ["openmetadata-standards-overview.md"]
---
# OpenMetadata Lineage with W3C PROV-O

OpenMetadata implements end-to-end data flow tracking using the W3C PROV-O (Provenance Ontology) standard. This provides a formal, interoperable model for capturing lineage at both column-level and table-level, from source systems through transformations to dashboards and ML models.

The PROV-O standard defines core concepts of entities, activities, and agents, along with their relationships (e.g., wasGeneratedBy, used, wasDerivedFrom). OpenMetadata maps these concepts to data engineering entities: data assets are PROV-O entities, pipeline runs are activities, and users/tools are agents.

This lineage model is expressed in all three representation formats (JSON Schema, RDF/OWL, JSON-LD), enabling SPARQL queries for impact analysis and root cause tracing. It strengthens the wiki's existing [[data-observability-three-pillars]] concept by providing the formal standard behind the lineage pillar, and supports [[data-root-cause-analysis]] by enabling systematic upstream dependency tracing.