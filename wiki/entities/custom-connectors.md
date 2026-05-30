---
type: entity
title: Custom Connectors
created: 2026-05-14
updated: 2026-05-15
tags: [custom-connectors, extensibility, ingestion, integration, python-sdk]
related: [custom-connector-deployment, either-stacktrace-error, ingestion-framework, integration-approaches-comparison, metadata-ingestion-workflow, openmetadata-connectors, pull-based-ingestion-model, python-sdk, schema-first-approach]
sources: ["Mini-Webinar on Custom Connectors dataintegration connectors ingestion datacatalog metadata.md", "custom-connectors-build-extend-openmetadata-easily-20260514.md"]
---

# Custom Connectors

Custom connectors are user-defined Python classes that extend the OpenMetadata [[ingestion-framework]]'s `Source` class (`metadata.ingestion.api.steps.Source`) to integrate internal business systems with the platform. They bridge the gap between OpenMetadata's 90+ built-in connectors and proprietary or organization-specific data sources. Custom connectors follow the same [[pull-based-ingestion-model]] as built-in connectors and are configured via the OpenMetadata UI, providing full UI integration for service creation, scheduling, and log viewing.

## When to Use Custom Connectors

Custom connectors are the recommended approach when:
- You have internal business systems with metadata that needs to be shared alongside third-party tools
- You want full UI integration (service creation, scheduling, log viewing) without managing separate scripts
- Your integration needs align with the abstractions of the ingestion framework

For simpler, one-off operations, raw API calls or the [[python-sdk]] may be more appropriate. See [[integration-approaches-comparison]] for a decision matrix.

Custom connectors support every service type: Database, Pipeline, Dashboard, Messaging, ML Model, Storage, Search, and Metadata.

## Architecture and Implementation

### Extending the Source Class

A custom connector extends `Source` from `metadata.ingestion.api.steps.Source`. The class must be implemented in Python and follow the interface expected by the ingestion framework.

### The Generator Method (`_iter`)

The core of a custom connector is the generator method that produces OpenMetadata entities. Implement the `_iter` generator method (or `next_record` in older versions) which:

- Iterates over the source data
- Creates OpenMetadata standard objects (`DatabaseService`, `Database`, `Schema`, `Table`, etc.)
- Yields them as `CreateEntityRequest` objects (e.g., `CreateTableRequest`) wrapped in `Either` instances:
  - `Either.right` — a successful `CreateEntityRequest`
  - `Either.left` — a `StackTraceError` (name, message, stack trace)

The workflow iterates over this generator to send all entities to the sink.

### Connection Options

Define custom parameters (e.g., `source_directory`, `business_unit`) that are configurable per service instance in the UI. These are passed to the connector when the ingestion pipeline is configured.

### Error Handling

Errors raised during ingestion are captured using the `StackTraceError` pattern. They are logged and displayed in a summary table at the end of execution, allowing you to trace failures without aborting the entire pipeline.

## Deployment

Custom connectors are deployed by extending an OpenMetadata ingestion image. The typical steps are: prepare the connector, package it, build a custom image, and configure it via the UI. See [[custom-connector-deployment]] for a complete 6-step workflow.

A common approach is to create a Dockerfile that extends the base ingestion image:

```dockerfile
FROM openmetadata/ingestion:latest
COPY ./my_connector /my_connector
RUN pip install /my_connector
```

This ensures the custom class is available when the ingestion workflow loads it via the source class name.

## Demo: CSV Connector

The webinar demonstrates a CSV-based custom connector that:
- Reads a CSV file defining table names, column names, and types
- Translates the data into OpenMetadata standard objects (`DatabaseService` → `Database` → `Schema` → `Table`)
- Accepts connection options: `source_directory` and `business_unit`
- Integrates fully with the UI for service creation, scheduling, and log viewing

The demo code is available in the OpenMetadata Demo Repository.

## Benefits

- **Focus only on source logic** — The ingestion framework handles translation, API calls, and scheduling
- **UI integration** — Any OpenMetadata admin can create and schedule ingestion pipelines
- **Reuse of Python SDK** — The same objects and helpers used in CI/CD scripts work in custom connectors

## Limitations

- Less flexibility than raw API calls — the connector must fit the ingestion framework's workflow structure
- Language-specific (Python/Java) — requires a Python or Java environment

## Related

- [[openmetadata-connectors]] — the library of 90+ built-in connectors
- [[ingestion-framework]] — the backbone for moving metadata
- [[metadata-ingestion-workflow]] — the 8-step UI-driven process
- [[python-sdk]] — for understanding how to create entities
- [[pull-based-ingestion-model]]
- [[integration-approaches-comparison]]
- [[either-stacktrace-error]]
- [[custom-connector-deployment]]