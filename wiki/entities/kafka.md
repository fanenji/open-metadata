---
type: entity
title: Kafka
created: 2026-01-15
updated: 2026-05-07
tags: ["streaming", "ingestion", "stream-processing", "messaging", "distributed-systems", "data-integration", "event-streaming", "infrastructure", "data-platform"]
related: ["kafka-ingestion-layer", "linkedin", "jay-kreps", "samza", "stream-processing-ingestion", "elt-pattern", "martin-kleppmann", "designing-data-intensive-applications", "data-ingestion-architectural-patterns"]
sources: ["Analisi Architettura.md", "Designing Data-intensive Applications with Martin Kleppmann.md", "Dimensionamento.md"]
---

# Apache Kafka

Apache Kafka is a distributed streaming platform originally built at LinkedIn by [[jay-kreps]] and his team. It serves as a general-purpose abstraction for moving data between various sources and downstream sinks, acting as a data integration point and an event streaming platform for building real-time data pipelines and streaming applications. It frequently utilizes **Kafka Connect** to ingest data from RDBMS and other sources.

## Motivation

Kafka was created to solve the data integration problem at LinkedIn: multiple databases and event-generating systems (including user activity events) produced data in a stream shape, and many downstream systems (data warehouses, Hadoop clusters for machine learning, etc.) needed to consume it. Kafka served as the lowest common denominator integration point by providing a unified append-only log abstraction.

## Key Concepts

- **Append-only log** — The core abstraction; an ordered, immutable sequence of records.
- **Data integration point** — Kafka acts as a central hub connecting producers and consumers, with **Kafka Connect** simplifying data ingestion from external systems like RDBMS.
- **Stream processing** — Frameworks like [[samza]] enable real-time processing of Kafka streams.
- **Design principles** — Understanding its design (partitioning, replication, and the append-only log) is essential for building reliable data pipelines.

## Role in *Designing Data-Intensive Applications*

[[martin-kleppmann]] worked on the stream processing team at LinkedIn, contributing to Samza (a stream processing framework on top of Kafka). His experience with Kafka directly shaped the ideas in *Designing Data-Intensive Applications*, particularly the chapters on stream processing and derived data.

## Relevance and Connections to Wiki

Kafka is a foundational technology for [[stream-processing-ingestion]] and [[elt-pattern]] architectures. It also plays a key role in [[data-ingestion-architectural-patterns]] and feeds data into [[data-lakehouse]] architectures. Understanding Kafka's design principles is essential for building reliable data pipelines.

## Infrastructure Sizing

In the proposed data platform architecture, Kafka is sized with:

- **3 Broker + Zookeeper nodes**: 12 vCPU, 64 GB RAM, 1 TB storage each
- **2 Worker nodes** (for Connect, Schema Registry, Kafka REST Proxy): 12 vCPU, 8 GB RAM, 50 GB storage each

This configuration supports high-throughput event ingestion and stream processing workloads.