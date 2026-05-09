---
type: source
title: Designing Data-intensive Applications with Martin Kleppmann
created: 2026-04-29
updated: 2026-05-07
tags:
  - distributed-systems
  - data-systems
  - cloud-native
  - reliability
  - scalability
  - podcast
  - interview
related:
  - martin-kleppmann
  - chris-riccomini
  - kafka
  - cloud-native-data-systems
  - distributed-systems-failure-modes
  - geopolitical-risk-in-cloud
  - scalability-definition
  - reliability-definition
  - maintainability-definition
  - object-store-abstraction
  - formal-verification
  - designing-data-intensive-applications
  - jay-kreps
  - geopolitical-resilience-in-data-architecture
  - formal-verification-for-data-systems
sources:
  - "Designing Data-intensive Applications with Martin Kleppmann.md"
authors:
  - "Martin Kleppmann"
  - "Chris Riccomini"
year: 2026
url: "https://www.youtube.com/watch?v=SVOrURyOu_U"
venue: "The Pragmatic Engineer Podcast"
---
# Designing Data-intensive Applications with Martin Kleppmann

This page summarizes a podcast interview with **Martin Kleppmann**, author of the influential book *Designing Data-Intensive Applications* (DDIA), hosted by **Gergely Orosz** on *The Pragmatic Engineer*. The conversation covers Kleppmann's career journey from startups through LinkedIn to academia, the writing of DDIA's first and second editions, and key themes in distributed systems and data-intensive application design.

## Background

### Career Journey
- **Go Test It** — First startup, cross-browser testing with Selenium.
- **Rapportive** — Social CRM integrated into Gmail, acquired by LinkedIn.
- **LinkedIn** — Worked on **Kafka** and **Samza**, learning distributed systems at scale; this experience heavily influenced the book.
- **Academia** — Later moved to academic research.

### Book Writing
- **First edition** — Four-year writing process; structured into three parts: foundational data systems, distributed data, and derived data. Emphasises teaching trade-offs rather than prescribing solutions.
- **Second edition** — Co-authored with **Chris Riccomini**. Major updates include cloud-native systems architecture built on object stores.

## Key Topics

- **Reliability, Scalability, Maintainability** — DDIA’s three pillars. Reliability means fault tolerance; scalability includes both scaling up and scaling down (serverless); maintainability is the third and often overlooked pillar.
- **Cloud-native systems architecture** — Building data systems on top of object stores (e.g., S3) as a foundational abstraction. This fundamentally changes replication models and system design.
- **Object store as abstraction** — Object stores provide a new abstraction layer that is distinct from block devices or file systems, enabling novel database architectures.
- **Sharding/Partitioning** — Horizontal scaling across machines is still relevant at very large scale but less pressing because single machines have become more powerful.
- **Distributed systems failure modes** — Network delays are unbounded, node crashes are ambiguous, partial failures are common. Understanding these is critical.
- **Formal verification** — Increasingly important, especially with AI-generated code (often called “vibe coding”), creating a need for formal proofs of correctness.
- **Geopolitical resilience** — European dependence on US cloud services is a real architectural risk. Multi-region and multi-cloud deployments are worth considering for critical workloads.
- **Serverless scaling down** — The ability to handle very low loads cheaply (e.g., $0.13/month) is as important as scaling up.
- **Cloud services** — Higher-level abstractions are fine for business logic, but understanding the internals of those services is a superpower for diagnosing problems.

## Key Quotes

> "If you rely on a higher level abstraction, you're no longer thinking about the lower level details. If you're building higher level business logic, actually, I think it's just fine."

> "Knowing a bit about the internals is actually like a superpower."

> "The cloud has helped quite a bit at the lower end of scaling down."

> "European dependence on US cloud services... it's no longer unthinkable."

## Relevance and Connections

### Relevance to Data Platform

This source provides foundational distributed systems theory that underpins architectural decisions for the Data Platform. It emphasises understanding trade-offs (reliability vs. cost vs. complexity) and the shift to cloud-native architectures built on object stores.

### Connections to Existing Wiki

- [[data-lakehouse]] — Cloud-native systems architecture discussion relates to lakehouse evolution.
- [[kubernetes-etl-deployment-strategies]] — Scalability and cloud-native deployment patterns.
- [[data-observability-definition]] — Reliability concept partially overlaps.
- [[model-context-protocol]] — AI-generated code quality concerns relate to Sonar discussion.
- [[dbt-cloud]] — Managed services abstraction parallels.
- [[data-contract-platform]] — Reliability and maintainability goals.
- [[data-ingestion-architectural-patterns]] — Kafka as data integration point.