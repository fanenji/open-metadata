---
type: concept
title: Object Store Abstraction
created: 2026-04-29
updated: 2026-04-29
tags: [cloud, storage, architecture]
related: [cloud-native-data-systems, data-lakehouse, kubernetes]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Object Store Abstraction

Object stores (like Amazon S3, Google Cloud Storage, Azure Blob Storage) provide a fundamentally different abstraction from traditional block devices or file systems. Understanding this difference is critical for building cloud-native data systems.

## Key Differences from Block Storage

- **No File System**: Object stores are not file systems. They provide a flat namespace of objects identified by keys.
- **Different Consistency Model**: Object stores typically offer strong consistency for PUT operations but eventual consistency for LIST operations (though this varies by provider).
- **Different Performance Characteristics**: Object stores have higher latency than local disks but provide virtually unlimited throughput through parallelism.
- **Built-in Replication**: Object stores handle replication and durability at the infrastructure level.

## Impact on Data System Design

Building on object stores changes how databases handle replication, consistency, and operations. For example, a database built on an object store may not need to implement its own replication protocol — it can rely on the object store's built-in replication.
