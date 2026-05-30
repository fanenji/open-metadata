---
type: source
title: "Research: ResourceQuota Sizing for OpenMetadata Ingestion Workloads"
created: 2026-05-15
updated: 2026-05-15
tags: [kubernetes, resource-quotas, sizing, ingestion, performance, research]
related: [resource-quota-sizing-ingestion, tag-usage-query-bottleneck, kubernetes-native-orchestrator, omjob-operator, ingestion-framework, openmetadata-system-architecture, external-dependencies-configuration, reindexing-search, filter-patterns, ingestion-pipeline-troubleshooting]
sources: ["research-resourcequota-sizing-for-openmetadata-ingestion-wo-2026-05-15.md"]
---
# Research: ResourceQuota Sizing for OpenMetadata Ingestion Workloads

A deep research synthesis on proper resource quota sizing for OpenMetadata ingestion workloads in Kubernetes. The source analyzes official documentation, Helm chart defaults, community performance reports (including Issue #27158 on the `tag_usage` bottleneck), and best practices to provide a comprehensive sizing guide. It identifies the [[tag-usage-query-bottleneck]] as a critical database performance issue, proposes a [[resource-quota-sizing-ingestion|workload-type sizing matrix]], and documents gaps in official guidance including the lack of tiered scaling recommendations and the undocumented interaction between job lifecycle parameters and namespace `ResourceQuota` policies.
