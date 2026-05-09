---
type: concept
title: Thoughtful Data Creation
created: 2026-04-29
updated: 2026-04-29
tags: [pattern, performance, geospatial, data-engineering]
related: [flatgeobuf-fgb, serverless-geospatial-architecture]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Thoughtful Data Creation

A performance optimization pattern for cloud-native geospatial data that involves pre-computing attributes to avoid repetitive client-side calculations. This is particularly important when dealing with hundreds or millions of features.

## Example

When displaying building footprints for an entire state, instead of having every web client calculate the area of every polygon each time it accesses the data, an 'area' attribute can be added to each [[flatgeobuf-fgb]] feature. This avoids repetitive client-side math and improves map responsiveness.

## Trade-offs

- **Pre-computed attributes**: Increases storage size but reduces client-side computation.
- **On-demand calculation**: Saves storage but increases client-side processing, which may be acceptable for small datasets but problematic for large ones.