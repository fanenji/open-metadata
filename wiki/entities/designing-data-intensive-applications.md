---
type: entity
title: "Designing Data-Intensive Applications (DDIA)"
created: 2026-04-29
updated: 2026-04-29
tags: [book, distributed-systems, data-systems]
related: [martin-kleppmann, chris-riccomini, cloud-native-data-systems, distributed-systems-failure-modes, kafka]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Designing Data-Intensive Applications (DDIA)

*Designing Data-Intensive Applications* (DDIA) is a foundational book on modern distributed systems and data-intensive application design, written by [[martin-kleppmann]]. The first edition was published in 2017 by O'Reilly Media. The second edition, co-authored with [[chris-riccomini]], is forthcoming.

## Structure

The book is organized into three parts:

1. **Foundations of Data Systems** — Storage engines (B-trees, LSM trees), encoding, and the basics of data models.
2. **Distributed Data** — Replication, partitioning/sharding, transactions, consistency, consensus, and the troubles with distributed systems.
3. **Derived Data** — Batch processing (MapReduce), stream processing (Kafka, Samza), and the unification of batch and stream.

## Core Framework

The book's tagline is "The big ideas behind reliable, scalable, and maintainable systems." These three pillars are:

- **Reliability** — Fault tolerance; the system continues working despite failures (network, node crashes).
- **Scalability** — Mechanisms for dealing with changes in load, including both scaling up and scaling down (serverless).
- **Maintainability** — The third pillar, often overlooked, covering operability, simplicity, and evolvability.

## Second Edition Changes

- **Cloud-native systems architecture** — Building on object stores as foundational abstraction, integrated throughout the narrative.
- **Removed MapReduce** — Macro produce (MapReduce) is "dead" and removed from the updated version.
- **Added AI/vector indexes** — Systems in support of AI like vector indexes.
- **Formal verification** — Increased coverage due to AI-generated code concerns.
- **Multi-region/multi-cloud** — Geopolitical resilience considerations.

## Influence

DDIA is widely considered the go-to reference for anyone building large backend systems. It is used for internal training at companies like LinkedIn and is frequently cited in industry discussions about distributed systems trade-offs.