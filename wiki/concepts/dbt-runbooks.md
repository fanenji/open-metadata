---
type: concept
title: dbt Runbooks
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, incident-response, operations, reliability]
related: [dbt-observability-implementation, dbt-cost-control, dbt-minimum-model-standards, abhishek-2025-running-dbt-real-world]
sources: ["Running dbt in the Real World Cost Control, Governance, and Team Practices at Scale.md"]
---
# dbt Runbooks

Documented, step-by-step guides for responding to dbt-related incidents. Runbooks prevent each incident from being improvised from scratch and are a key indicator of operational maturity.

## Example Runbooks

### "Critical prod job failed"
1. Where to check (dbt Cloud logs, warehouse).
2. How to assess impact (lineage, exposures).
3. Who to page (on-call data/analytics owner).
4. Temporary mitigations and follow-up actions.

### "Source schema changed"
1. How to discover what models are impacted.
2. Process for coordinating with source team.
3. Timeline and communication plan for consumers.

## Relationship to Existing Wiki

Runbooks complement [[dbt-observability-implementation]] by providing the incident response layer. They are part of the operational maturity framework alongside [[dbt-cost-control]] and [[dbt-minimum-model-standards]].