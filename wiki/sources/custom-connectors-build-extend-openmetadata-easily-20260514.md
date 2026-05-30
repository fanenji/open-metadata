---
type: source
title: "Custom Connectors Build Extend Openmetadata Easily 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "Custom Connectors | Build & Extend OpenMetadata Easily"
created: 2026-05-14
updated: 2026-05-14
tags: [custom-connectors, ingestion, python-sdk, extensibility]
related: [custom-connectors, custom-connector-deployment, either-stacktrace-error, openmetadata-connectors, ingestion-framework, pull-based-ingestion-model, metadata-ingestion-workflow]
sources: ["custom-connectors-build-extend-openmetadata-easily-20260514.md"]
---

# Custom Connectors | Build & Extend OpenMetadata Easily

Official OpenMetadata documentation (v1.12.x) for building custom connectors. This guide provides a complete 6-step workflow for creating a custom Python connector class that extends the `Source` base class and yields `CreateEntityRequest` objects for ingestion into OpenMetadata.

## Key Topics

- The `Source` base class and the `_iter` generator method
- The `Either`/`StackTraceError` pattern for structured error handling
- Packaging custom connector code with `setup.py`
- Building a custom ingestion Docker image based on `openmetadata/ingestion`
- Configuring the connector in the UI using the full Python module name
- Reference to the working demo in the OpenMetadata Demos repository

## Connections

- Extends the [[openmetadata-connectors]] concept by explaining how to build connectors beyond the 90+ built-in ones.
- The custom connector is a component of the [[ingestion-framework]]; the `Source` class and `Workflow` are part of this framework.
- Custom connectors follow the same [[pull-based-ingestion-model]] as built-in connectors.
- The custom connector replaces the standard connector in step 4 of the [[metadata-ingestion-workflow]].
- The [[python-sdk]] is referenced as the tool for understanding how to create entities.

## Caveats

- The guide references version 1.4.4 for the demo, while the wiki is based on v1.12.x. The `Either`/`StackTraceError` pattern may have been introduced or changed between versions.
- The guide explicitly states "We do not have docs and examples of all the supported Services" and directs users to integration tests for examples.