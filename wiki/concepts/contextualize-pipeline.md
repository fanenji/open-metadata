---
type: concept
title: Contextualize Pipeline
created: 2026-03-14
updated: 2026-03-14
tags: [data-engineering, ai, semantics, pipeline, context]
related: [ecl-framework, context-store, early-binding-vs-late-binding, context-propagation, context-architect-role, ananth-packkildurai]
sources: ["Data Engineering After AI.md"]
---
# Contextualize Pipeline

The **Contextualize pipeline** is a separate, agentic pipeline that runs alongside data infrastructure to build and maintain a living, validated store of semantic context. It is the core architectural innovation of the [[ECL-framework]] proposed by [[Ananth Packkildurai]].

## Design

### Trigger Model
The pipeline is event-driven, not scheduled:
- Every new dataset that lands automatically kicks off the pipeline
- Continuous profiling monitors existing datasets for meaningful changes (new column, dropped column, distribution shifts)
- Any significant change re-triggers the pipeline for affected entities

### Agentic Inference
An AI agent analyzes incoming data — schema, sample values, statistical profiles, lineage — and infers semantic meaning:
- What does this field represent?
- What business entity does it belong to?
- What relationships exist between it and other data?
- Produces structured, versioned context artifacts

### Validation Layer
Inferences don't automatically commit. They route through a validation workflow:
- **High-confidence** inferences validated by LLM-as-Judge before human review
- **Medium-confidence** inferences surfaced to domain experts for labeling
- **Low-confidence or contested** inferences flagged for deeper investigation
- Humans review only the uncertain ones, not every artifact

### Output
Validated artifacts land in the [[context-store]] — a dedicated, versioned, queryable store of semantic definitions, entity classifications, and relationship maps.

## Relationship to Other Pipelines

The Contextualize pipeline is distinct from:
- **Extract pipeline** — handles data movement, not meaning
- **Query-time processes** — context is pre-validated and stored, not inferred on the fly

## Open Questions

- How to design the trigger model for production scale
- How to structure the labeling workflow for domain experts
- What validation confidence threshold earns formalization
- How to version context artifacts as definitions evolve