---
type: concept
title: Data Contract Versioning Strategy
created: 2026-04-04
updated: 2026-04-04
tags: [data-contracts, versioning, schema-evolution, governance]
related: [data-contract-platform, great-expectations-for-data-contracts, delta-lake-schema-enforcement]
sources: ["Data Contract Enforcement Ensuring Reliability in Distributed Pipelines.md"]
---
# Data Contract Versioning Strategy

A Git-based approach to managing the evolution of data contracts over time. Contracts are versioned with semantic versioning, include changelogs documenting additions and deprecations, and specify migration strategies for backward compatibility.

## Contract Version Structure

```yaml
version: 2.1
changelog:
  - added column "session_id" for tracking multi-event sequences
  - deprecated "event_type" values: "click-through"
migration_strategy: backward_compatible
```

## Key Practices

- **Git-based versioning**: Contracts live in a repository alongside pipeline code, enabling pull request workflows for schema changes.
- **Changelog documentation**: Every version change includes a human-readable changelog explaining what changed and why.
- **Migration strategy declaration**: Each contract specifies whether the change is backward compatible, allowing consumers to plan upgrades.
- **CI/CD validation**: Pull requests that modify contracts trigger automated validation to ensure changes don't break dependent systems.

## Relationship to Data Contract Platform

This strategy operationalizes the evolution aspect of [[data-contract-platform]]. Without controlled versioning, contracts become stale and lose their value as the source of truth.
