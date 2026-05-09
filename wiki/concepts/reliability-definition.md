---
type: concept
title: Reliability Definition
created: 2026-04-29
updated: 2026-04-29
tags: [reliability, fault-tolerance, distributed-systems]
related: [distributed-systems-failure-modes, data-observability-definition, maintainability-definition]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Reliability Definition

Reliability, as defined in DDIA, primarily means fault tolerance — the ability of a system to continue working despite failures such as network interruptions, node crashes, or other unexpected events.

## Key Techniques

- **Replication**: Copying data across multiple nodes to tolerate node failures.
- **Redundancy**: Having backup components that can take over when primary components fail.
- **Graceful Degradation**: Continuing to provide partial service when full service is not possible.

## Relevance to Data Platform

Reliability is a core design goal for the Data Platform. Understanding fault tolerance techniques is essential for designing pipelines that can withstand failures without data loss or corruption.
