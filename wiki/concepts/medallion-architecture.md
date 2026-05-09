---
type: concept
title: Medallion Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, architecture, data-lakehouse, data-quality]
related: [data-lakehouse, data-quality-certification-vs-usability-certification, data-quality-dimensions, data-mesh, semantic-layer]
sources: ["if-you-understand-these-5-data-engineering-terms-youre-ahead-of-90-of-the.md"]
---
# Medallion Architecture

The **Medallion Architecture** is a data organization pattern for data lakehouses that structures data into three quality tiers: Bronze (raw), Silver (cleaned), and Gold (aggregated/business-ready). It brings auditability, debugging clarity, and governance to what would otherwise be a chaotic data swamp.

## The Three Tiers

### Bronze
- Raw, unfiltered data exactly as it arrived from source systems.
- Preserves the original format (JSON, CSV, Parquet) for replay and audit.
- If the source system breaks, Bronze data enables full replay.

### Silver
- Cleaned, filtered, and typed data.
- Deduplicated, standardized, and validated.
- Schema is enforced and data types are consistent.

### Gold
- Business-level aggregations and pre-joined star schemas.
- Optimized for BI tools and executive queries.
- Metrics are pre-calculated and business logic is applied.

## Why It Matters

- **Debugging:** If a metric is wrong, check Gold first. If logic is wrong there, fix it. If Gold is fine, check Silver for missing data. No need to untangle 500-line SQL queries.
- **Auditability:** Bronze preserves the original source of truth. Any transformation can be replayed from scratch.
- **Governance:** Different access controls can be applied at each tier (e.g., raw PII in Bronze, anonymized in Silver, aggregated in Gold).

## Connection to Existing Wiki

- [[data-lakehouse]] — Medallion Architecture is the most common organizational pattern for lakehouses.
- [[data-quality-certification-vs-usability-certification]] — The Bronze/Silver/Gold tiers map naturally to certification levels: Bronze = raw, Silver = quality-certified, Gold = usability-certified.
- [[data-quality-dimensions]] — Each tier enforces progressively stricter quality dimensions.
- [[data-mesh]] — Medallion Architecture can be applied within each data domain in a mesh architecture.
