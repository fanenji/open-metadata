---
type: concept
title: Bottom-Up Data Modeling
created: 2026-04-07
updated: 2026-04-07
tags: [data-modeling, dbt, methodology, agile]
related: [dbt-project-folder-structure, agile-analytics-engineering, dbt-project-scaffolding, data-mesh]
sources: ["Modern Data Modeling Start with the End?.md"]
---
# Bottom-Up Data Modeling

A data modeling methodology that starts with fast, raw queries for immediate business value and progressively refactors them into a structured architecture. This contrasts with traditional top-down approaches like [[dimensional-modeling]] that require significant upfront design time.

## Core Principles

1. **Start small, start fast**: Deliver insights quickly with direct queries, proving value to the organization.
2. **Progressive refactoring**: Extract repeated logic into separate models as patterns emerge.
3. **Rule of three**: Isolate logic into its own model only after it has been repeated 3+ times.
4. **Fan-out from core**: Build central business objects, then create stakeholder-specific variations.

## Three-Layer Architecture

The methodology organizes models into three layers:

- **Base layer**: Explicit column selection from raw sources, no joins or grain changes.
- **Core layer**: Central business logic, dimensional models or One Big Tables at the object grain.
- **Usecases layer**: Stakeholder-specific variations that select from core objects.

## Relationship to Other Concepts

- Provides a concrete implementation pattern for [[dbt-project-scaffolding]]
- Extends [[dbt-testing-patterns]] by suggesting progressive test addition
- Aligns with [[data-mesh]] domain ownership through usecases-per-stakeholder organization
- Contrasts with top-down [[dimensional-modeling]] approaches