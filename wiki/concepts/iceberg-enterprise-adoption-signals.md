---
type: concept
title: Iceberg Enterprise Adoption Signals
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, enterprise, adoption, case-studies]
related: [apache-iceberg, apple, expedia-group, stripe, netflix, iceberg-vendor-standardization]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Iceberg Enterprise Adoption Signals

Credible signals that enterprises are adopting Apache Iceberg to solve common constraints, not merely copying Netflix's architecture.

## Enterprise Case Studies

- **Apple**: Iceberg use "all over the place," spanning hundreds of MB to many PB, with investments in maintenance procedures and row-level operations for regulatory compliance
- **Expedia Group**: Data lake on S3 backed by Hive Metastore created complexity; Iceberg adopted as an alternative providing ACID transactions, time travel, and partition spec evolution
- **Stripe**: Extensive Iceberg table usage replacing legacy Hive tables, with operational friction around reading Iceberg metadata from S3

## Key Takeaway

These are not "copy Netflix" stories. They are "we hit the same lake pain points at scale and needed a table layer" stories. The common pattern is organizations encountering real operational and financial pain from traditional Hive-style data lakes.
