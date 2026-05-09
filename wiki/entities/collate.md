---
type: entity
title: Collate
created: 2026-05-06
updated: 2026-05-07
tags: ["managed-service", "enterprise-governance", "software", "metadata", "openmetadata", "company", "collate", "metadata-platform", "data-catalog"]
related: ["openmetadata", "trino", "collate-ai", "model-context-protocol", "openmetadata-mcp-server", "openmetadata-vs-alternatives", "openmetadata-mcp-integration", "openmetadata-cloud-vs-os"]
sources: ["announcing-openmetadata-1-13-20260506.md", "Collate vs OpenMetadata Managed Service for Data Teams at Scale.md", "Embedding an MCP Server into OpenMetadata.md", "OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md", "OpenMetadata MCP.md", "OpenMetadata.md"]
---
# Collate

**Collate** is the company that maintains and develops [[openmetadata]], offering both an open-source version and a managed cloud service. As the commercial entity behind OpenMetadata, Collate provides an enterprise-grade managed service built on the OpenMetadata engine, designed to automate metadata management, discovery, observability, and governance for large-scale data teams. The managed service includes additional AI analytics, advanced governance workflows, proprietary connectors, enterprise-grade support, managed hosting, SLAs, security and compliance features, and professional services and consulting. Collate also develops key components of the OpenMetadata platform, including the [[openmetadata-mcp-server]] and the [[openmetadata-application-framework]]. The official comparison of the different deployment options is available at [getcollate.io/comparison](https://www.getcollate.io/comparison).

## Collate AI

A suite of agentic features designed for intelligent data interaction:
- **AskCollate**: Conversational AI for natural language querying.
- **AI Studio**: A platform for agent creation.
- **AutoPilot**: Specialized agents for automating documentation, tiering, and data quality.

## Enterprise Features

- **Advanced Governance**: Includes a custom workflow builder with trigger-based workflows on asset state transitions, reverse metadata synchronization, and automated classification.
- **Hybrid Search**: Unified keyword and semantic search capabilities.
- **Metadata Exporter**: Support for exporting governance analytics to engines like [[trino]].

## Deployment & Integration

- **Deployment Models**: Offers SaaS, Hybrid, and **BYOC** (Bring Your Own Cloud) models to support various [[data-sovereignty-strategy]] requirements.
- **Integration**: The [[model-context-protocol]] (MCP) is supported through the [[openmetadata-mcp-server]], which was developed by Collate. This integration is available both in the open-source version of OpenMetadata and through Collate's managed service. Collate also developed the [[openmetadata-application-framework]] for building custom applications on the metadata platform.
- **Talks & Contributors**: Shihara and Moit, the presenters of the "Embedding an MCP Server into OpenMetadata" talk, are from Collate, underscoring the company's active role in the OpenMetadata community.

## Related Pages

- [[openmetadata]] — The open-source metadata platform maintained by Collate.
- [[openmetadata-cloud-vs-os]] — Comparison of Cloud vs. Open-Source versions.