---
type: concept
title: dbt Docs
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, documentation, catalog]
related: [dbt-core, dbt-project-scaffolding, dbt-exposures]
sources: ["How to get started with dbt.md"]
---
# dbt Docs

dbt Docs is a built-in documentation feature of [[dbt Core]] that generates a lightweight data catalog as a static web page. Users add metadata (descriptions, tests, lineage) to models, sources, and other entities in YAML files. Running `dbt docs generate` compiles this metadata into a searchable HTML site, and `dbt docs serve` hosts it locally.

The generated documentation includes:
- Model descriptions and column-level documentation
- Lineage graphs showing model dependencies
- Test results and coverage
- Exposure definitions

dbt Docs provides a self-contained catalog without requiring external tools, though it is less feature-rich than dedicated catalog platforms like [[datahub]] or [[openmetadata]].