---
type: concept
title: Feature Store Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [machine-learning, feature-store, streaming, batch-processing]
related: [elt-pattern, blablacar, database-snapshotting-pattern]
sources: ["Data Pipelines Architecture at BlaBlaCar.md"]
---
# Feature Store Architecture

A feature store is an object store designed to ingest data from both streaming and batch sources, and serve it with low latency through an HTTP API for machine learning inference in production services.

## BlaBlaCar Implementation

At [[BlaBlaCar]], the feature store is a Java application backed by BigTable, which provides value historicization and low latency access. It has two main components:

### State Builder
- Processes incoming streaming events (domain events)
- Extracts data from events and stores it (potentially transformed) in BigTable
- Handles both batch and streaming data, including backfilling

### Serve
- HTTP API that allows applications to retrieve states and feature sets
- Supports both batch (high-throughput) and online (low-latency) access
- Online access is the most commonly used mode

## Feature Types

- **Domain event features**: Features ingested directly from streaming domain events
- **Client-defined features (CDFs)**: Features that may involve external computations
- **Feature sets**: Combinations of states used for machine learning models

## Data Sources

- **Streaming**: Domain events from Kafka
- **Batch**: Data from the data warehouse (BigQuery)

## Key Capabilities

- Low-latency serving for production ML inference
- Value historicization via BigTable
- Encoding of feature values
- Backfilling support for historical feature computation