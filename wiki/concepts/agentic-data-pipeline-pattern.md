---
type: concept
title: Agentic Data Pipeline Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [agentic-ai, pipeline-pattern, data-architecture, automation]
related: [semantic-layer-generator, forward-deployed-engineering-data, text2sql-patterns, data-product-definition]
sources: ["the-semantic-layer-generatorwhen-agentic-ai-meets-data-architecture.md"]
---
# Agentic Data Pipeline Pattern

The **Agentic Data Pipeline Pattern** is a reusable architectural pattern for automating complex data engineering workflows using a multi-phase autonomous pipeline that interleaves LLM reasoning with deterministic optimization steps. It was introduced by [[Nayan Paul]] in the context of the [[semantic-layer-generator]].

## The 5-Phase Pipeline

1. **Analyze** — LLM reasons about the input (schema, relationships, semantics) to build a comprehensive understanding.
2. **Optimize** — Deterministic algorithms (e.g., pure Python set logic) prune irrelevant elements based on provided requirements.
3. **Design** — LLM designs the output structure (wide tables, schemas, join paths) based on the optimized input.
4. **Generate** — LLM produces production-ready artifacts (DDL, typed schemas, configuration files).
5. **Report** — LLM generates human-readable documentation, coverage matrices, and audit trails.

## Key Design Principle: Hybrid Deterministic-Probabilistic

The critical insight is interleaving deterministic and probabilistic steps:
- **LLM reasoning** (phases 1, 3, 4, 5) provides semantic understanding, creativity, and natural language generation.
- **Deterministic logic** (phase 2) provides auditable precision where correctness is critical (e.g., pruning irrelevant tables).

This hybrid approach ensures the pipeline gets the benefits of language models where they matter while maintaining rigor where precision is required.

## Applicability

The pattern applies to any "translation layer" problem in software engineering:
- ETL pipeline design
- API schema generation
- Test suite scaffolding
- Data model transformation
- Report generation

## Connections

- The [[semantic-layer-generator]] is the canonical implementation of this pattern.
- The pattern embodies the [[forward-deployed-engineering-data]] philosophy.
- The output artifacts (wide tables) are [[data-product-definition|data products]].
- The pattern strengthens [[text2sql-patterns]] by producing flat schemas optimized for LLM SQL generation.