---
type: concept
title: Schema Flatness Principle
created: 2026-05-07
updated: 2026-05-07
tags: [text2sql, schema-design, llm, data-architecture]
related: [text2sql-patterns, semantic-layer-generator, llm-sql-generation-evaluation]
sources: ["the-semantic-layer-generatorwhen-agentic-ai-meets-data-architecture.md"]
---
# Schema Flatness Principle

The **Schema Flatness Principle** states that flat schemas — denormalized, pre-joined wide tables with descriptive column names — dramatically improve LLM SQL generation accuracy and reduce hallucination compared to normalized schemas with complex join paths.

## Rationale

- Fewer tables reduce the search space for join path selection.
- Descriptive column names provide semantic cues that help LLMs map natural language questions to database columns.
- Pre-joined views eliminate the need for the LLM to reason about foreign key relationships at query time.
- Column-level definitions in the schema provide additional context for accurate SQL generation.

## Implications

- The [[semantic-layer-generator]] produces flat schemas as its primary output, explicitly designed to feed downstream Text2SQL tools.
- The principle suggests that organizations investing in Text2SQL should prioritize building a flat semantic layer before optimizing prompt engineering or model selection.
- The principle connects to [[llm-sql-generation-evaluation]] by providing a design heuristic for schema preparation.

## Connections

- Strengthens [[text2sql-patterns]] by adding a schema design dimension to the pipeline.
- The [[semantic-layer-generator]] operationalizes this principle by generating flat schemas from normalized inputs.
- The principle implicitly validates the wiki's emphasis on [[data-product-definition]] — well-designed data products are naturally flat and query-ready.