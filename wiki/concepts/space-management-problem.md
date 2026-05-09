---
type: concept
title: The Space Management Problem
created: 2026-04-04
updated: 2026-04-04
tags: [storage, databases, fragmentation, metadata, architecture]
related: [object-storage-critique, metadata-bottleneck-principle, iceberg-critique, data-lakehouse]
sources: ["Iceberg, The Right Idea - The Wrong Spec - Part 1 of 2 History.md"]
---
# The Space Management Problem

The set of storage challenges that databases solve but file systems and object storage cannot adequately handle. These include:

- **Fragmentation**: As data changes, free space must be reclaimed. File systems and object storage handle this poorly, leading to performance degradation over time.
- **Impedance mismatch**: Real-world data (rows) has arbitrary sizes; storage media works in powers-of-two blocks. Databases optimize this mapping.
- **Concurrency and locking**: File systems lack fine-grained locking for concurrent writes. Retry-based coordination (creating new files) leads to fragmentation hell.
- **Atomicity**: File systems are terrible at atomic operations across multiple files. Databases have solved this since the 1970s.
- **Temp space management**: Databases need fast, temporary space for joins and sorts. File systems are not optimized for this.
- **Custom compression**: Databases can tailor compression algorithms to data types (bit-packing for integers, LZ4 for strings, run-length encoding for columnar data).
- **Checksumming and bit-rot detection**: Databases detect and repair data corruption; file systems are poor at this.

The concept is central to the critique of Apache Iceberg: Iceberg relies on object storage, which does not solve the Space Management Problem, and its metadata layer inherits these weaknesses.
