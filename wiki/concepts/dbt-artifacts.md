---
type: concept
title: dbt Artifacts
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, metadata, json, artifacts]
related: [dbt-observability-implementation, on-run-end-hook, elementary-dbt-package, dbt-jinja-variables]
sources: ["dbt observability 101 How to monitor dbt run and test results.md"]
---
# dbt Artifacts

JSON files that dbt produces after every command execution, containing run results and project metadata. They include information about models, tests, sources, seeds, snapshots, exposures, and analyses.

## Contents

- **Run results metadata:** execution status, compilation time, run time, error messages, rows affected.
- **Project metadata:** connections between models, tags, owners, connections between tests and models.

## Challenges

The article "dbt observability 101" identifies several difficulties with processing artifacts:

- **Nested structure:** Objects contain dictionaries within dictionaries, requiring complex flattening logic.
- **Poor documentation:** The artifact schema is not well documented, making parsing error-prone.
- **Version dependency:** Artifact structure changes between dbt versions, requiring maintenance of parsing code.
- **Orchestration overhead:** A separate process must run after every dbt command and have access to the artifact file location.

## Alternative Approach

The [[dbt-observability-implementation]] pattern avoids artifacts entirely by using Jinja variables (`results`, `graph`, `invocation_id`) within an [[on-run-end-hook]] to log metadata directly to the warehouse. However, this approach captures less comprehensive metadata than full artifact processing.

The [[elementary-dbt-package]] and Brooklyn Data's `dbt_artifacts` package both process artifacts for richer observability, creating an internal tension with the article's critique of artifact complexity.

## Related

- [[dbt-observability-implementation]] — The Jinja-based alternative to artifact processing.
- [[on-run-end-hook]] — The mechanism used to access result metadata without artifacts.
- [[elementary-dbt-package]] — A package that processes artifacts for comprehensive observability.