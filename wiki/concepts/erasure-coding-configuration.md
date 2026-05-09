---
type: concept
title: Erasure Coding Configuration
created: 2026-04-29
updated: 2026-04-29
tags: [storage, resilience, capacity-planning]
related: [minio, data-platform-infrastructure-sizing]
sources: ["Dimensionamento.md"]
---
# Erasure Coding Configuration

Erasure Coding is a data protection method that splits data into fragments, expands and encodes them with redundant data pieces, and stores them across different locations. MinIO uses this to provide resilience without the overhead of full replication.

## MinIO Configuration

The data platform uses an Erasure Code Stripe Size of 16 and an Erasure Code Parity of 8. This means:

- **Usable capacity**: 32 TiB (50% of total)
- **Total capacity**: 64 TiB
- **Storage efficiency**: 50%
- **Drive Failure Tolerance**: Can lose 8 drives out of 16
- **Server Failure Tolerance**: Can lose 2 servers out of 4

This configuration is a critical design decision that drives storage efficiency, capacity, and failure tolerance for the entire platform. The 50% efficiency means that for every 2 TB of raw storage, only 1 TB is usable. Capacity planning must account for this overhead, especially when compute engines like Dremio consume distributed storage from the same MinIO cluster.