---
type: concept
title: Event Geometry Grid (EGG)
created: 2026-05-08
updated: 2026-05-08
tags: [geospatial, h3, data-model, acronym, proposed]
related: [hex-egg-table, h3-geospatial-indexing, spatial-bucketing]
sources: ["research-hexegg-table-2026-05-08.md"]
---
# Event Geometry Grid (EGG)

The **Event Geometry Grid (EGG)** is a proposed expansion of the "EGG" acronym in the [[hex-egg-table]] pattern. It describes the concept of converting individual telemetry events (GPS pings, detections, incidents) into standardized hexagonal cells for efficient analytical processing.

This interpretation follows the pattern of spatial bucketing where raw point-level events are mapped to discrete grid cells, enabling fast equality joins and aggregations without complex geometric comparisons.

> **Note**: This expansion is not canonical. The "EGG" acronym lacks a documented definition in available literature. Alternative interpretations include "Entity Geographic Grid." See [[hex-egg-table]] for the full discussion of the acronym ambiguity.