---
type: concept
title: Event-Driven ETL
created: 2026-04-08
updated: 2026-04-08
tags: [etl, orchestration, automation, kestra]
related: [kestra, anomaly-detection, aws-s3]
sources: ["Beyond Storing Data How to Use DuckDB, MotherDuck and Kestra for ETL.md"]
---
# Event-Driven ETL

[[event-driven-etl]] is a data engineering pattern where data pipelines are triggered by external, real-time events rather than relying solely on fixed, periodic schedules (batch processing).

### Implementation with Kestra
Using an orchestrator like [[kestra]], an event-driven pipeline can be configured to "listen" to changes in infrastructure, such as:
- **Object Storage Triggers**: An AWS S3 `PUT` event (new file upload) triggers a DuckDB transformation task immediately.
- **Webhooks**: An external API call triggers a data refresh.

### Advantages over Batch Processing
- **Reduced Latency**: Data is processed as soon as it becomes available, significantly reducing the "time-to-value" for downstream analytics.
- **Efficiency**: Resources are only consumed when there is actual work to be done, avoiding the overhead of running empty scheduled jobs.
- **Automated Response**: Enables immediate downstream actions, such as [[anomaly-detection]] or automated alerting, as soon as new data enters the system.
