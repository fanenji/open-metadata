---
type: concept
title: Distributed Systems Failure Modes
created: 2026-04-29
updated: 2026-05-07
tags: [distributed-systems, reliability, fault-tolerance]
related: ["reliability-definition", "cloud-native-data-systems", "data-observability-definition", "designing-data-intensive-applications"]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Distributed Systems Failure Modes

Distributed systems failure modes are the fundamental ways in which distributed systems can fail, as distinct from single‑machine systems. These are covered extensively in [[designing-data-intensive-applications]]'s chapter "The Trouble with Distributed Systems." Understanding these failure modes is essential for building reliable, fault‑tolerant systems.

## Key Failure Modes

- **Network delays are unbounded**: There is no upper bound on how long a message might take to traverse the network. A message might arrive in 100 microseconds or take 10 years.
- **Node crashes are ambiguous**: A node can become unavailable for many reasons: software crash, hardware failure, power loss, or network disconnection. The system cannot always distinguish between a crashed node and a disconnected one.
- **Partial failures**: Some parts of the system may fail while others continue working, making it difficult to reason about system state.
- **Clock skew**: Clocks on different machines drift, making time‑based coordination unreliable.
- **Timing assumptions are dangerous**: Making assumptions about timing (e.g., "this operation will complete within X milliseconds") is dangerous because real‑world behavior can violate these assumptions. Distributed system theory avoids making timing assumptions where possible.

## Implications

- **Fault tolerance requires redundancy**: Replication, retries, and timeouts are essential mechanisms.
- **Consistency vs. availability trade‑off**: The CAP theorem and related results show that distributed systems must choose between strong consistency and high availability during network partitions.
- **Design for failure**: Systems should be designed assuming failures will occur, not hoping they won't.
- Understanding these failure modes is essential for designing reliable data pipelines and choosing appropriate replication and consistency strategies. It also informs [[data-observability-definition]] by highlighting what can go wrong.

## Related Wiki Pages

- [[data-observability-definition]] — Reliability and fault tolerance are core concerns of data observability.
- [[designing-data-intensive-applications]] — DDIA's chapter "The Trouble with Distributed Systems" is the definitive treatment of these failure modes.
- [[cloud-native-data-systems]] — Cloud services abstract away some failure modes but introduce new ones.