---
type: concept
title: Observability Layer
created: 2026-05-14
updated: 2026-05-14
tags: [data-lineage, data-quality, observability, openmetadata]
related: [data-lineage, lineage-layers, data-quality, data-observability-alerts]
sources: ["explore-the-lineage-view-official-documentation----20260514.md"]
---
# Observability Layer

The Observability Layer is one of the five [[lineage-layers]] in the OpenMetadata lineage view. It integrates data quality insights directly into the lineage graph by displaying test outcomes such as passes, failures, and pending checks on each node.

This layer enables users to:
- Identify potential data quality issues as they trace data flow through pipelines.
- Assess the trustworthiness of data at each stage of transformation.
- Quickly spot failing tests on upstream nodes that may affect downstream consumers.

The Observability Layer bridges the [[data-lineage]] and [[data-quality]] features, providing a unified view of data health and data flow. It is a key component of OpenMetadata's [[data-observability-alerts]] ecosystem.