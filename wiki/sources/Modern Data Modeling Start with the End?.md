---
type: source
title: "Modern Data Modeling: Start with the End?"
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, data-modeling, agile, analytics-engineering]
related: [bottom-up-data-modeling, dbt-project-folder-structure, agile-analytics-engineering, dbt-project-scaffolding, dbt-schema-synchronization]
sources: ["Modern Data Modeling Start with the End?.md"]
authors: [Brice Luu]
year: 2022
url: "https://www.adventofdata.com/modern-data-modeling-start-with-the-end/"
venue: "Advent of Data"
---
# Modern Data Modeling: Start with the End?

A practical guide to structuring dbt projects using a bottom-up, iterative approach. The author argues against top-down dimensional modeling, advocating instead for starting with fast, dirty queries for immediate value, then progressively refactoring into a structured **Base → Core → Usecases** architecture.

## Key Arguments

- **Start fast, refactor later**: Deliver value quickly with raw queries, then progressively extract repeated logic.
- **Rule of three**: Extract repeated logic into separate models after 3+ occurrences.
- **Fan-out pattern**: Core objects feed multiple usecase variations for different stakeholders.
- **Agile analytics engineering**: Iterative, value-first approach to data modeling.

## Project Structure

The recommended three-layer folder structure under `models/`:

1. **`base/`** — Explicit column selection from raw sources, no joins or aggregations.
2. **`core/`** — Central business logic, dimensional models or One Big Tables.
3. **`usecases/`** — Stakeholder-specific variations fanning out from core objects.

## Key Techniques

- `generate_schema_name` macro for environment-aware schema mapping
- `dbt_utils` package for Jinja templating patterns
- Source declarations via `_sources.yml` files
- Progressive addition of descriptions and tests

## Connections

This source provides a concrete methodology for [[dbt-project-scaffolding]] and extends [[dbt-testing-patterns]] by adding context on when to add tests progressively. The usecases-per-stakeholder pattern aligns with [[data-mesh]] domain ownership principles.