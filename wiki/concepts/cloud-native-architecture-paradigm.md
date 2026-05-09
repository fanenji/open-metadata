---
type: concept
title: Cloud-Native Architecture Paradigm
created: 2026-04-29
updated: 2026-04-29
tags: [cloud-architecture, object-store, replication, data-lakehouse]
related: [distributed-systems-fundamentals, data-lakehouse, data-lakehouse-versioning-strategies, elt-pattern, ddia-book]
sources: ["Designing Data-intensive Applications with Martin Kleppmann-SUMMARY.md"]
---
# Cloud-Native Architecture Paradigm

The fundamental shift in data systems architecture identified by [[Martin Kleppmann]] in the second edition of *Designing Data-Intensive Applications*.

## The Shift

In the first edition, the implicit assumption was: each machine has local disks, the database writes there, and replication happens at the database level between machines. Today, this assumption is obsolete.

**Cloud-native architecture**: Systems are built on **object store** (S3 and similar) as the fundamental abstraction. Replication happens at the storage layer, not the database layer.

## Object Store vs Block Device

- **EBS**: Block device on cloud, still within the "local disk" abstraction.
- **Object store (S3)**: A completely new abstraction with different behaviors from a file system. Replication, durability, and availability are handled by the storage layer.

## Implications for Data Platform Architecture

- [[data-lakehouse]] designs benefit from object store as the foundation.
- [[data-lakehouse-versioning-strategies]] are affected by where replication occurs (storage layer vs database layer).
- The [[elt-pattern]] is naturally suited to cloud-native architectures.
- Managed services become more viable because the storage layer handles replication.

## Scaling Down

Cloud-native architecture also enables **scaling down**: serverless systems that cost pennies per month with minimal traffic. This is scalability in the opposite direction — cost proportional to actual load.