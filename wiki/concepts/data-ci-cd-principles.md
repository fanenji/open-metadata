---
type: concept
title: Data CI/CD Principles
created: 2026-04-04
updated: 2026-04-04
tags: [ci-cd, data-delivery, accelerate, framework]
related: [data-release-pipeline, deployment-critical-vs-monitoring-tests, CI-CD-for-data-pipelines, dbt-slim-ci, data-contract-observability, data-mesh]
sources: ["How CI-CD should look for Data teams.md"]
---
# Data CI/CD Principles

A framework for CI/CD adapted specifically for data teams, based on the 24 characteristics from the book *Accelerate* but extended and modified for the unique responsibilities of data teams. The core premise is that data teams ship *data objects* (files/tables), not just code, which fundamentally changes CI/CD requirements.

## Key Principles

### Continuous Delivery (adapted for data)
1. **Store raw data in partitions and version control the code** that materializes data.
2. **Automate deployment** via a [[data-release-pipeline]] (transformation + orchestration + observability).
3. **Implement continuous integration**: code triggers ephemeral materialization of data assets for rapid testing.
4. **Use trunk-based development**: fewer than 3 active branches recommended for SQL repositories.
5. **Implement test automation efficiently**: avoid running all tests on full production replicas.
6. **Clone data into production**: staging data that passes quality checks should be flat-cloned into production.
7. **Shift left on security**: assess security requirements before building infrastructure.
8. **Implement continuous delivery**: data should be in a deployable state throughout its lifecycle.
8b. **Ensure state is available**: downstream consumers need to infer the state of upstream data (job status, quality check results).

### Architecture Capabilities
- **Build the architecture for the job**: loosely coupled or tightly coupled depending on circumstances.
- **Architect for empowered teams**: let data teams choose tools subject to cost.
- **Model data using a framework** (e.g., medallion, facts and measures, datavault).
- **Model data sparingly**: fewer models improve cost and simplicity.

### Hierarchy of Data Needs
A prioritization framework for tooling and process decisions:
1. **Security** — non-negotiable business obligation.
2. **Functionality** — tooling must achieve the desired outcome.
3. **Reliability** — data must be reliably deployed to production.
4. **Cost and time to maintain** — higher priority than in software.
5. **Flexibility** — important but subordinate to present needs.
6. **Simplicity** — the "data nirvana" achieved after other needs are met.

## Relationship to Existing Wiki
This framework extends the existing [[CI-CD-for-data-pipelines]] page with a more detailed, principle-based structure. It connects to [[data-contract-observability]] through the "state availability" concept, and to [[dbt-slim-ci]] through the emphasis on efficient test automation. The "flat cloning" approach contrasts with the more granular versioning strategies documented in [[nessie-catalog-versioning]] and [[iceberg-table-versioning]].

## Status
Opinion-based framework from a vendor-adjacent source. Lacks empirical validation but provides a useful heuristic for data teams designing CI/CD processes.