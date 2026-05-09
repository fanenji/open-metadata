---
type: concept
title: Object Storage Critique
created: 2026-04-04
updated: 2026-04-04
tags: [object-storage, cloud, critique, storage]
related: [space-management-problem, metadata-bottleneck-principle, iceberg-critique, data-lakehouse]
sources: ["Iceberg, The Right Idea - The Wrong Spec - Part 1 of 2 History.md"]
---
# Object Storage Critique

A technically-grounded critique of object storage (e.g., AWS S3) as a foundation for data lakehouse architectures. Key points:

- **HTTP is a poor protocol for high-speed data modification**: HTTP adds latency, overhead, and makes clients complex when speed and concurrency are required.
- **TCP scaling is hard**: A single TCP pipe is not fast enough for high read speeds; multiplexing and retries create a "world of pain."
- **Complexity shifted to clients**: Object storage is simpler to run for vendors but makes client implementations needlessly complex (connection management, backoffs, retries).
- **"Dis-invention"**: Object storage is a step backward from block-based storage, analogous to the fax machine.
- **Vendor motivation**: Cloud vendors pushed object storage to overcharge for block storage (EBS) and to disrupt the SAN vendor market (HP, EMC, IBM, Hitachi). The "big lie" was that object storage is technically superior, embedded in the truth that SAN vendors were terrible.
- **Metadata unsuitability**: Object storage is uniquely unsuited for the metadata operations that data lakehouses require (fast, atomic, scalable, queryable metadata).

The critique argues that object storage is entrenched but technically inferior, and that architectures built on it (including Iceberg) inherit fundamental weaknesses.
