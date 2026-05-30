---
type: source
title: "Mini-Webinar on Custom Connectors"
created: 2026-05-14
updated: 2026-05-14
tags: [custom-connectors, ingestion, python-sdk, schema-first, webinar]
related: [custom-connectors, python-sdk, ingestion-framework, schema-first-approach, openmetadata-connectors, metadata-ingestion-workflow, bot-authentication, owner-propagation, tag-inheritance-for-masking, integration-approaches-comparison]
sources: ["Mini-Webinar on Custom Connectors dataintegration connectors ingestion datacatalog metadata.md"]
authors: [Pere Miquel Brull]
year: 2023
url: "https://www.youtube.com/watch?v=fDUj30Ub9VE"
venue: "OpenMetadata Community Meetup"
---
# Mini-Webinar on Custom Connectors

Presented by Pere Miquel Brull (OpenMetadata engineer), this webinar covers the foundations of OpenMetadata's schema-first approach, the Python SDK, the ingestion framework, and a live demo on building custom connectors. It explains the three-tier integration approach (raw API calls, SDK, custom connector) with trade-offs, and demonstrates a CSV-based custom connector that reads table definitions from a file and ingests them into OpenMetadata.

Key topics include:
- The OpenMetadata Standard as a common language for defining data assets and people
- How JSON Schema definitions drive code generation for Java, Python, TypeScript, DB storage, and documentation
- The ingestion workflow pipeline: Source → Processor → Sink
- Custom connector implementation by extending the `Source` class and implementing `next_record()`
- Deployment via custom Docker images extending the OpenMetadata ingestion image
- Q&A on tag propagation (future roadmap) and ownership propagation (available in v0.13.2)

The webinar emphasizes that custom connectors are the recommended approach for integrating internal business systems, offering the best balance of abstraction and UI integration.