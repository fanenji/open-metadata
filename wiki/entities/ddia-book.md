---
type: entity
title: "DDIA (Designing Data-Intensive Applications)"
created: 2026-04-29
updated: 2026-04-29
tags: [book, distributed-systems, data-systems]
related: [martin-kleppmann, distributed-systems-fundamentals, cloud-native-architecture-paradigm, formal-verification]
sources: ["Designing Data-intensive Applications with Martin Kleppmann-SUMMARY.md"]
---
# DDIA (Designing Data-Intensive Applications)

*Designing Data-Intensive Applications* by [[Martin Kleppmann]] (first edition 2017, second edition 2026 with co-author Chris Riccomini). Published by O'Reilly.

## Structure

Three parts:
1. **Foundational Data Systems**: Storage engines, encoding, replication, partitioning.
2. **Distributed Data**: Transactions, consistency, consensus, the trouble with distributed systems.
3. **Derived Data**: Batch processing, stream processing, the future of data systems.

## Second Edition Changes

- **Cloud-native architecture**: Replication now happens at the object store layer (S3), not the database layer. This paradigm shift is woven throughout the book.
- **New topics**: Vector indexes, DataFrames, broader coverage of cloud-native and managed services.
- **Removed**: Detailed MapReduce coverage (kept only as teaching tool); replaced by Spark and Flink.
- **Ethics**: Expanded from a section to a full chapter.

## Key Themes

- Reliability, Scalability, Maintainability as core qualities.
- Distributed system failures are empirical reality, not paranoia.
- Understanding internals is a superpower even with managed services.
- Formal verification will become more important with AI-generated code.