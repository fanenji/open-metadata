---
type: concept
title: CI/CD for Data Pipelines
created: 2026-04-04
updated: 2026-04-04
tags: [CI-CD, data-pipelines, data-governance, data-contracts]
related: [data-contract, YAML-data-contract-format, data-contract-versioning-strategy, data-contract-platform]
sources: ["Data Contracts Implementation Guide.md"]
---
# CI/CD for Data Pipelines

CI/CD for data pipelines is the application of software engineering continuous integration and continuous deployment practices to data workflows. It is the core enforcement mechanism for [[data-contract]]s, as described in [[Jatin Solanki]]'s implementation guide.

## Enforcement Workflow

1. **Git Branching and Version Control**: A `main` branch represents the stable version of the data contract. Developers create feature branches for proposed changes.
2. **Code Reviews and Merge Requests**: Developers submit pull requests (PRs) or merge requests (MRs) for review.
3. **Continuous Integration (CI) Pipeline**: When a PR is created, a CI pipeline is triggered that performs:
   - YAML Linting: Ensures syntactic correctness
   - Schema Validation: Uses tools like `yamale` or `jsonschema` to validate the YAML against the defined schema
   - Unit Tests: Verifies that logic depending on the data contract is not broken
4. **Documentation and Change Log**: PR descriptions document changes; a change log is updated.
5. **Merging and Deployment**: Once CI checks pass and the PR is approved, it is merged into `main` and deployed.
6. **Access Control and Security**: Merge access to `main` is restricted to authorized personnel.

## Relationship to Data Contracts

The [[YAML-data-contract-format]] file is the artifact that flows through this CI/CD pipeline. Any changes to the data contract are automatically validated, ensuring that data integrity and reliability are maintained.