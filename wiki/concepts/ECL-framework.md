---
type: concept
title: ECL Framework (Extract, Contextualize, Link)
created: 2026-03-14
updated: 2026-03-14
tags: [data-engineering, architecture, ai, semantics, context]
related: [ananth-packkildurai, contextualize-pipeline, context-store, early-binding-vs-late-binding, context-propagation, context-architect-role, data-contract-platform, data-catalog-critique, embedded-metadata]
sources: ["Data Engineering After AI.md"]
---
# ECL Framework (Extract, Contextualize, Link)

The **ECL framework** (Extract, Contextualize, Link) is a proposed replacement for the traditional ETL (Extract, Transform, Load) framework in data engineering. Proposed by [[Ananth Packkildurai]] in his article "[[Data Engineering After AI]]", ECL reorients data engineering from data movement to data meaning.

## The Three Components

### Extract
Data still needs to move from source systems to analytical environments. AI handles the mechanical parts, but architectural decisions about what to extract, when, and how remain human responsibilities. This includes judgments about reliability, latency, volume, and failure modes.

### Contextualize
The core innovation of ECL. This is the work of giving data semantic meaning — understanding that "revenue" is calculated differently by Finance and Sales, that a timestamp in a clickstream event means something different than a timestamp in a billing record. AI can draft this work at scale, but human judgment is required for validation and formalization. The [[contextualize-pipeline]] is the engineering implementation of this component.

### Link
Entity relationships across the data landscape — connecting a customer record in CRM to a user record in a product database, linking an event in analytics to a session in a support tool. Linkage makes context portable, allowing meaning built in one part of the landscape to be grounded in its relationships to the rest.

## Key Techniques

- **[[early-binding-vs-late-binding]]** — Two complementary approaches for capturing context
- **[[context-propagation]]** — How context travels alongside the pipeline via metadata and lineage
- **[[context-store]]** — The new infrastructure component for storing validated semantic artifacts

## Relationship to Existing Concepts

- **vs. ETL**: ECL replaces the Transform step with Contextualize and Link, shifting focus from data transformation to meaning preservation
- **vs. [[data-contract-platform]]**: ECL embraces contracts as early binding but argues they are insufficient alone — the Contextualize pipeline is needed alongside
- **vs. [[data-catalog-critique]]**: ECL's emphasis on embedded context over separate catalogs aligns with the critique
- **vs. [[embedded-metadata]]**: Context propagation via metadata/lineage directly supports this concept

## Open Questions

- Tooling for the Contextualize pipeline and Context Store is still maturing
- Organizational patterns for governing ownership of the Context Store are not yet established
- How discovered context graduates to prescribed context is an open pattern