---
type: concept
title: dbt Minimum Model Standards
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, governance, data-quality, testing]
related: [dbt-data-contract-implementation, data-contract-observability, dbt-testing-patterns, dbt-runbooks, abhishek-2025-running-dbt-real-world]
sources: ["Running dbt in the Real World Cost Control, Governance, and Team Practices at Scale.md"]
---
# dbt Minimum Model Standards

Codified rules for tests, contracts, and documentation that all production-facing dbt models must meet. These standards turn governance into something checkable in code review and CI, rather than vague aspirations.

## Standard for Production-Facing Models

**Tests (at minimum):**
- `not_null` and `unique` tests on keys.
- Relationship tests on critical foreign keys.

**Contracts:**
- Enforced on all public/gold models (dim/fact tables used by many downstream tools).

**Documentation:**
- Model and key column descriptions kept in sync before merge.

## Example Enforceable Rule

"Any model tagged `public` must:
- Have `contract.enforced: true`.
- Have tests on primary keys and critical relationships.
- Have at least one paragraph of description explaining business meaning."

## Relationship to Existing Wiki

This concept extends [[dbt-data-contract-implementation]] by adding the governance layer of minimum standards. It connects to [[data-contract-observability]] for monitoring compliance and [[dbt-testing-patterns]] for implementation.