---
type: entity
title: Semantic Layer Generator
created: 2026-05-07
updated: 2026-05-07
tags: [agentic-ai, semantic-layer, data-architecture, tool]
related: [agentic-data-pipeline-pattern, forward-deployed-engineering-data, text2sql-patterns, data-product-definition, model-context-protocol, nayan-paul]
sources: ["the-semantic-layer-generatorwhen-agentic-ai-meets-data-architecture.md"]
---
# Semantic Layer Generator

The **Semantic Layer Generator** is an agentic AI system proposed by [[Nayan Paul]] that autonomously transforms normalized database schemas and business questions into optimized, production-ready wide-table views. It embodies the [[forward-deployed-engineering-data]] philosophy by working with existing schemas (plain JSON) and analytical questions, without requiring DSLs, YAML manifests, or new platforms.

## Architecture

The system uses a 5-phase autonomous pipeline (see [[agentic-data-pipeline-pattern]]):

1. **Analyze** — LLM reasons about schema semantics, foreign keys, and relationships.
2. **Optimize** — Pure Python set logic prunes tables that don't answer provided questions.
3. **Design** — LLM designs wide-table schemas based on optimized join paths.
4. **Generate** — LLM produces Snowflake-ready `CREATE OR REPLACE VIEW` DDL and typed output schema.
5. **Report** — LLM generates an HTML report with column-level documentation and question-coverage matrix.

## Key Features

- **Schema-native:** Works with plain JSON schema input — no DSL or YAML required.
- **Question-driven:** Every generated wide table is traceable to a specific business question.
- **Production-ready output:** Snowflake DDL, typed output schema for Text2SQL, and self-contained HTML report.
- **Hybrid pipeline:** Interleaves LLM reasoning (phases 1, 3, 4, 5) with deterministic Python set logic (phase 2) for auditable precision.

## Example

An HR database with 5 normalized tables (`EMPLOYEES`, `DEPARTMENTS`, `ROLES`, `SALARIES`, `LEAVE_REQUESTS`) and 5 analytical questions produced 4 wide tables with 100% question coverage in under 30 seconds.

## Limitations

- No documented support for schema evolution or versioning.
- No failure cases or production deployment data.
- Snowflake-specific DDL output partially contradicts the "schema-native" claim.
- No integration with data governance frameworks (data contracts, lineage tracking).

## Connections

- Provides a concrete use case for [[model-context-protocol]] as an integration layer.
- The generated wide tables are essentially [[data-product-definition|data products]].
- The output schema JSON could feed [[dbt-data-contract-implementation]] definitions.
- The "schema flatness principle" strengthens [[text2sql-patterns]].