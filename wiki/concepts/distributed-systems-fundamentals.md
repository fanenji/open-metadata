---
type: concept
title: Distributed Systems Fundamentals
created: 2026-04-29
updated: 2026-04-29
tags: [distributed-systems, reliability, scalability, maintainability]
related: [cloud-native-architecture-paradigm, formal-verification, ddia-book, martin-kleppmann]
sources: ["Designing Data-intensive Applications with Martin Kleppmann-SUMMARY.md"]
---
# Distributed Systems Fundamentals

Core concepts from [[Martin Kleppmann]]'s *Designing Data-Intensive Applications* that underpin all modern data platforms.

## Three Core Qualities

- **Reliability**: Fault tolerance — the system continues to function despite network failures, node crashes, or other faults. Achieved through replication and redundancy.
- **Scalability**: Mechanisms to handle load increases (horizontal scaling, shared-nothing architecture) and decreases (serverless, pay-per-use). Scaling down is as important as scaling up.
- **Maintainability**: The system must be understandable, modifiable, and operable over time.

## The Trouble with Distributed Systems

Empirical evidence justifies pessimistic assumptions:

- **Network latency**: No upper bound guaranteed. A message can arrive in 100 µs or never arrive.
- **Node crashes**: Not just software crashes — hardware failure, power loss, node alive but disconnected from network. Distinctions matter for recovery protocols.
- **Clocks**: Tempting to assume they are correct, but even NTP-synchronized clocks are not precise enough for critical algorithms.

Failures happen. Edge cases happen. Claims that "failures are rare, don't worry" are false certainties.

## Relevance to Data Platform Architecture

These fundamentals explain why data platforms need:
- Replication strategies (not just for scale, but for fault tolerance)
- Pessimistic consistency models
- Careful trade-off analysis between reliability and operational cost
- Understanding of internals for debugging and service selection