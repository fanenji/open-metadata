---
type: source
title: "Iceberg, The Right Idea - The Wrong Spec - Part 1 of 2: History"
created: 2026-04-04
updated: 2026-04-04
tags: [iceberg, critique, object-storage, metadata, data-lakehouse, history]
related: [iceberg-critique, space-management-problem, object-storage-critique, metadata-bottleneck-principle, parquet, postgresql, data-lakehouse]
sources: ["Iceberg, The Right Idea - The Wrong Spec - Part 1 of 2 History.md"]
authors: ["database-doctor"]
year: 2025
url: "https://database-doctor.com/posts/iceberg-is-wrong-1.html"
venue: "database-doctor.com"
---
# Iceberg, The Right Idea - The Wrong Spec - Part 1 of 2: History

A historically-grounded technical critique of Apache Iceberg's design, arguing that its flaws are severe enough to cause a "HADOOP-style disaster." The author traces the history of storage, file systems, databases, and cloud object storage to establish the foundational concept of "The Space Management Problem" — the set of challenges (fragmentation, concurrency, atomicity, impedance mismatch, compression, checksumming, temp space) that databases solve but file systems and object storage cannot. The post argues that Iceberg's reliance on object storage for metadata management is fundamentally flawed, because metadata must be fast, atomic, scalable, and queryable — properties object storage uniquely lacks. The author praises Parquet as a genuine open standard success and PostgreSQL as a model of vendor independence, while critiquing cloud vendors for pushing object storage for profit and lock-in. This is Part 1 of a two-part series; the specific Iceberg spec critique is deferred to Part 2.

## Key Arguments

- **The Space Management Problem**: Databases solve fragmentation, concurrency, atomicity, impedance mismatch, compression, checksumming, and temp space — problems file systems and object storage cannot handle.
- **Object Storage critique**: HTTP-based storage is technically inferior to block storage for high-speed data modification; cloud vendors pushed it for profit and to disrupt SAN vendors.
- **Metadata bottleneck**: Metadata must be fast, atomic, scalable, and queryable. Object Storage is uniquely unsuited for this.
- **Metadata is small**: Metadata is ~6 orders of magnitude smaller than data (10PB data → 10TB metadata). A single server can handle it.
- **Lock-in at any layer**: Vendor-specific storage formats hold data hostage. Openness is table stakes.
- **Parquet as genuine success**: Open, standardized columnar format that broke the closed storage format pattern.
- **PostgreSQL as model**: Truly open database that shed its "toy" label by 2015, demonstrating vendor independence.

## Historical Context

The post traces the evolution from early file systems (FAT, FFS, HFS) through the SAN vendor era (HP, EMC, IBM, Hitachi), the database lock-in era (Oracle, SAP), the emergence of ODBC/JDBC as client-side open protocols, the rise of cloud analytics (Snowflake, Databricks, Dremio), and the emergence of Parquet from the HADOOP ecosystem. It argues that cloud vendors pushed object storage as a "big lie" embedded in a truth (SAN vendors were terrible), creating a new form of lock-in.

## Connection to Part 2

This is the historical foundation. The specific critique of Iceberg's metadata specification is deferred to Part 2, which is referenced at the end of the post.
