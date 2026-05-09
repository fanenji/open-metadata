---
type: concept
title: Context Propagation
created: 2026-03-14
updated: 2026-03-14
tags: [data-engineering, architecture, semantics, metadata, lineage]
related: [ecl-framework, contextualize-pipeline, context-store, early-binding-vs-late-binding, data-contract-platform, embedded-metadata]
sources: ["Data Engineering After AI.md"]
---
# Context Propagation

**Context propagation** is the architectural principle in the [[ECL-framework]] that describes how semantic context travels through the data infrastructure without being lost. The key insight is that context does not travel *through* the data pipeline — it travels *alongside* it, as metadata, lineage records, and contract provenance.

## The Relay Model

The conventional mental model (context travels through the pipeline) is wrong because context would be lost at every transformation step — this is precisely the Medallion erosion problem. The correct model is a **relay**:

1. **Early binding** stamps prescribed context at the point of origin — schema, field-level semantics, ownership, quality thresholds — as an executable contract living in metadata, not column values
2. **Lineage tooling** propagates this through Bronze, Silver, and Gold layers, maintaining a record of transformations applied and the contract that governed the data at each stage
3. The [[contextualize-pipeline]] reads that lineage as part of its inference process — understanding not just what a field looks like today, but also the history of how it arrived
4. Validated inferences land in the [[context-store]], which becomes the relay's destination

## The Git Analogy

A file can be modified heavily across dozens of commits — refactored, renamed, moved, rewritten — but the context of how it got there is never lost, because it lives in the commit history, not in the file itself.

- The Gold layer is the latest commit
- The lineage graph is the git log
- The Context Store is the understanding built by reading that log systematically

## Implications

This reframe changes what data engineers are responsible for building:
- Transformations are increasingly automatable
- Metadata infrastructure, lineage graph, Contextualize pipeline, and Context Store require sustained human judgment