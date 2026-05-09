---
type: concept
title: Cloud-Native Data Systems
created: 2026-04-29
updated: 2026-05-07
tags: [cloud, architecture, distributed-systems, object-stores]
related: [object-store-abstraction, kubernetes, data-lakehouse, scalability-definition, geopolitical-risk-in-cloud, designing-data-intensive-applications, kubernetes-etl-deployment-strategies, distributed-systems-failure-modes]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Cloud-Native Data Systems

Cloud-native data systems are built on top of cloud services (particularly object stores like S3, GCS, Azure Blob) as the foundational abstraction, rather than on local disks or virtual block devices. This paradigm shift fundamentally changes how databases and data systems are architected, enabling new architectural patterns.

## Key Characteristics

- **Object Store as Foundation**: Object stores provide a new abstraction layer different from block devices or file systems, with different behavior (eventual consistency, different API semantics). Replication happens at the object store level rather than at the database level, fundamentally changing how data systems are built and operated.
- **Elastic Storage**: Object stores provide virtually unlimited storage capacity, eliminating the need for disk capacity planning.
- **Separation of Compute and Storage**: Compute resources can be scaled independently from storage, enabling serverless and auto-scaling patterns.
- **Serverless Scaling**: Cloud-native systems excel at scaling down to very low load cheaply (e.g., $0.13/month for a serverless website), making it feasible to run services with minimal traffic, as well as scaling up horizontally.

## Comparison with Traditional Architecture

| Aspect | Traditional | Cloud-Native |
|--------|-------------|--------------|
| Storage | Local disks or block devices (EBS) | Object stores (S3, GCS, Azure Blob) |
| Replication | At database level | At object store level |
| Scaling | Vertical (bigger machines) | Horizontal + serverless |
| Capacity Planning | Required | Eliminated |

## Impact on System Design

- **Database Architecture**: Databases built on object stores (e.g., Snowflake, DuckDB, Dremio) have fundamentally different replication, durability, and consistency models compared to traditional databases.
- **Operational Simplicity**: Managed services hide many operational details, but understanding the underlying cloud-native internals remains valuable for diagnosing performance and cost issues.
- **Scaling Down**: The ability to scale to zero and pay only for storage is a key advantage of cloud-native systems, as important as scaling up.

## Connections to the Wiki

This concept is foundational for understanding modern [[data-lakehouse]] architectures, which build on object stores with ACID transactions. It also relates to [[kubernetes-etl-deployment-strategies]] for cloud-native deployment patterns of ETL workloads, and the second edition of [[designing-data-intensive-applications]] integrates cloud-native systems architecture throughout its narrative. The shift toward object stores directly impacts decisions about storage engine selection, replication strategies, and cost modeling.