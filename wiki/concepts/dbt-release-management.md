type: concept
title: dbt Release Management
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, release-management, ci-cd, git]
related: [indirect-promotion, hierarchical-promotion, dbt-git-branching-strategies, dbt-cloud-environments, continuous-delivery]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# dbt Release Management

**dbt Release Management** refers to the process of batching approved changes from a middle branch (e.g., `qa`) and promoting them to `main` as a single release. This is a key practice in [[indirect-promotion]] and [[hierarchical-promotion]] strategies.

## Release Workflow

1. A **release manager** opens a pull request from the middle branch (`qa`) targeting `main`.
2. The release PR is reviewed by QA specialists, SMEs, or stakeholders.
3. A release-specific PR template is used (e.g., [dbt Labs release PR template](https://github.com/dbt-labs/dbt-proserv/blob/main/.github/release_pull_request_template.md)).
4. After approval, the middle branch is merged to `main`.
5. The `main` branch is deployed to production.

## Key Concepts

- **Continuous Delivery:** Releases enable batched changes to production, as opposed to the continuous deployment model of [[direct-promotion]].
- **Release Manager:** A person or group responsible for managing the release cycle, validation status, and merge process.
- **Release CI:** A dedicated CI job that tests the release PR before merge, ensuring the combined changes work together.

## Challenges

- Changes can be slower to reach production due to the release process.
- Valid changes can get stuck behind changes that aren't ready.
- Requires dedicated ownership and project management.
- Additional compute for release CI jobs.