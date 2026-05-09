---
type: concept
title: Write-Audit-Publish (WAP) Pattern
created: 2026-05-22
updated: 2026-05-07
tags: [ci-cd, data-quality, workflow, versioning, data-lakehouse, apache-iceberg, validation, design-pattern, iceberg, data-engineering]
related: ["apache-iceberg", "data-quality-dimensions", "kestra", "iceberg-table-versioning", "data-lakehouse-versioning-strategies", "data-lakehouse", "data-contract-platform", "iceberg-cherry-pick-snapshot", "shift-left-data-quality", "data-quality-certification-vs-usability-certification", "WAP Pattern", "write-audit-publish-pattern"]
sources: ["Chill Your Data with Iceberg Write Audit Publish.md", "data-lakehouse-versioning-nessie-vs-iceberg-vs-lakefs.md", "WAP Pattern.md"]
---
# Write-Audit-Publish (WAP) Pattern

The **Write-Audit-Publish (WAP)** pattern is a data validation workflow that ensures only high-quality, validated data reaches production environments. It is a three-stage data quality design pattern that enforces validation before data reaches production consumers, and is a practical implementation of [[shift-left-data-quality]] and [[data-quality-certification-vs-usability-certification]]. Enabled by Apache Iceberg's branching capabilities, it isolates write operations to an audit branch, validates the data independently, and then atomically promotes it to the main branch only after passing all quality checks. This prevents the "broken pipeline" syndrome where corrupted or incomplete data becomes immediately visible to downstream consumers.

## How It Works

The WAP pattern operates in three conceptual stages:

1. **Write** – New data is written to an isolated environment, such as a temporary table or, in Iceberg, a dedicated **audit branch**. The production state remains untouched during this phase.
2. **Audit** – The staged data undergoes rigorous quality checks, including completeness, uniqueness, schema integrity, and business logic validation.
3. **Publish** – Once the audit passes, the data is atomically committed to the production environment. In Iceberg, this is a metadata-only operation: the main branch is fast-forwarded to the audit branch's head, or the validated snapshot is cherry-picked onto the main branch.

## Iceberg Implementation

Apache Iceberg provides native support for WAP through its branching and snapshot management capabilities. The general workflow involves:

1. **Enable WAP** – Set the table property `write.wap.enabled=true` on the target Iceberg table.
2. **Create an Audit Branch** – Create a branch from a known-good snapshot, optionally with a retention period (e.g., `RETAIN 7 DAYS`).
3. **Write to the Audit Branch** – Direct write operations to the audit branch using a session configuration (e.g., `spark.wap.branch='audit-branch'`).
4. **Validate** – Run data quality checks (completeness, uniqueness, schema, business rules) against the audit branch.
5. **Publish** – If validation succeeds, promote the branch to `main`. Two mechanisms are available:
   - **Fast-forward**: Executes `fast_forward` to move the `main` branch pointer to the audit branch's head. This merges the entire branch history.
   - **Cherry-pick snapshot**: Uses `cherry_pick_snapshot` to atomically apply only the validated snapshot(s) to `main`, allowing selective publication.
6. **Cleanup** – The audit branch is automatically removed when its retention policy expires, or can be dropped manually. This prevents metadata bloat.

### Example (SparkSQL using Fast-Forward)

```sql
ALTER TABLE prod.db.table SET TBLPROPERTIES ('write.wap.enabled'='true');
ALTER TABLE prod.db.table CREATE BRANCH `audit-branch` AS OF VERSION 3 RETAIN 7 DAYS;
SET spark.wap.branch = 'audit-branch';
INSERT INTO prod.db.table VALUES (3, 'c');
-- Validate data on audit-branch
CALL catalog_name.system.fast_forward('prod.db.table', 'main', 'audit-branch');
```

For cherry-pick, the analogous call would be `CALL catalog_name.system.cherry_pick_snapshot('prod.db.table', 'main', <snapshot-id>)`.

## Benefits and Challenges

### Benefits
- **Zero downtime** – Production remains untouched during the write and audit phases.
- **Safe validation** – Invalid data is never exposed to production consumers.
- **Isolation** – Validation runs on a separate branch without affecting main table consumers.
- **Atomicity** – Publishing is an atomic operation (via fast-forward or cherry-pick), avoiding partial updates.
- **Rollback simplicity** – Failed validations require only dropping a branch, not complex rollback procedures.
- **Reduced storage cost** – Avoids massive UAT table clones; Iceberg branching uses metadata-only operations. As demonstrated by Expedia Group, this approach can reduce release costs by up to 99%.
- **Automation** – Can be integrated into CI/CD pipelines for data, using orchestration tools like Apache Airflow, Dagster, or [[kestra]] for automated quality gates.
- **Improved trust** – Downstream users only see data that has passed all quality gates.
- **Retention** – Audit branches are automatically cleaned up via retention policies.

### Challenges
- **Metadata management** – Excessive branching and tagging can lead to "metadata bloat."
- **Lifecycle governance** – Requires automated processes (e.g., via [[kestra]]) to prune or expire old branches and tags.
- **Complexity** – Introduces the need for managing branch naming conventions and lineage.

## Open Questions

- What rollback strategies are needed when audit fails mid-pipeline?
- How does WAP interact with dbt's testing framework and CI/CD patterns?
- Is WAP suitable for streaming data, or only batch workloads?
- What are the performance costs of Iceberg branching for very large tables?

## See Also

- [[apache-iceberg]]
- [[data-quality-dimensions]]
- [[kestra]]
- [[iceberg-table-versioning]] – Iceberg's branching and tagging as the foundation for WAP
- [[data-lakehouse-versioning-strategies]] – Comparative framework for versioning approaches
- [[data-lakehouse]] – Core architecture where WAP is applied
- [[data-contract-platform]] – WAP can enforce data contracts before publishing
- [[iceberg-cherry-pick-snapshot]] – Alternative publication method
- [[shift-left-data-quality]] – WAP moves quality checks earlier in the pipeline
- [[data-quality-certification-vs-usability-certification]] – WAP provides a certification gate before production
- [[write-audit-publish-pattern]] – This page (self-reference for index linking)