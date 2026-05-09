---
type: concept
title: Agile Analytics Engineering
created: 2026-04-07
updated: 2026-04-07
tags: [agile, analytics-engineering, methodology, dbt]
related: [bottom-up-data-modeling, dbt-project-folder-structure, data-mesh]
sources: ["Modern Data Modeling Start with the End?.md"]
---
# Agile Analytics Engineering

An iterative, value-first philosophy for data modeling that prioritizes delivering insights quickly over upfront design perfection. The approach is summarized as: "Be like water my friend."

## Core Cycle

1. **Start small but start fast** — Deliver immediate value with raw queries.
2. **Progressively regroup repetitions** — Extract repeated logic as patterns emerge.
3. **Only formalize once you have a good grasp** — Avoid premature abstraction.
4. **Rinse and repeat** — Continuously refine the architecture.

## Key Heuristics

- **Rule of three**: Don't extract logic until it has been repeated 3+ times.
- **Progressive testing**: Add descriptions and tests for the most important models first, expanding coverage over time.
- **Stakeholder-driven organization**: Structure usecases by department, enabling eventual domain ownership.

## Relationship to Other Concepts

This philosophy provides the "why" behind [[bottom-up-data-modeling]] and the [[dbt-project-folder-structure]]. It aligns with [[data-mesh]] principles by organizing usecases around domain ownership and treating data as a product for specific stakeholders.