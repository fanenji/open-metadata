---
type: concept
title: Data Quality Dimensions
created: 2026-04-04
updated: 2026-05-07
tags: ["data-governance", "metrics", "data-quality", "framework"]
related: ["ai-driven-data-quality", "data-governance", "data-quality-score", "shift-left-data-quality", "engineering-led-data-quality", "data-observability-definition", "environmental-data-quality-hierarchy", "great-expectations-for-data-contracts", "dbt-testing-patterns"]
sources: ["Automate Data Quality Checks with AI Agents.md", "Defining Data Quality The Foundation of Modern Data Architecture.md"]
---
# Data Quality Dimensions

Data Quality (DQ) in modern data architectures is defined by a set of seven measurable dimensions. These dimensions provide a consistent vocabulary and criteria for assessing how well data meets the needs of its consumers, and serve as a framework for defining validation rules for both manual and [[ai-driven-data-quality|AI-driven quality checks]]. By measuring these dimensions, organizations can effectively monitor and govern their data assets.

## The Seven Dimensions

### Accuracy
How closely data reflects the real-world value or event it represents. At source systems, this involves input validation and business logic. At the data lake/warehouse, data should match the source with no corruption or transformation error. Cross-checking via DB links or data-sharing mechanisms is common. Accuracy also prevents “hallucinations” in AI models by ensuring data correctly reflects real-world entities or events.

### Completeness
Ensures all expected data is present — no missing rows, fields, or files. At source systems, required fields are enforced. At the warehouse, checks for missing partitions, truncated rows, or nulls in key columns are performed. Record counts between source and raw zone should match. Examples include identifying missing values or null fields.

### Consistency
Ensures no contradictions exist within or across datasets. At source systems, referential integrity and standardized rules apply. At the warehouse, consistent values and metrics across reports and systems are required, including timezone, currency, and data type standardization. For example, `user_id` must be formatted identically across all systems.

### Uniqueness
Ensures no duplicate records or keys exist where they shouldn't. At source systems, unique key constraints are enforced. At the warehouse, deduplication, identity resolution, and master data management for dimensions are applied.

### Integrity
Maintains correct relationships between entities (facts and dimensions). At source systems, referential integrity is enforced. At the warehouse, validations ensure fact-to-dimension relationships remain intact.

### Validity
Ensures data values conform to defined formats, domains, and business rules. Examples include email format (`user@example.com`), date format (`YYYY-MM-DD`), and logical constraints (`start_date < end_date`). Regular expressions for emails and range checks for ages are common. Ideally validated upstream; invalid patterns downstream indicate weak source hygiene.

### Availability (Timeliness)
Ensures data is delivered on time and per SLA. Even with correct values, stale data breaks trust. At source systems, data is published according to SLA. At the warehouse, ingestion timeliness and pipeline latency affecting data freshness are monitored. This dimension captures the degree to which data is up‑to‑date and available when needed for decision‑making or real‑time inference.

## Role in Governance and Relationship to Other Frameworks

Defining these seven dimensions is a prerequisite for establishing **Data Ownership** and **Quality KPIs** within a [[data-governance]] framework.

These DQ dimensions complement the [[data-observability-definition]]'s seven observability dimensions (freshness, security, redundancy, discrepancy, documentation, quality, lineage). While observability focuses on the operational health of pipelines, DQ dimensions focus on the intrinsic properties of the data itself.

The framework also aligns with the [[environmental-data-quality-hierarchy]]'s tiered validation approach (VAL → VAL_COR → CERT) and supports the shift‑left enforcement strategy documented in [[shift-left-data-quality]].

## Note on Data Drift

Data distribution stability (data drift) is considered an inherent property of the data for ML workloads, not a criterion for assessing data quality. Changes in distribution can degrade model performance even if data is accurate and complete.