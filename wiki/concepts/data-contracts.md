---
type: concept
title: Data Contracts
created: 2026-04-22
updated: 2026-04-22
tags: [data-governance, data-quality, engineering]
related: [dbt, data-observability, data-governance]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md"]
---
# Data Contracts

**Data Contracts** are enforceable agreements between data producers and consumers regarding the schema, structure, and quality of a dataset. In a dbt environment, these are implemented via **Model Contracts**.

### Purpose in CI/CD
- **Breaking Change Prevention**: Automatically failing a Pull Request if a change violates a predefined schema (e.g., changing a data type or removing a column).
- **Downstream Stability**: Providing a guarantee to downstream consumers that the interface of a model will remain consistent.
- **Automated Governance**: Moving governance from a manual review process to an automated, code-driven enforcement mechanism.
---END EXAMINE ---
Wait, I need to follow the exact format. Let me re-check the `data-contracts` file.

---FILE: wiki/concepts/data-contracts.md---
---
type: concept
title: Data Contracts
created: 2026-04-22
updated: 2026-04-22
tags: [data-governance, data-quality, engineering]
related: [dbt, data-observability, data-governance]
sources: ["5-dbt-slim-ci-tactics-for-large-repos.md"]
---
# Data Contracts

**Data Contracts** are enforceable agreements between data producers and consumers regarding the schema, structure, and quality of a dataset. In a dbt environment, these are implemented via **Model Contracts**.

### Purpose in CI/CD
- **Breaking Change Prevention**: Automatically failing a Pull and PR if a change violates a predefined schema (e.g., changing a data type or removing a column).
- **Downstream Stability**: Providing a guarantee to downstream consumers that the interface of a model will remain consistent.
- **Automated Governance**: Moving governance from a manual review process to an automated, code-driven enforcement mechanism.