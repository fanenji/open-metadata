---
type: source
title: "Data Engineering After AI"
created: 2026-03-14
updated: 2026-03-14
tags: [data-engineering, ai, ecl, context, data-contracts, architecture]
related: [ananth-packkildurai, ecl-framework, contextualize-pipeline, context-store, context-architect-role, early-binding-vs-late-binding, context-propagation, data-contract-platform, data-contract-versioning-strategy, data-product-definition]
sources: ["Data Engineering After AI.md"]
authors: [Ananth Packkildurai]
year: 2026
url: "https://www.dataengineeringweekly.com/p/data-engineering-after-ai"
venue: "Data Engineering Weekly"
---
# Data Engineering After AI

**Author:** [[Ananth Packkildurai]]
**Published:** 2026-02-24
**Source:** [Data Engineering Weekly](https://www.dataengineeringweekly.com/p/data-engineering-after-ai)

## Summary

This article argues that the ETL (Extract, Transform, Load) framework is ending as AI becomes competent at generating transformation code. The author proposes a new framework called **ECL (Extract, Contextualize, Link)** that reorients data engineering from data movement to data meaning. The core innovation is the **Contextualize pipeline** — a separate, agentic pipeline that infers, validates, and stores semantic context alongside data infrastructure — and the **Context Store**, a new infrastructure component for versioned, queryable semantic artifacts. The article introduces the concepts of **early binding** (executable contracts at the source) and **late binding** (deferred definition via the Contextualize pipeline), with the **accountability boundary** as the decision criterion for choosing between them. The data engineer role evolves into a **Context Architect** who owns the architecture of meaning, contracts, lineage, and context infrastructure.

## Key Concepts Introduced

- [[ECL-framework]] — Extract, Contextualize, Link as replacement for ETL
- [[contextualize-pipeline]] — Agentic pipeline for semantic inference and validation
- [[context-store]] — Versioned, queryable store of semantic artifacts
- [[context-architect-role]] — Evolution of data engineer to architect of meaning
- [[early-binding-vs-late-binding]] — Decision framework for prescribed vs. discovered context
- [[context-propagation]] — Context travels alongside pipeline via metadata/lineage

## Key Arguments

1. ETL is ending because AI can generate transformation code competently
2. ECL replaces ETL, focusing on meaning rather than movement
3. Early binding (contracts) alone is insufficient — context erodes across Medallion transformations
4. A Contextualize pipeline is necessary to infer, validate, and store semantic context
5. The Context Store is new infrastructure for versioned semantic artifacts
6. The data engineer becomes a Context Architect

## Evidence Strength

**Weak to moderate.** The article is a conceptual framework proposal, not an empirical study. Arguments are logical but untested at scale. The author acknowledges tooling is immature and patterns are still emerging.

## Connections

- Strengthens [[data-contract-platform]] — contracts as executable infrastructure
- Strengthens [[data-catalog-critique]] — embedded context over separate catalogs
- Extends [[data-contract-versioning-strategy]] — versioned context artifacts
- Challenges [[data-contract-platform]] — argues contracts alone are insufficient